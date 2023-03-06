import os
from genco.regle_de_passage.generalization import add_fk_to_att_list ,get_primary_keys_list
from dotenv import load_dotenv
from genco.regle_de_passage.asociation_functions.oneone import ONEONE, ONEONEINV,ONEZEROONE,ZEROONEONE
from genco.regle_de_passage.asociation_functions.onestar import ONESTAR,STARONE
from genco.regle_de_passage.asociation_functions.starstar import STARSTAR

load_dotenv()
functions_list = os.environ.get('association_functions_list')

def Association(classobj, classes, cardinality, name):
        if cardinality in functions_list:
            
            strobj=str(classobj)
            if(cardinality!="STARSTAR"):
                if(cardinality != "ONESTAR" and cardinality != "STARONE"): 
                    classobj=eval(cardinality+"("+strobj+","+classes[0]+","+classes[1]+")")
                    #print("yes")
                    #print(functions_list)
                    return classobj
                else:
                    classobj=eval(cardinality+ "(" + strobj + "," + classes[0] + "," + classes[1] +","+ str(name) + ")")
                    #print("yes")
                    #print(functions_list)
                    return classobj
                    
            else:
                # classobj=eval(cardinality+ "(" + strobj + "," + classes[0] + "," + classes[1] +","+ str(name) + ")")
                classobj=STARSTAR(classobj,classes[0],classes[1],name)
                #print("yes")
                #print(functions_list)
                return classobj
                
        else:
            print("there is an error in cardinalities\n -404-function doesn't exist ")