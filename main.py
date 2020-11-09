import csv
import requests
import pandas as pd

from flask import Flask, render_template  # request redirect, flash, url_for

app = Flask(__name__)


url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
s = pd.read_csv(url)

url2 = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
c = pd.read_csv(url2)


# Function to connect our home HTML file
@app.route('/')
def index():
    # CSV_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
    # req = requests.get(CSV_URL, 'covid_file/us-states.csv')
    #
    # with open('covid_file/us-states.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     for line in req.iter_lines():
    #         writer.writerow(line.decode('utf-8').split(','))

    return render_template('index.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


# Function to get a COVID-19 data file and display the contents of it
@app.route('/covid')
def covid():
    # with open('covid_file/us-counties.csv', 'r') as covidfile:
    #     csv_read = csv.DictReader(covidfile)
    #     # print(csv_read)
    #     covid_list = []
    #
    #     # For loop to get the last 7 days of Covid Data
    #     for j in list(reversed(list(csv_read)))[0:7]:
    #         # print(j)
    #         date = j['date']
    #         cases = j['cases']
    #         deaths = j['deaths']
    #         covid_list.append({'date': date, 'cases': cases, 'deaths': deaths})
    #
    #     # Function to compute and display the COVID-19 death rate
    #     def compute_csv():
    #         data = []
    #         with open('covid_file/us-counties.csv', 'r') as covidfile:
    #             csv_read = csv.DictReader(covidfile)
    #             for i in list(reversed(list(csv_read))):
    #                 # print(i)
    #                 cases = i['cases']
    #                 deaths = i['deaths']
    #                 rate = int(deaths) / int(cases)
    #                 data.append({'cases': cases, 'deaths': deaths, 'rate': rate})
    #                 return data

    return render_template('covid.html')  # , l=covid_list, k=compute_csv())


app.secret_key = 'some_secret_key_27'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
