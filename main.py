from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace these with your details
FULL_NAME = "john_doe"
DOB = "17091999"     # ddmmyyyy
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

def process_input(input_array):
    even_numbers = []
    odd_numbers = []
    alphabets = []
    special_characters = []
    total_sum = 0

    for item in input_array:
        # Check if item is a number
        if item.isdigit():
            num = int(item)
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
            total_sum += num

        # Check if item is alphabetic (letters only)
        elif item.isalpha():
            alphabets.append(item.upper())

        # Otherwise, treat it as special character
        else:
            special_characters.append(item)

    # Create concatenated string in reverse with alternating caps
    concat_str = "".join([c for c in "".join(alphabets)][::-1])
    alternating = ""
    for i, ch in enumerate(concat_str):
        if i % 2 == 0:
            alternating += ch.upper()
        else:
            alternating += ch.lower()

    return even_numbers, odd_numbers, alphabets, special_characters, str(total_sum), alternating


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "API is running. Use POST /bfhl"}), 200


@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.get_json()
        input_array = data.get("data", [])

        even_numbers, odd_numbers, alphabets, special_characters, total_sum, concat_str = process_input(input_array)

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": total_sum,
            "concat_string": concat_str
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    # Change port if needed
    app.run(host="0.0.0.0", port=8000, debug=True)
