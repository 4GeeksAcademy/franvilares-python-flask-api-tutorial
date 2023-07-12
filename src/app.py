from flask import Flask, jsonify
app = Flask(__name__)
from flask import request


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }, 
    { "label": "Sample Todo 1", "done": True }]

@app.route('/todos', methods=['GET'])
def otra():
    json_text = jsonify(todos)
    return json_text



@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    
    # Add the new task to the todos list
    todos.append(request_body)
    
    # Return the updated todos list as a JSON response
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position >= 0 and position < len(todos):
        del todos[position]  # Remove the task at the specified position
        return jsonify(todos)  # Return the updated todos list
    else:
        return jsonify({"error": "Invalid position"})
    
# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)