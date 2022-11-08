# import json
#
#
# interns = {
#     "firstintern": "james",
#     "secondintern": "batul",
#     "thirdintern": "jessica"
#
# }
#
#
# with open("C:\\Users\\jess\\Documents\\school work\\hiit interns.json", "w") as amazingemma:
#     json.dump(interns, amazingemma)
#
# with open("C:\\Users\\jess\\Documents\\school work\\hiit interns.json","r") as emma:
#     maslaw = json.load(emma)
# print(maslaw)
#
#
# jess = json.dumps(interns)
# print(jess)

# class exercise
# import json
#
# jayy = {
#     "institution": "hiit",
#     "subject": "python",
#     "student": ["batul", "james", "jessica"]
# }
#
# with open("jayy.json", "w") as name:
#     json.dump(jayy.name)

import json

employees = '''
{
    "employees": [
        {
            "firstname": "jess",
            "lastname": "ibro"
        },
        {
            "firstname": "name",
            "lastname": "james"

        }
    ]
}
'''


data = json.loads(employees)
print(type(data))
print(data)


for head in data["employees"]:
    print(head["lastname"])