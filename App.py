from flask import Flask, request, render_template, jsonify
from openai import OpenAI

app = Flask(__name__)

# API Setup
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        # Call NVIDIA API
        completion = client.chat.completions.create(
            model="nvidia/llama-3.1-nemotron-70b-instruct",
            messages=[{"role": "user", "content": user_message}],
            temperature=0.5,
            max_tokens=1024
        )

        response = completion.choices[0].message.content
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=False)
