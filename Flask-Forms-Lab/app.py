from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


accounts = {
	'anty':'123',
	'zain':'mahmoud',
	'mahmoud':'zain',
	'farid':'meet2020',
	'lour' : "mahmoud's cat is ugly",
	'1' : '1'
}
facebook_friends=["Jhon","Andrew","Lily", "Preston", "Emily", "Tia"]


@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username_in = request.form['username']
		password_in = request.form['password']
		for account in accounts:
			print(account)
			if (account == username_in and accounts[account] == password_in):
				return redirect(url_for('home'))
		return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', facebook_friends = facebook_friends)


@app.route('/friend_exists/<string:name>', methods = ["GET", "POST"])
def friend_exists(name):
	for friend in facebook_friends:
		if name == friend:
			return render_template('friend_exists.html', friend = True)
		else:
			return render_template('friend_exists.html', friend = False)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)