from flask import Flask, render_template, request, jsonify
import sys

app = Flask(__name__)


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

        # Extract the data
        selected_options = [data.get(f'selectedOption{i}') for i in range (1, option_num + 1)]
        location = data.get('location')

        # Validate data
        if not selected_options or not location:
            return jsonify({'error': 'Missing required data'}), 400

        lat = location.get('lat')
        lng = location.get('lng')

        if lat is None or lng is None:
            return jsonify({'error': 'Invalid location data'}), 400

        # Process the data (add your logic here)
        print(f"Received data:")
        [print(f"  Selected Option {i}: {selected_options[i]}") for i in range(0, option_num)]
        print(f"  Latitude: {lat}")
        print(f"  Longitude: {lng}")
        sys.stdout.flush()

        # Example: Do something with the data
        result = process_data(selected_options, lat, lng)

        # Return success response
        return jsonify({
            'message': 'Location processed successfully!',
            'data': {
                'option': selected_options[0],
                'coordinates': f"{lat}, {lng}",
                'result': result
            }
        }), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500


def process_data(option, lat, lng):
    """
    Process the location data based on selected option
    Add your custom logic here
    """
    # Example processing
    if option == 'option1':
        result = f"Processing option 1 for location ({lat}, {lng})"
    elif option == 'option2':
        result = f"Processing option 2 for location ({lat}, {lng})"
    elif option == 'option3':
        result = f"Processing option 3 for location ({lat}, {lng})"
    else:
        result = f"Processing {option} for location ({lat}, {lng})"

    # You can add:
    # - Database operations
    # - API calls to other services
    # - Calculations based on coordinates
    # - File operations
    # etc.

    return result


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)