from flask import Flask, jsonify, request
app = Flask(__name__)

# Sample data
books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'id': 3, 'title': '1984', 'author': 'George Orwell'}
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

# Get a single book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify({'book': book[0]})

# Create a new book
@app.route('/books_insert/<int:id>/title', methods=['POST'])
def create_book(id):
    data = request.get_json()
    book = {'id': data['id'], 'title': data['title'], 'author': data['author']}
    books.append(book)
    return jsonify({'book': book}), 201

# Update an existing book
@app.route('/books_update/<int:id>', methods=['PUT'])
def update_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        return jsonify({'message': 'Book not found'}), 404
    data = request.get_json()
    book[0]['title'] = data.get('title', book[0]['title'])
    book[0]['author'] = data.get('author', book[0]['author'])
    return jsonify({'book': book[0]})

# Delete an existing book
@app.route('/books_delete/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        return jsonify({'message': 'Book not found'}), 404
    books.remove(book[0])
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
