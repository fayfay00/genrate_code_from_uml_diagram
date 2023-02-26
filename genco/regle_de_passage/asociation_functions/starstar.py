import random
from genco.regle_de_passage.generalization import add_fk_to_att_list ,get_primary_keys_list



def STARSTAR(classobj,first_class,second_class,name):
    #get pks from first class
    first_class_pks= get_primary_keys_list(classobj, first_class)
        #get pks from second class
    second_class_pks=get_primary_keys_list(classobj, second_class)
    keys=first_class_pks+second_class_pks
    if not(len(name)== 1):
            #print("this is a not class association") 
            class_to_add=create_class(name,keys)  
            #print(class_to_add) 
            classobj=addclass(classobj,class_to_add)
            #print(classobj)
            return classobj     
    else:
        add_fk_to_att_list(keys, classobj, name)
        return classobj
        

        
        
#############################################################

def create_class(new_class_name,new_attributs):
    class_model={'class_id': {'id': '','name': 'class_name','attributs': []}}
    random_number = random.randint(1000, 10000)
    new_class_id= str(random_number)
    class_model[new_class_id]=class_model.pop('class_id')
    class_model[new_class_id]['id']=new_class_id
    class_model[new_class_id]['name']=new_class_name
    class_model = add_fk_to_att_list(new_attributs, class_model, new_class_id)
    
    return class_model
    
#######################################################
def addclass(classbj,class_to_add):
    print("am adding this class")
    classbj.update(class_to_add)
    return classbj
    