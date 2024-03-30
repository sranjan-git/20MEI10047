# Import necessary libraries
from flask import Flask, request, jsonify
import requests
from collections import deque
import time

# Initialize Flask app
app = Flask(__name__)

# Global variables
window_size = 10
numbers_queue = deque([], maxlen=window_size)

# Function to fetch numbers from the third-party server
def fetch_numbers(number_type):
    url = f"https://localhost:9876/{1,3,5,7}"
    try:
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.Timeout:
        return None
    except requests.exceptions.RequestException:
        return None

# Function to calculate average
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Endpoint to handle requests
@app.route('/numbers/<number_type>')
def process_number_request(number_type):
    global numbers_queue
    
    # Fetch numbers from third-party server
    numbers = fetch_numbers(number_type)

    # If numbers are fetched successfully, update the numbers queue
    if numbers:
        numbers_queue.extend(numbers)

    # Calculate average based on window size
    window_prev_state = list(numbers_queue)
    avg = calculate_average(numbers_queue)

    # Prepare response
    response_data = {
        "windowPrevState": window_prev_state,
        "windowCurrState": list(numbers_queue),
        "numbers": list(numbers) if numbers else [],
        "avg": avg
    }

    # Return response
    return jsonify(response_data)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)
