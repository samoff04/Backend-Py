from flask import Flask
from routes.auth_routes import auth_bp

print("Starting app...")
app = Flask(__name__)
print("Flask created")
app.register_blueprint(auth_bp)
print("Blueprint registered")

if __name__ == "__main__":
    print("Running server")
    app.run(debug=True)