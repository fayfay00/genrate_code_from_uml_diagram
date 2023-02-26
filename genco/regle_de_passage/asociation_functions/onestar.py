from genco.regle_de_passage.generalization import add_fk_to_att_list ,get_primary_keys_list

#if 1--------*
def ONESTAR(classobj,first_class,second_class,name):
        #print("onestar")
        classobj=dict(classobj)
        name=str(name)
        first_class_keys = get_primary_keys_list(classobj, first_class)
        if not(len(name)== 1):
            #print(second_class)
            classobj = add_fk_to_att_list(first_class_keys, classobj, str(second_class))
            #print(classobj)
            return classobj
        else:
            associated_class_attributs = classobj[name]['attributs']
            #print(associated_class_attributs)
            keys=associated_class_attributs+first_class_keys
            classobj = add_fk_to_att_list(keys, classobj, str(second_class))
            del classobj[name]
            return classobj
        

###################################################################################################
#if *--------1
def STARONE(classobj,first_class,second_class,name):
            #print("onestar")
            name=str(name)
            classobj=dict(classobj)
            foreign_keys = get_primary_keys_list(classobj,second_class )
            if not(len(name)== 1):
                #print(second_class)
                # ajouter les clés étrangères à la liste des attributs de la classe fille
                classobj = add_fk_to_att_list(foreign_keys, classobj, str(first_class))
                #print(classobj)
                return classobj
            else:
                associated_class_attributs = classobj[name]['attributs']
                keys=foreign_keys+associated_class_attributs
                classobj = add_fk_to_att_list(keys, classobj, str(first_class))
                del classobj[name]
                return classobj
    