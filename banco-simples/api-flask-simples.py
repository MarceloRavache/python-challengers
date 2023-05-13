from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota GET
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello, World!'}
    return jsonify(data)

# Rota POST
@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)