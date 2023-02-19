from genco.regle_de_passage.generalization import add_fk_to_att_list ,get_primary_keys_list



def Composition(classobj,parent,childs):
    
        foreign_key = get_primary_keys_list(classobj,parent)
        
        for child in childs:
                child=str(child)
                classobj=add_fk_to_att_list(foreign_key,classobj,child)
                #print(foreign_key)
        return classobj