from flask import Flask, request

from model.email import EmailSchema
from service.EmailService import send_email

app = Flask(__name__)


@app.route('/api/v1/email', methods=['POST'])
def post_email():
    email = EmailSchema().load(request.get_json())
    send_email(email)
    return "", 204


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8081)
