from author import Author
from schema import AuthorSchema

author = Author(1, "Alex", "alex5@mail.ru")
author_schema = AuthorSchema()
result = author_schema.dump(author)
print(result)


authors = [
    Author(1, "Alex", "alex5@mail.ru"), 
    Author(2, "Tom",  "tom5@mail.ru"), 
    Author(3, "Bob",  "bob5@mail.ru")
]
authors_schema = AuthorSchema(many=True)
result = authors_schema.dump(authors)
print(result)
