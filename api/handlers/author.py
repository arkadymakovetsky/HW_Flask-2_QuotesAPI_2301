from api import app, db, request, auth
from api.models.author import AuthorModel
from api.schemas.author import author_schema, authors_schema
from api.models.quote import QuoteModel


@app.get('/authors')
def get_authors():
    authors = AuthorModel.query.all()
    return authors_schema.dump(authors), 200


@app.get('/authors/<int:author_id>')
def get_author_by_id(author_id):
    author = AuthorModel.query.get(author_id)
    if author is None:
        return f"Author with id={author_id} not found", 404
    return author_schema.dump(author), 200


@app.post('/authors')
@auth.login_required
def create_author():
    author_data = request.json
    author = AuthorModel(**author_data)
    db.session.add(author)
    db.session.commit()
    return author_schema.dump(author), 201


@app.put('/authors/<int:author_id>')
@auth.login_required
def edit_author(author_id):
    author_data = request.json
    author = AuthorModel.query.get(author_id)
    if author is None:
        return {"Error": f"Author with id={author_id} not found"}, 404
    for key, value in author_data.items():
            setattr(author, key, value)
    db.session.commit()
    return author_schema.dump(author), 200


@app.delete('/authors/<int:author_id>')
@auth.login_required
def delete_author(author_id):
    author = AuthorModel.query.get(author_id)
    if author is None:
        return f"Author with id={author_id} not found", 404
    db.session.delete(author)
    db.session.commit()
    return {"message": f"Author with id={author_id} has deleted"}, 200
