from flask import Flask, render_template, request, jsonify
from chatbot import load_dataset, clean_input, get_response, DATASET_FILE, is_exit

app = Flask(__name__)
qa_pairs = load_dataset(DATASET_FILE)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_message = request.json.get("message", "")
    cleaned = clean_input(user_message)

    if is_exit(cleaned):
        reply = "Goodbye! Feel free to come back if you have more questions."
    else:
        reply = get_response(cleaned, qa_pairs)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)