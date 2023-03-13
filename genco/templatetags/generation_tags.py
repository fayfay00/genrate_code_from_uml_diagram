from django import template

register = template.Library()

@register.simple_tag
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


@register.simple_tag
def Foreign_key(key_name,table_name):
    return f"FOREIGN KEY ({key_name}) REFERENCES {table_name}({key_name})"

@register.simple_tag
def primary_key(primary_key_object, class_id):
    id=str(class_id)
    pks=primary_key_object[id]["primary_keys"]
    if len(pks)==0:
        fks=primary_key_object[id]["foreign_keys"]
        result=','.join(fks)
    else:
        result=','.join(pks)
    return f"PRIMARY KEY({result})"
    