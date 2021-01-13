from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello, Welcome to the application."


@app.route('/<name>')
def hello_world_name(name):
	return "Hello {}, Welcome to the application.".format(name)

if __name__ == '__main__':
	app.run(port=8080)
	print('Terminated')


