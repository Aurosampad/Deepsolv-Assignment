from flask import Flask, request, jsonify
from agent_scraper_two import scrape_data
from RAG_Implementation import query_brand_index, store_in_vector_store

app = Flask(__name__)

@app.route("/scrape-brand", methods=["GET"])
def scrape_brand():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400
    try:
        data = scrape_data(url)
        if not data:
            return jsonify({"error": "Website could not be scraped"}), 401
        store_in_vector_store(data)
        return jsonify({"status": "success", "message": "Data scraped and stored"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get-brand-context", methods=["GET"])
def get_brand_context():
    prompt = request.args.get("prompt")
    if not prompt:
        return jsonify({"error": "Missing 'prompt' parameter"}), 400
    try:
        response = query_brand_index(prompt)
        return jsonify({"brand_context": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
