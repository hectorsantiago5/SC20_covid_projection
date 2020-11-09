import csv
import pandas as pd

from flask import Flask, render_template, request  # redirect, flash, url_for

app = Flask(__name__)

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
s = pd.read_csv(url)

url2 = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
c = pd.read_csv(url2)

url3 = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
us = pd.read_csv(url2)


# Function to connect our home HTML file
@app.route('/')
def index():
    return render_template('index.html')


# Function to connect our about us HTML file
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


# Function to get a COVID-19 data file and display the contents of it
@app.route('/covid', methods=['POST', 'GET'])
def covid():
    with open('us.csv', 'r') as covidfile:
        csv_read = csv.DictReader(covidfile)
        #print(csv_read)
        covid_list = []

        # For loop to get the last 7 days of Covid Data
        for j in list(reversed(list(csv_read)))[0:7]:
            #print(j)
            date = j['date']
            cases = j['cases']
            deaths = j['deaths']
            covid_list.append({'date': date, 'cases': cases, 'deaths': deaths})

    return render_template('covid.html', covid_list=covid_list)


app.secret_key = 'some_secret_key_27'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

# df = pd.read_csv('us-counties.csv', dtype={'date': str,'county':str, 'state': str, 'fips': str, 'cases': int, 'death':int})
#
#     newdf=df[df.fips == '13121']
#     low_memory=False
#     print(newdf[-7:-1])
#     nnewdf = newdf[-7:-1]
#     date = nnewdf['date']
#     cases = nnewdf['cases']
#     deaths = nnewdf['deaths']
#     covid_list.append({'date': date, 'cases': cases, 'deaths': deaths})
#     for i in covid_list:
#         print(i['date'])

