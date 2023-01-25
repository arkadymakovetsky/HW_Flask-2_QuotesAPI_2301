from api import ma
from api.models.quote import QuoteModel
from api.schemas.author import AuthorSchema

class QuoteSchema(ma.SQLAlchemySchema):
   class Meta:
       model = QuoteModel

   id = ma.auto_field()
   text = ma.auto_field()
   rating = ma.auto_field()
   author = ma.Nested(AuthorSchema())

# одиночная
quote_schema = QuoteSchema()
# множестверрая
quotes_schema = QuoteSchema(many=True)
