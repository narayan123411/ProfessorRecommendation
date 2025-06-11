from flask import Blueprint, render_template, request, jsonify
from app.services.recommender import recommend_professors

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    try:
        df = recommend_professors(data['description'], data['subjectCode'], data['challengeLevel'])
        return jsonify({'recommendations': df.to_dict(orient='records')})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
