from flask import Flask
from src.user_api import users_blueprint

app = Flask(__name__)
app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
