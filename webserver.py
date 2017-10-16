"""
webserver.py

File that is the central location of code for your webserver.
"""
import requests
import os
from os import environ
import json



from flask import Flask, render_template, request

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")


user = environ['INFO253_MAILGUN_USER']
pw = environ['INFO253_MAILGUN_PASSWORD']
from_email = environ['INFO253_MAILGUN_FROM_EMAIL']
to_email = environ['INFO253_MAILGUN_TO_EMAIL']
domain = environ['INFO253_MAILGUN_DOMAIN']


@app.route('/p', methods=['POST'])
def post():
	data = json.loads(request.data.decode('ascii'))
	r = requests.post(
		"https://api.mailgun.net/v3/"+domain+"/messages",
		auth = (user, pw),
		data = {"from": data['name'] + " " + from_email,
		'to': to_email,
		'subject': data['subject'],
		'text': data['msg']})
	return(' ', 204)

# @app.route('/contact', methods=['POST'])
# def send_email():
# 	message = request.form.get("message")
# 	notifications = []
# 	data = {
# 		'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
# 		'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
# 		'subject': "You just was sent a message",
# 		'text': message,
# 		}
# 	auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

# 	r = requests.post(
# 		'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
# 		auth=auth,
# 		data=data)
# 	if r.status_code == requests.codes.ok:
# 		notifications.append("Your email was sent")
# 	else:
# 		notifications.append("You email was not sent. Please try again later")
# 	return render_template("contact.html", notifications=notifications)



@app.route('/')
def hello_world():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"
   
@app.route('/index')
def hello_index():
    return render_template("index.html") 

@app.route('/about')
def hello_about():
	return render_template("about.html")



@app.route('/contact')
def hello_contact():
	return render_template("contact.html")



@app.route('/blog/8-experiments-in-motivation')
def hello_experiments():
	return render_template("/blog/8-experiments-in-motivation.html")



@app.route('/blog/a-mindful-shift-of-focus')
def hello_mindful():
	return render_template("/blog/a-mindful-shift-of-focus.html")



@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def hello_develop():
	return render_template("/blog/how-to-develop-an-awesome-sense-of-direction.html")




@app.route('/blog/training-to-be-a-good-writer')
def hello_training():
	return render_template("/blog/training-to-be-a-good-writer.html")



@app.route('/blog/what-productivity-systems-wont-solve')
def hello_productivity():
	return render_template("/blog/what-productivity-systems-wont-solve.html")




