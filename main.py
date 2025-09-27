# app.py
from flask import Flask, request, jsonify

# Create a Flask web application instance
app = Flask(__name__)


data = {
    1:{"task":"Learn Python","done":False},
    2:{"task":"Bulid first REST API","done":False}
}

@app.route("/todos",methods=["GET"])
def get_todos():
    response =[]
    for key, value in data.items():
        temp = value
        temp["id"]= key
        response.append(temp)
    return response

@app.route("/todos/<int:id>",methods=["GET"])
def get_todo(id):
    if id in data:
        temp = data[id]
        temp["id"]= id
        return temp
    else:
        return {
            "error":"Todo not found"
        },404
    

@app.route("/todos",methods=["POST"])
def post_todos():
    requestdata = request.get_json()
    todo = {
        "task":requestdata["task"],
        "done":False
    }    
    data[len(data)+1] = todo
    todo["id"] = len(data)
    return todo,201


@app.route("/todos/<int:id>", methods=["PUT"])
def put_todos(id):
    requestdata = request.get_json()
    if id in data:
        temp = data[id]  # ✅ fixed line
        temp["task"] = requestdata.get("task", temp["task"])
        temp["done"] = requestdata.get("done", temp["done"])

        todo_with_id = temp.copy()
        todo_with_id["id"] = id

        return jsonify(todo_with_id), 200
    else:
        return jsonify({
            "error": "Todo not found"
        }), 404
    

@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_toddos(id): 
    data.pop(id, None)
    return {
        "message": "Todo deleted Successfully"
    }   

if __name__=="__main__":
    app.run(debug=True)