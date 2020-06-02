import json 
import dicttoxml
x = '{ "Name" : "Tony Stark", "Age" : 48, "Height" : 180, "Education" : "Masters of Information Techonology", "Occupation": "Engineer", "Hobbies" : ["saving earth","mentor spiderman","beat Thanos"], "EMP ID" : "001" }'

y = json.loads(x)
z = dicttoxml.dicttoxml(y,attr_type=False)
print(z)