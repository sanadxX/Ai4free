from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ AI Server is Online!"

@app.route("/ask", methods=["GET", "POST"])
def ask_ai():
    user_input = request.args.get("q")
    if not user_input:
        data = request.get_json(silent=True) or {}
        user_input = data.get("q")

    if not user_input:
        return jsonify({"error": "No question provided. Use ?q=... or JSON {'q': '...'}"}), 400

    try:
        # Import lazily to avoid crashing server on startup
        from ai4free import BLACKBOXAI

        ai = BLACKBOXAI(is_conversation=True)
        response = ai.chat(user_input)
        return jsonify({"status": "success", "answer": response})

    except ModuleNotFoundError as e:
        # This catches ai4free missing OR Helpingai_T2 missing
        return jsonify({
            "error": f"Missing module: {str(e)}",
            "hint": "ai4free package may be broken on this version or depends on non-pip module (e.g. Helpingai_T2)."
        }), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
