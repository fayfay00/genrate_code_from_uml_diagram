



def SQL_code_generator(classobj,db_name,):
    
    database_creation=f"CREATE OR DROP DATABASE {input('set your db name')};\n"
    comment="/* \n --------------------------------------------------------------------------*/ \n"
    sql_script= database_creation + comment
    for cls_id,cls_data in classobj.items():
        table_code=f"CREATE OR DROP TABLE {cls_data['name']} ( "
        for att in cls_data['attributs']:
            if (att['attribut_key_type']=="LOCAL_KEY"):
                var=Variable_data_types(att['attribut_type'],att['attribut_name'])+","
                table_code+=var
            elif not(att['attribut_key_type']=="FOREIGN_KEY"):
                var=Variable_data_types(att['attribut_type'],att['attribut_name'])
                temp= str(Only_one_variable_key_types(data=att['attribut_key_type'],key_type=var)) +" ,"
                table_code+=temp
                #print(table_code)
            else:
                temp=str(Only_one_variable_key_types(data=att['attribut_key_type'],foreign_key_name=att['attribut_name'], foreign_keys_table=att['table']))+" ,"
                table_code+=temp
                #print(temp)

        table_code=table_code[:-2] +"); \n"
        table_code+=comment
        sql_script+=table_code
            
        


def Variable_data_types(case,name):
    Variables={
        "STRING":f"{name} VARCHAR(255)",
        "INT":f"{name} INT",
        "FLOAT":f"{name} FLOAT",
        "DOUBLE":f"{name} DOUBLE",
        "DATE":f"{name} DATE",
        "BOOLEAN":f"{name} BOOLEAN",
        "TEXT":f"{name} TEXT",
        "TIMESTAMP":f"{name} TIMESTAMP",    
    }
    return Variables.get(case,"STRING")

def Only_one_variable_key_types(**kwargs):
    key_type=kwargs.get('key_type','Unknown')
    data=kwargs.get('data','Unknown')
    foreign_key_in_table=kwargs.get('foreign_key_in_table','Unknown')
    foreign_key=kwargs.get('foreign_key','Unknown')
    foreign_keys_table=kwargs.get('foreign_keys_table','Unknown')
    KEYS={
        "PRIMARY_KEY":f"{key_type} PRIMARY KEY",
        "FOREIGN_KEY":f"FOREIGN KEY ({foreign_key_in_table}) REFERENCES {foreign_keys_table} ({foreign_key})",
        "LOCAL_KEY":f"{key_type}",
    }
    return KEYS.get(data)


