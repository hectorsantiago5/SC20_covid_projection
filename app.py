# import base64
import csv
# import json
import os
# import urllib
from urllib.request import urlretrieve as retrieve
# from werkzeug.utils import secure_filename
# import requests
from google.cloud import storage

from flask import Flask, render_template, request# redirect, flash, url_for

app = Flask(__name__)

#CLOUD_STORAGE_BUCKET = os.environ['sc20-covid-prediction']

# UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Function to connect our home HTML file
# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


# Function to get a COVID-19 data file and display the contents of it
@app.route('/covid')
def import_covid_csv():
    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
    retrieve(url, 'covid_file/us-counties.csv')

    with open('covid_file/us-counties.csv', 'r') as covidfile:
        csv_read = csv.DictReader(covidfile)
        # print(csv_read)
        covid_list = []

        # For loop to get the last 7 days of Covid Data
        for j in list(reversed(list(csv_read)))[0:7]:
            # print(j)
            date = j['date']
            cases = j['cases']
            deaths = j['deaths']
            covid_list.append({'date': date, 'cases': cases, 'deaths': deaths})

        # Function to compute and display the COVID-19 death rate
        def compute_csv():
            data = []
            with open('covid_file/us-counties.csv', 'r') as covidfile:
                csv_read = csv.DictReader(covidfile)
                for i in list(reversed(list(csv_read))):
                    # print(i)
                    cases = i['cases']
                    deaths = i['deaths']
                    rate = int(deaths) / int(cases)
                    data.append({'cases': cases, 'deaths': deaths, 'rate': rate})
                    return data

        return render_template('index.html', l=covid_list, k=compute_csv())


# @app.route('/upload', methods=['POST'])
# def upload():
#     """Process the uploaded file and upload it to Google Cloud Storage."""
#     uploaded_file = request.files.get('../covid_file/us-counties.csv')
#
#     if not uploaded_file:
#         return 'No file uploaded.', 400
#
#     # Create a Cloud Storage client.
#     gcs = storage.Client()
#
#     # Get the bucket that the file will be uploaded to.
#     bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)
#
#     # Create a new blob and upload the file's content.
#     blob = bucket.blob(uploaded_file.filename)
#
#     blob.upload_from_string(
#         uploaded_file.read(),
#         content_type=uploaded_file.content_type
#     )
#
#     # The public URL can be used to directly access the uploaded file via HTTP.
#     return blob.public_url


# Function to only allow CSV files
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app.secret_key = 'some_secret_key_27'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
