###############################
from genco.regle_de_passage.generalization import add_fk_to_att_list ,get_primary_keys_list


def Association(classobj, classes, cardinalities):
        child = classes[0]
        parent =classes[1]
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
