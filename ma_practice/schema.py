from marshmallow import Schema, fields, validate

class LearnerSchema(Schema):
    uid = fields.Int()
    name = fields.Str(
        required=True, 
        error_messages={
            "required": {
                "message": "Field 'name' is required", 
                "code": 400
            }
        }
    )
    final_test = fields.Bool(
        required=True, 
        error_messages={
            'required': 'Final test is required'
        }
    )


class LearnerSchema(Schema):
    uid = fields.Integer()
    name = fields.Str(
        required=True,
        error_messages={
            'required': {
                'message': 'name is requided',
                'code': 400
            }
        },
        validate=[validate.Length(max=50)]
    )
    final_test = fields.Boolean(required=True, error_messages={
        'required': 'final_test is required'})
