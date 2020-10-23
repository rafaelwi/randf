from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)

import uuid
import imp
import rnote_for_webapp as rnote

# Displays the homepage
# Page has to go into templates regardless of whether it actually uses the template features or not
@app.route('/')
def index():
    return render_template('index.html')

# Displays the pdf
# TODO: Accept an id to display the correct file to the correct user
@app.route('/out')
def peedeeeff():
    return send_from_directory('', 'out.pdf')

# Test route
@app.route('/hello')
def hello():
    return 'Hello world!'

# This is how you'd use a template with an input from the url
# Could be useful for displaying pdf?
@app.route('/user/<string:username>')
def user(username):
    return 'User {}'.format(username)

@app.route('/render', methods=['POST'])
def render():
    # Generate a new UUID for the file and save file
    filename = str(uuid.uuid4()) + '.temp'
    print('Filename to save to: {}'.format(filename))
    with open('temp/' + filename, 'w') as f: f.write(request.form['code'])
    #TODO: Add paramters for filename and/or the text and an output name
    #rnote.run()
    return index()

# This is how you do error handling
# We need to pass in the error parameter in regardless
# This part can stay, we just need to modify error.html
# Look into wekzeug for error codes for insufficient storage
@app.errorhandler(404)
def error_404(error):
    return render_template('error.html'), 404

# Consider using user cookies or sessions to store things? Maybe that's too naughty

