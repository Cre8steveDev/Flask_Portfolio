from flask import Flask
from dotenv import load_dotenv
import os
from jokes_routes import joke_bp


load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("APPSECRET")

# Register Blueprint
app.register_blueprint(joke_bp)


if app.secret_key is None:
    print("Secret key is required for this application")
    exit()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
