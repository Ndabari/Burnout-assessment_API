from flask import Flask
from test_view import bp_views

app = Flask(__name__)

app.register_blueprint(bp_views)

if __name__ == '__main__':
    app.run(debug=True)