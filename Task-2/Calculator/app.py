from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for development purposes

# Dummy data for testing
data = {
    "windowPrevState": [],
    "windowCurrState": [],
    "numbers": [],
    "avg": 0.0
}

@app.route('/numbers/<numberid>', methods=['GET'])
def get_numbers(numberid):
    global data
    # Dummy logic to update data based on numberid (replace with your actual logic)
    if numberid == 'p':
        data["numbers"] = [2, 3, 5, 7, 11]
    elif numberid == 'f':
        data["numbers"] = [55, 89, 144, 233, 377]
    elif numberid == 'e':
        data["numbers"] = [2, 4, 6, 8, 10]
    elif numberid == 'r':
        data["numbers"] = [2, 19, 25, 7, 4]
    else:
        return jsonify({"error": "Invalid number ID"}), 400
    
    # Update window states and average (replace with your actual logic)
    data["windowPrevState"] = data["windowCurrState"]
    data["windowCurrState"] = data["numbers"]
    data["avg"] = sum(data["numbers"]) / len(data["numbers"])

    return jsonify(data)

if __name__ == "__main__":
    app.run(port=9876)
