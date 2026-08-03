#Ebony
#Mod 4 Case Study: Python APIs

#creating a CRUD API for a book


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#DATABASE CONFIG
# Configures a local SQLite database named 'books.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#BOOK MODEL SETUP

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"{self.book_name} by {self.author}"

#creates the database file and tables
with app.app_context():
    db.create_all()


#CRUD API ENDPOINTS

#GET ALL BOOKS (Read)
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {
            'id': book.id, 
            'book_name': book.book_name, 
            'author': book.author, 
            'publisher': book.publisher
        }
        output.append(book_data)
    return jsonify({"books": output})

#GET A SINGLE BOOK BY ID (Read)
@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id, 
        'book_name': book.book_name, 
        'author': book.author, 
        'publisher': book.publisher
    })

#POST A NEW BOOK (Create)
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        book_name=data['book_name'], 
        author=data['author'], 
        publisher=data['publisher']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'id': new_book.id}), 201

#PUT/UPDATE AN EXISTING BOOK BY ID (Update)
@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.json
    
    # Updates field if provided in JSON body, otherwise keeps original value
    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)
    
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

#DELETE A BOOK BY ID (Delete)
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)

