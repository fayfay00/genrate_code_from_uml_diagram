{% load generation_tags %}
CREATE DATABASE {{db_name}};
USE {{db_name}};
{%for cls_id,cls_data in classes.items%}/*code de creation de la table {{cls_data.name}}*/
CREATE TABLE  {{cls_data.name}}(

    {%for att in cls_data.attributs%}{% Variable_data_types att.attribut_type att.attribut_name %},
    {%endfor%}
    {%for att in cls_data.attributs%}{%if att.attribut_key_type == "FOREIGN_KEY"%}
    {% Foreign_key att.attribut_name att.table %},{% endif %}{%endfor%}
    {%primary_key  pk_fk cls_id %}
);
{% endfor %}


