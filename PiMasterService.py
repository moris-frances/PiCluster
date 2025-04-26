from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sendPrimes', methods=['POST'])
def post_integers():
    # Check if the request contains JSON data
    if request.is_json:
        try:
            # Attempt to retrieve the JSON data
            data = request.get_json()
            integers = data['primes']  # Assume the JSON array is keyed by 'integers'
            
            # Optionally, process the integers (example: summing them)
            result = sum(integers)

            # Return a JSON response with status code 200
            return jsonify({"success": True, "result": result}), 200
        except (KeyError, TypeError, ValueError):
            # Handle errors if integers are not properly sent
            return jsonify({"success": False, "message": "Invalid input"}), 400
    else:
        return jsonify({"success": False, "message": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)
