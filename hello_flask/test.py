from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", name="Thomas")
	
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/form")
def form():
	return render_template('form.html')

@app.route("/about")
def about():
	return render_template('about.html')



app.run(debug=True)
