from flask import Flask
	
def create_app():
	app = Flask(__name__)

	@app.route('/')
	def kittens():
		return """
		<h1><font color = "blue">Hello, World!</font></h1>
		<br>
		<img src = "https://trupanion.com/-/media/trupanion/images/testimonials/cupcake-testimonials.jpg?h=260&la=en&w=264&hash=FA027D857DE3853BA38F1DBD0EB5B862C91AD451", alt= "kitten">

		"""

	@app.route('/hello')
	def hello_world():
		return '<h1><b><font color = "red">Hello, World!</font></b></h1>'

	return app
