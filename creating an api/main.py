from flask import Flask, jsonify

app = Flask(__name__)

items = [
    {'id': 1, 'name': 'First item'},
    {'id': 2, 'name': 'Second item'},
    {'id': 3, 'name': 'Third item'},
]


@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)


@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_items_by_id(item_id: int):
    item = next((item for item in items if item['id'] == item_id), None)

    if item is None:
        return jsonify({'message': 'Item not found'}), 404

    return jsonify(item)


if __name__ == '__main__':
    app.run(debug=True)
