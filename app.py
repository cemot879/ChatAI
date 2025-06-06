from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

# Konfigurasi client baru (v1.0+)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are ChatAI, a helpful assistant."},
                {"role": "user", "content": incoming_msg}
            ]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = "Maaf, terjadi kesalahan:\n\n" + str(e)

    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
