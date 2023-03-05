###############################
from genco.regle_de_passage.generalization import add_fk_to_att_list ,get_primary_keys_list


def Association(classobj, classes, cardinalities,name):
    child = classes[0]
    parent =classes[1]
    if not(len(name)== 1):
        # récupérer la classe mère et la classe fille de la relation 
        if cardinalities == ['1', '0..1']:
            foreign_keys = get_primary_keys_list(classobj, child)
            # ajouter les clés étrangères à la liste des attributs de la classe fille
            classobj = add_fk_to_att_list(foreign_keys, classobj, parent)
        elif cardinalities == ['0..1', '1']:
            foreign_keys = get_primary_keys_list(classobj, parent)
            # ajouter les clés étrangères à la liste des attributs de la classe mère
            classobj = add_fk_to_att_list(foreign_keys, classobj, child)
        elif cardinalities == ['1', '1']:
            # récupérer les clés primaires des deux classes
            foreign_keys_parent = get_primary_keys_list(classobj, parent)
            foreign_keys_child = get_primary_keys_list(classobj, child)
            # ajouter les clés étrangères à la liste des attributs de chaque classe
            classobj = add_fk_to_att_list(foreign_keys_child, classobj, parent)
            classobj = add_fk_to_att_list(foreign_keys_parent, classobj, child)
        return classobj
    else:
        if (cardinalities[0] == '1' and (cardinalities[1].find('*'))!=-1):
            keys = classobj[name]['attributs']
            keys_toadd = get_primary_keys_list(classobj, child)+keys
            classobj = add_fk_to_att_list(keys_toadd, classobj, parent)
            ##print(keys_toadd)
            return classobj
        elif (cardinalities[1] == '1' and (cardinalities[0].find('*'))!=-1):
            keys = classobj[name]['attributs']
            keys_toadd = get_primary_keys_list(classobj, parent)+keys
            classobj = add_fk_to_att_list(keys_toadd, classobj, child)
            ##print(classobj)
            return classobj
        elif ((cardinalities[0].find('*'))!=-1 and (cardinalities[1].find('*'))!=-1):
            parent_pk_key=get_primary_keys_list(classobj, parent)
            child_pk_key=get_primary_keys_list(classobj, child)
            keys=parent_pk_key+child_pk_key
            classobj = add_fk_to_att_list(keys, classobj, name)
            ##print(classobj)      
            return classobj
    
