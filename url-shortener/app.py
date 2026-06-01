from flask import Flask
from routes.auth_routes import auth_bp
from routes.url_routes import url_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(url_bp)

if __name__ == "__main__":
    app.run(debug=True)