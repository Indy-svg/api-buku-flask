from flask import Flask, request, jsonify

app = Flask(__name__)
books = [
    {"id": 1, "title": "Rumah Untuk Alie", "author": "Lenn Liu", "year": 2024, "stock": 150},
    {"id": 2, "title": "Galaksi", "author": "Poppi Pertiwi", "year": 2022, "stock": 75}
]

@app.route('/api/v1/books', methods=['GET'])
def get_all_books():
    return jsonify({
        "status": "success",
        "total": len(books),
        "data": books
    }), 200

@app.route('/api/v1/books', methods=['POST'])
def create_book():
    # Validasi 1: Content-Type harus JSON
    if not request.is_json:
        return jsonify({
            "status": "error",
            "message": "Payload harus berformat application/json"
        }), 400

    data = request.get_json()

    # Validasi 2: semua field wajib ada
    required = ["title", "author", "year", "stock"]
    for field in required:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": f"Field '{field}' wajib diisi"
            }), 400

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"],
        "year": data["year"],
        "stock": data["stock"]
    }
    books.append(new_book)

    return jsonify({
        "status": "success",
        "message": "Buku berhasil ditambahkan",
        "data": new_book
    }), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)