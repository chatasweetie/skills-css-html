from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def application():
	"""This is the home page that contains the application form"""

	return render_template("application-form.html")


@app.route("/application-submit")
def submit():
	"""This is the 'action' of submitting the appliation and showing a page with info"""
	namefirst = request.args.get("firstname")
	namelast = request.args.get("lastname")
	salary = request.args.get("salaryrequirments")
	position = request.args.get("job-position")

	html= render_template("application-submit.html", namefirst=namefirst, namelast=namelast, 
		                    							salary=salary, position=position)
	return html

if __name__ == "__main__":
	app.run(debug=True)

