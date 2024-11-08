from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/suggestions', methods=['GET'])
def get_suggestions():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Please provide a query parameter."}), 400

    # Using the unofficial Google Autocomplete API
    google_autocomplete_url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={query}"
    
    try:
        response = requests.get(google_autocomplete_url)
        response.raise_for_status()
        suggestions = response.json()[1]  # Parse the suggestions list from JSON
        
        return jsonify({"query": query, "suggestions": suggestions}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

# Example url
# http://127.0.0.1:5000/suggestions?query=Pk