
import os

def SQL_code_generator(classobj,db_name):
    
    database_creation=f" \n\nCREATE DATABASE {db_name};\nUSE {db_name}; \n"
    comment="\n\n/*--------------------------------------------------------------------------*/ \n\n\n"
    sql_script=database_creation+comment
    for cls_id,cls_data in classobj.items():
        table_code=f"CREATE TABLE {cls_data['name']} ( "
        pk_key_number=test_pks(cls_data['attributs'])
        #print("pk key number is "+str(pk_key_number))
        for att in cls_data['attributs']:
            if (att['attribut_key_type']=="LOCAL_KEY"):
                var=Variable_data_types(att['attribut_type'],att['attribut_name'])+","
                table_code+=var
            elif (att['attribut_key_type']=="PRIMARY_KEY"):
                var=Variable_data_types(att['attribut_type'],att['attribut_name'])
                temp=str(Only_one_variable_key_types(data=att['attribut_key_type'],key_type=var))+','
                table_code+=temp
                #print(table_code)
                
                
            else:
                fk_class_id=att['table_id']
                #print(fk_class_id)
                pk_info=get_pk_info(classobj,fk_class_id,att['attribut_name'])
                #print(pk_info)
                var=Variable_data_types(pk_info,att['attribut_name'])
                #print(var)
                table_code+=var+','
                #print(table_code)
                temp=str(Only_one_variable_key_types(data=att['attribut_key_type'],foreign_key_in_table=att['attribut_name'], foreign_keys_table=att['table']))+','
                table_code+=temp
                #print(temp)

        table_code=table_code[:-1] +"); \n"
        table_code+=comment
        sql_script+=table_code
        print(classobj)
    desk=os.path.join(os.path.expanduser("~"), 'C:\\Users\\yassine\\OneDrive\\Bureau')
    filepath=os.path.join(desk,"script_sql_from_django.txt")
    with open(filepath,"w") as f:
        f.write(str(sql_script))

    f.close()

            
        

##################################################################################################

def Variable_data_types(case,name):
    Variables={
        "STRING":f"{name} VARCHAR(50)",
        "INT":f"{name} INT",
        "FLOAT":f"{name} FLOAT",
        "DOUBLE":f"{name} DOUBLE",
        "DATE":f"{name} DATE",
        "BOOLEAN":f"{name} BOOLEAN",
        "TEXT":f"{name} TEXT",
        "TIMESTAMP":f"{name} TIMESTAMP",    
    }
    return Variables.get(case,"STRING")

#########################################################################################################

def Only_one_variable_key_types(**kwargs):
    key_type=kwargs.get('key_type','Unknown')
    data=kwargs.get('data','Unknown')
    foreign_key_in_table=kwargs.get('foreign_key_in_table','Unknown')
    foreign_keys_table=kwargs.get('foreign_keys_table','Unknown')
    KEYS={
        "PRIMARY_KEY":f"{key_type} PRIMARY KEY",
        "FOREIGN_KEY":f"FOREIGN KEY ({foreign_key_in_table}) REFERENCES {foreign_keys_table} ({foreign_key_in_table})",
        "LOCAL_KEY":f"{key_type}",
    }
    return KEYS.get(data)

##############################################################################################################

def get_pk_info(classobj,id,att_name):
    one_class_att=classobj[id]["attributs"]
    #print(one_class_att)
    for dict in one_class_att:
        if dict['attribut_key_type']=="PRIMARY_KEY":
            return dict['attribut_type']

###############################################################################################################
def test_pks(att_list):
    pk=0
    for att in att_list:
        if att['attribut_key_type']=="PRIMARY_KEY":
            pk=pk+1
    return pk
