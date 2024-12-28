from flask import Blueprint, request, jsonify
from app.helpers.query_handler import fetch_data
from app.helpers.text_generator import generate_response

bp = Blueprint('routes', __name__)

@bp.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')

    # Validate input
    if not user_question or len(user_question.strip()) == 0:
        return jsonify({"error": "Invalid input"}), 400

    # Query database
    data = fetch_data(user_question)
    if not data:
        return jsonify({"error": "No matching data found"}), 404

    # Generate response
    response_text = generate_response(data)
    return jsonify({"response": response_text})
