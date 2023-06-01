from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/api/data', methods=['GET'])
def get_data():
    # Fetch data
    data = {'name' : 'John', 'age': 30}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def create_data():
    # Payload Logic
    data = request.get_json()
    # Data logic
    
    response = {'message' : 'Data created successfully'}
    return jsonify(response), 201

@app.route('/api/data<int:data_id>', methods=['PUT'])
def update_data(data_id):
    # Updating data based on params
    data = request.get_json()
    # Data update logic
    response = {'message' : f'Data with id {data_id} updated successfully'}
    return jsonify(response)

@app.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    #Logic to delete
    # TODO: Input logic
    
    response = {'message': f'Data with id {data_id} deleted successfully'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
