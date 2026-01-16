import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"

from flask import Flask, render_template, request, jsonify
import sys
import fetch_weather
from model.build_model import RecommendationEngine
sys.stdout.reconfigure(line_buffering=True)

app = Flask(__name__)

recommendation_engine = RecommendationEngine()

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/process-location', methods=['POST'])
def process_location():
    """Handle location data from frontend"""
    option_num = 2
    try:
        # Get JSON data from request
        data = request.get_json()
        print(data)

        # Example: Do something with the data
        result = process_data(data)

        # Return success response
        return jsonify({
            'message': 'Location processed successfully!',
            'data': {
                'result': result
            }
        }), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/recommend', methods=['POST'])
def recommend():
    """Get product recommendations"""
    try:
        data = request.get_json()

        # Extract user preferences
        user_inputs = {
            'gender': data.get('gender', 'Men'),
            'articleType': data.get('articleType', 'Tshirts'),
            'season': data.get('season', 'Summer'),
            'usage': data.get('usage', 'Casual')
        }

        # Get recommendations using the class
        recommendations = recommendation_engine.predict(user_inputs)

        return jsonify({
            'recommendations': recommendations,
            'query': user_inputs
        }), 200

    except Exception as e:
        print(f"Error in recommendation: {str(e)}")
        return jsonify({'error': f'Recommendation error: {str(e)}'}), 500


def process_data(data: dict):
    """Process the location data based on selected option"""
    location = data['location']
    weather_data = fetch_weather.fetch_weather_data(location['lat'], location['lng'])
    #print(weather_data)
    season = fetch_weather.categorize_season(weather_data)

    # Example: Use weather to determine season/usage
    # You can integrate this with your recommendation system

    # Example recommendation based on weather
    user_inputs = {
        'gender': data['gender'],
        'articleType': 'Tshirts',
        'season': season,  # Could be derived from weather_data
        'usage': data['occasion'].capitalize()
    }

    # Use the class to get recommendations
    recommendations = recommendation_engine.predict(user_inputs)

    return recommendations

if __name__ == '__main__':
    recommendation_engine.load_model_and_index()
    app.run(debug=False, host='localhost', port=5000)
