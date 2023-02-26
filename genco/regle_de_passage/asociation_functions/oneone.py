from genco.regle_de_passage.generalization import add_fk_to_att_list ,get_primary_keys_list

def ONEONE(classobj,first_class,second_class):
            classobj=dict(classobj)
            foreign_keys = get_primary_keys_list(classobj, first_class)
            #print(second_class)
            # ajouter les clés étrangères à la liste des attributs de la classe fille
            classobj = add_fk_to_att_list(foreign_keys, classobj, str(second_class))
            print(classobj)
            return classobj
        
####################################################################
#if i want to send thet pks from the second class to the first

def ONEONEINV(classobj,first_class,second_class):
            classobj=dict(classobj)
            foreign_keys = get_primary_keys_list(classobj, second_class)
            print(foreign_keys)
            # ajouter les clés étrangères à la liste des attributs de la classe fille
            classobj = add_fk_to_att_list(foreign_keys, classobj, str(first_class))
            #print(classobj)
            return classobj
        
        
        
#########################################################################
### 1-----0.1

def ONEZEROONE(classobj,first_class,second_class):
            classobj=dict(classobj)
            foreign_keys = get_primary_keys_list(classobj, first_class)
            print(foreign_keys)
            # ajouter les clés étrangères à la liste des attributs de la classe fille
            classobj = add_fk_to_att_list(foreign_keys, classobj, str(second_class))
            #print(classobj)
            return classobj
        
###################################################################################
##### 0.1-------1

def ZEROONEONE(classobj,first_class,second_class):
            classobj=dict(classobj)
            foreign_keys = get_primary_keys_list(classobj, second_class)
            print(foreign_keys)
            # ajouter les clés étrangères à la liste des attributs de la classe fille
            classobj = add_fk_to_att_list(foreign_keys, classobj, str(first_class))
            #print(classobj)
            return classobj