from learner import Learner
from schema import LearnerSchema


learner = Learner(name='Vlad', uid=10, olympic=True)
leaner_schema = LearnerSchema()
result = leaner_schema.dump(learner)
print(result)


learners = [
    Learner(name='Vlad', uid=10, olympic=True), 
    Learner(name='Arkady', uid=11, olympic=False), 
    Learner(name='Max', uid=12, olympic=True)
]
learners_schema = LearnerSchema(many=True)
result = learners_schema.dump(learners)
print(result)

