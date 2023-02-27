import os
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

def Only_one_variable_key_types(**kwargs):
    key_type=kwargs.get('key_type','Unknown')
    data=kwargs.get('data','Unknown')
    foreign_key_name=kwargs.get('foreign_key_name','Unknown')
    foreign_keys_table=kwargs.get('foreign_keys_table','Unknown')
    KEYS={
        "PRIMARY_KEY":f"{key_type} PRIMARY KEY",
        "FOREIGN_KEY":f"FOREIGN KEY ({foreign_key_name}) REFERENCES {foreign_keys_table}({foreign_key_name})",
    }
    return KEYS.get(data)
def get_pk_info(classobj,id,att_name):
    one_class_att=classobj[id]["attributs"]
    #print(one_class_att)
    for dict in one_class_att:
        if dict['attribut_key_type']=="PRIMARY_KEY":
            return dict['attribut_type']









classobj={
    '1': {
        'id': '1',
        'name': 'commande',
        'attributs': [{
            'attribut_type': 'STRING',
            'attribut_name': 'pk_commande',
            'attribut_key_type': 'PRIMARY_KEY',
            'table': 'commande',
            'table_id': '1'
        }, {
            'attribut_type': 'STRING',
            'attribut_name': 'pk_commande2',
            'attribut_key_type': 'LOCAL_KEY'
        }, {
            'attribut_type': 'STRING',
            'attribut_name': 'pk_commande3',
            'attribut_key_type': 'LOCAL_KEY'
        }]
    },
    '2': {
        'id': '2',
        'name': 'facture',
        'attributs': [{
            'attribut_type': 'STRING',
            'attribut_name': 'pk_facture',
            'attribut_key_type': 'PRIMARY_KEY'
        }, {
            'attribut_type': 'STRING',
            'attribut_name': 'fayfay',
            'attribut_key_type': 'LOCAL_KEY'
        }, {
            'attribut_type': 'STRING',
            'attribut_name': 'pk_commande',
            'attribut_key_type': 'FOREIGN_KEY',
            'table': 'commande',
            'table_id': '1'
        }]
    }
}

database_creation=f"CREATE DATABASE {input('set your db name')};\n"
comment="/*--------------------------------------------------------------------------*/ \n"
sql_script=database_creation+comment
for cls_id,cls_data in classobj.items():
    table_code=f"CREATE TABLE {cls_data['name']} ( "
    for att in cls_data['attributs']:
        if (att['attribut_key_type']=="LOCAL_KEY"):
            var=Variable_data_types(att['attribut_type'],att['attribut_name'])+","
            table_code+=var
        elif not(att['attribut_key_type']=="FOREIGN_KEY"):
            var=Variable_data_types(att['attribut_type'],att['attribut_name'])
            temp=Only_one_variable_key_types(data=att['attribut_key_type'],key_type=var)+' ,'
            table_code+=temp
            #print(table_code)
        else:
            fk_class_id=att['table_id']
            #print(fk_class_id)
            pk_info=get_pk_info(classobj,fk_class_id,att['attribut_name'])
            #print(pk_info)
            var=Variable_data_types(pk_info,att['attribut_name'])
            table_code+=var+','
            temp=Only_one_variable_key_types(data=att['attribut_key_type'],foreign_key_name=att['attribut_name'], foreign_keys_table=att['table'])+' ,'
            #print(type(temp))
            table_code+=temp
            #print(temp)

    table_code=table_code[:-1] +"); \n"
    table_code+=comment
    sql_script+=table_code

desk=os.path.join(os.path.expanduser("~"), 'Desktop')
filepath=os.path.join(desk,"script_sql.txt")
with open(filepath,"w") as f:
    f.write(sql_script)

f.close()
