from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
import json

# Create your views here.

def index(request):
    return render(request,'index.html')

def generated (request):
    if request.method == 'POST':
        try:
             input_text = request.POST['input_text']
             data = json.loads(input_text)
             classes = {cls['id']: cls for cls in data[0]['classes']}
             relations = {rel['id']: rel for rel in data[1]['relations']}
             
             return render(request,'generated.html',{"classes":classes,"relations":relations})
        except json.JSONDecodeError:
            # Return a bad request response if the JSON is invalid
            return HttpResponseBadRequest('Invalid JSON')
    else:
        # Handle other HTTP methods (e.g. GET) if needed
        return HttpResponse('This view only accepts POST requests')
    


def generate_Code(relations_dict,classes_dict):
    """_summary_this function allow us to generate code from the relation's dictionary
    """
    relations=relations_dict
    classes=classes_dict
    for relation_id,relation_data in relations.item():
        if(relation_data.relation_type=="assocoation"):
            pass
        elif(relation_data.relation_type=="generalization"):
            pass
        elif(relation_data.relation_type=="composition"):
            pass



    