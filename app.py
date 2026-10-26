import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

# Create the Flask application instance.
app = Flask(__name__)


# Display the home page and log each request to the index route.
@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')


# Serve the favicon from the static directory.
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# Handle the hello form submission and show a personalized greeting.
@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')

    # If a name was provided, render the greeting page with that value.
    if name:
        print('Request for hello page received with name=%s' % name)
        return render_template('hello.html', name=name)
    else:
        # If the form is empty, send the user back to the home page.
        print('Request for hello page received with no name or blank name -- redirecting')
        return redirect(url_for('index'))


# Run the app when this script is executed directly.
if __name__ == '__main__':
    app.run()
