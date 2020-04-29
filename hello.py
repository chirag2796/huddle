from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
import atexit
import os
import json

app = Flask(__name__)

db_name = 'mydb'
client = None
db = None

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif "CLOUDANT_URL" in os.environ:
    client = Cloudant(os.environ['CLOUDANT_USERNAME'], os.environ['CLOUDANT_PASSWORD'], url=os.environ['CLOUDANT_URL'], connect=True)
    db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

@app.route('/')
def home():
    return render_template('index.html')  # render a template

@app.route('/HA/login')
def ha_login():
    return render_template('/HA/login.html')  # render a template

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
    return render_template('/HCP/login.html')  # render a template

@app.route('/HCP/dashboard')
def hcp_dashboard():
    return render_template('/HCP/dashboard.html')  # render a template

@app.route('/HCP/addpatient')
def hcp_addpatient():
    return render_template('/HCP/addpatient.html')  # render a template

@app.route('/HCP/transferpatient')
def hcp_transferpatient():
    return render_template('/HCP/transferpatient.html')  # render a template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
