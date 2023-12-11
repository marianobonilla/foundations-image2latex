from flask import Blueprint, request, jsonify
from ..services.pix2tex_service import process_image

api = Blueprint('api', __name__)


@api.route('/process_image', methods=['POST'])
def process_image_route():
    if 'image' not in request.files:
        return jsonify({"error": "No image part}"}), 400
    file = request.files['image']
    # add more validations as needed (e.g., file type, size)
    try:
        latex = process_image(file)
        return jsonify({"latex": latex})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
