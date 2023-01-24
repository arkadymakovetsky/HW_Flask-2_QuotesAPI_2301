from learner import Learner
from schema import LearnerSchema

json_data = """
{
   "name": "Ivan",
   "final_test": True
}
"""

schema = LearnerSchema()
result = schema.loads(json_data)
print(result)


json_data = """
[
   {
       "id": 1,
       "name": "Alex",
       "final_test": True
   },
   {
       "id": 2,
       "name": "Ivan",
       "final_test": False
   },
   {
       "id": 4,
       "name": "Tom",
       "final_test": True
   }
]
"""

schemas = LearnerSchema(many=True)
result = schemas.loads(json_data)
print(result)
