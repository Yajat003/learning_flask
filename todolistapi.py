from flask import Flask, jsonify, request
# - Flask provides 'jsonify' to handle converting native dictionaries or lists directly into clean JSON output.

app = Flask(__name__)

items = [
    {"id":1, "name":"Item 1", "description":"This is Item 1"},
    {"id":2, "name":"Item 2", "description":"This is Item 2"},
]


@app.route('/')
def home():
    return "Welcome to a Basic To Do List\n as i you gon really complete all the tasks huh!"
 
# Get all the tasks/items
@app.route('/items', methods = ["GET"])
def get_items():
    return jsonify(items)

# Get a specific task/item by id
@app.route('/items/<int:item_id>', methods = ["GET"])
def get_item(item_id):
    """    
    1. We filter the array to compare whether the entry ID matches the requested integer ID
    2. Using Python's built-in 'next()' function targets the matching element inside the loop
    3. Passing 'None' as the fallback parameter tells 'next(  )' what to return if no matches are found
    """
    item = next((item for item in items if item["id"] == item_id), None)

    # Error checking, return a specific JSON formatted error if an invalid ID is requested
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

# Create a new task/item
@app.route('/items', methods = ["POST"])
def create_item():
    """
    1. 'request.json' reads incoming body payloads
    2. This validation checks if the request format is valid JSON & ensures the required 'name' key exists
    """
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    
    """
    ID generation on the go    
    1. To safely increment task tracking we fetch the final element using python slice index 'items[-1]'
    2. We take that last entry's ID and increment it by +1 if items are present or otherwise fallback to 1
    """
    new_item={
        "id":items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "description": request.json["description"] 
    }
    items.append(new_item)
    return jsonify(new_item)

# Update/put and existing item
@app.route('/items/<int:item_id>', methods = ["PUT"])
def update_item(item_id):
    """
    1. POST is strictly responsible for creating a brand-new task
    2. PUT is specifically designed to target and update details on an already existing item
    """
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item is not found"})
    
    # Overwrites old names/descriptions completely with updated values passed via JSON payload
    item["name"] = request.json.get("name", item["name"])
    item["description"] = request.json.get("description", item["description"])

    return jsonify(item)


# Deleting the tas/item
@app.route('/items/<int:item_id>', methods = ["DELETE"])
def delete_item(item_id):
    """
    1. Used the 'global' keyword to explicitly modify our initial list reference
    2. List comprehension creates a filtered list keeping records only where IDs do NOT match the target parameter
    3. This effectively drops matching elements and completely overwrites the global tracking state
    """
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result":"Item deleted!"})
    


if __name__ == "__main__":
    app.run(debug = True)