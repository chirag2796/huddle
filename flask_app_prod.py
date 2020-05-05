# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html')  # render a template

@app.route('/HA/login')
def ha_login():
    return render_template('/HA/login_new.html')  # render a template

@app.route('/HA/dashboard')
def ha_dashboard():
    return render_template('/HA/dashboard.html')  # render a template

@app.route('/HA/review')
def ha_review():
    return render_template('/HA/review.html')  # render a template

@app.route('/HA/allocate')
def ha_allocate():
    return render_template('/HA/allocate.html')  # render a template

@app.route('/HCP/login')
def hcp_login():
    return render_template('/HCP/login_new.html')  # render a template

@app.route('/HCP/dashboard')
def hcp_dashboard():
    return render_template('/HCP/dashboard.html')  # render a template

@app.route('/HCP/addpatient')
def hcp_addpatient():
    return render_template('/HCP/addpatient.html')  # render a template

@app.route('/HCP/transferpatient')
def hcp_transferpatient():
    return render_template('/HCP/transferpatient.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)