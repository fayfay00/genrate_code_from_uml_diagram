    #########################################################################################################


def Generatilization(classobj,mother,child): 
    if(not (len(mother)>1 and len(child)>1)):
        if(len(mother)==1 and len(child)==1 ):
            #we pass the current class object and the mother id in order to get all the primary keys that it has
            child=str(child[0])
            foreign_keys = get_primary_keys_list(classobj,mother[0])
            classobj=add_fk_to_att_list(foreign_keys,classobj,child)
            #print(classobj)
            return classobj
        elif(len(mother)>1 and len(child)==1):
            child=str(child[0])
            for_keys=[]
            for each_mother in mother:
                one_mom=str(each_mother)
                #get all pk changed to pk 
                foreign_key = get_primary_keys_list(classobj, one_mom)
                #assemble all of previous keys in order to add them to the child class
                for_keys= for_keys + foreign_key
                print(each_mother)
            classobj=add_fk_to_att_list(for_keys,classobj,child)
        elif(len(mother)==1 and len(child)>1):
            foreign_keys = get_primary_keys_list(classobj,mother[0])
            for each_child in child:
                each_child=str(each_child)
                classobj=add_fk_to_att_list(foreign_keys,classobj,each_child)
                print(each_child)
            
        #print(for_keys)
        return classobj

            
            

#########################################################################################################

def change_pk_to_fk(pk_list):
    """_summary_ changes the primary keys into a foreign keys by changing the attribut_key_type
    inside attribut list  
    Args:
        pk_list (_type_): _description_ the primary key list 
    Returns:
        _type_: _description_ return the same list as pk_list but with foreign_key value
    """
    fk_list = [{**attr_dict, 'attribut_key_type': 'foreinkey'} for attr_dict in pk_list if attr_dict['attribut_key_type'] == 'primarykey']
    # print(fk_list)
    return fk_list

#########################################################################################################

def add_fk_to_att_list(foreign,classobj,class_id):
    """_summary_this function adds the foreign keys to the object we have 

    Args:
        foreign (_type_): _description_
        classobj (_type_): _description_
        class_id (_type_): _description_
    """
    for dicts in foreign:
            classobj[class_id]['attributs'].append(dicts)
    return classobj

#########################################################################################################

def get_primary_keys_list(classobj,mother):
    """_summary_ this function will return a dictionary with all primary keys

    Args:
        classobj (_type_): _description_
        mother (_type_): _description_
    """
    mother=str(mother)
    mother_attributs_list= classobj[mother]['attributs']
    # permet de extraire les clé primaire d'une class
    primary_keys = [attr_dict for attr_dict in mother_attributs_list if attr_dict['attribut_key_type'] == 'primarykey']
    # permet de changer les type de cle de pk a foreign key
    foreign_keys = change_pk_to_fk(primary_keys)
    #here we return the list of foreign keys
    return foreign_keys