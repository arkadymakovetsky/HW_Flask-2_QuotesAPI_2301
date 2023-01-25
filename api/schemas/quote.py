from api import ma
from api.models.quote import QuoteModel
from api.schemas.author import AuthorSchema

class QuoteSchema(ma.SQLAlchemyAutoSchema): #ma.SQLAlchemySchema
    class Meta:
        model = QuoteModel

    # Добавить структуру Author
    author = ma.Nested(AuthorSchema())

# одиночная
quote_schema = QuoteSchema()
# множественная
quotes_schema = QuoteSchema(many=True)
