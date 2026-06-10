import os
from flask import Flask
from routes.file_routes import file_bp
from config import UPLOAD_FOLDER

app = Flask(__name__)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.register_blueprint(file_bp)

if __name__ == "__main__":
    app.run(debug=True)