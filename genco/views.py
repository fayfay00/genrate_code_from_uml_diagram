from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
import json

from genco.regle_de_passage.generalization import Generatilization
from genco.regle_de_passage.composition import Composition
from genco.regle_de_passage.association_2 import Association
from sql_script.sql_script import SQL_code_generator

# Create your views here.

def index(request):
    return render(request,'index.html')

def generated (request):
    if request.method == 'POST':
        try:
             input_text = request.POST['input_text']
             data = json.loads(input_text)
             #classes object has all classes we have in our UML diagram
             classes = {cls['id']: cls for cls in data[0]['classes']}
             #relations object has all relations we have in our UML diagram
             relations = {rel['id']: rel for rel in data[1]['relations']}
             #generated_code=Generate_Code(relations,classes)
             classes=Generate_Code(relations,classes)
            
            
             return render(request,'generated.html',{'classes':classes,'relations':relations})
         
         
        except json.JSONDecodeError:
            # Return a bad request response if the JSON is invalid
            return HttpResponseBadRequest('Invalid JSON')
    else:
        # Handle other HTTP methods (e.g. GET) if needed
        return HttpResponse('This view only accepts POST requests')
    

#une proposition kan a yassine

def Generate_Code(relations_dict,classes_dict):
    """_summary_ his function allow us to generate code from the relation's dictionary
    and modify a dictionary that is called mpd dictionairy, in order to save all the 
    changes during the generation process

    Args:
        relations_dict (dict): _description_
        classes_dict (dict): _description_
    """
    relations = relations_dict
    classes = classes_dict
     
    for relation_name,relation_data in relations.items():
        if(relation_data['relation_type']=="association"):
            classes=Association(classes, relation_data['classes'],relation_data['cardinalities'],relation_data['relation_name'] )
            #print(relation_data['classes'])
        elif(relation_data['relation_type']=="generalization"):
            classes = Generatilization(classes, relation_data['class_mother'],relation_data['class_child'])
        elif(relation_data['relation_type']=="composition"):
            classes=Composition(classes, relation_data['class_parent'],relation_data['class_child'])
    # add code for generating code 
    #print(classes)
    #SQL_code_generator(classes,"test_database")
    
    return classes




    
    
    
     

    