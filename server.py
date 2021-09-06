from flask import Flask, render_template, url_for, send_from_directory, request, redirect
import os
import csv
from pathlib import Path

app = Flask(__name__)

print(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'scon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def about(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode = 'a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/Thanks.html')
    else:
        return "something went wrong"
