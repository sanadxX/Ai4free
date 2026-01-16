from flask import Flask, request, jsonify
from ai4free import BLACKBOXAI
import os

app = Flask(__name__)
@app.route('/')
def home():
    return " AI Server is Online!"

@app.route('/ask', methods=['GET', 'POST'])
def ask_ai():
    user_input = request.args.get('q') or request.json.get('q')
    
    if not user_input:
        return jsonify({"error": "No question provided. Use ?q=your_question"}), 400

    try:
        ai = BLACKBOXAI(is_conversation=True)
        response = ai.chat(user_input)
        
        return jsonify({
            "status": "success",
            "answer": response
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
