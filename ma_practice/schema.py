from marshmallow import Schema, fields

class LearnerSchema(Schema):
    uid = fields.Int()
    name = fields.Str(required=True, error_messages={"required": {"message": "Field 'name' is required", "code": 400}})
    final_test = fields.Bool(required=True, error_messages={'required': 'Final test is required'})
