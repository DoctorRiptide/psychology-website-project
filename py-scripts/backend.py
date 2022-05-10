from flask import flask

app = Flask(__name__)

@app.route('/')
def home():
	app.run(
		host = '127.0.0.1',
		port = '8080',
		debug=True
)


@app.route('/contact-script', methods=['POST'])  # Allow info to be posted into the backend
def contact_email():
	print('hey bby')

