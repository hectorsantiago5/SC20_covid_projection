import csv
import pandas as pd

from flask import Flask, render_template, request #redirect, flash, url_for


app = Flask(__name__)


url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
s = pd.read_csv(url)

url2 = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
c = pd.read_csv(url2)


# Function to connect our home HTML file
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


# @app.route('/covid',methods = ['POST', 'GET'])
# def covid():
#     if request.method == 'POST':
#       result = request.form
    
#     return render_template("covid.html", result=result)

# Function to get a COVID-19 data file and display the contents of it
@app.route('/covid',methods = ['POST', 'GET'])
def covid():
    with open('us.csv', 'r') as covidfile:
        csv_read = csv.DictReader(covidfile)
        # print(csv_read)
        covid_list = []
    #
    #     # For loop to get the last 7 days of Covid Data
        for j in list(reversed(list(csv_read)))[0:7]:
            # print(j)
            date = j['date']
            cases = j['cases']
            deaths = j['deaths']
            covid_list.append({'date': date, 'cases': cases, 'deaths': deaths})
        # print(covid_list)
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
# covid()
    return render_template('covid.html', covid_list=covid_list)  # , l=covid_list, k=compute_csv())


app.secret_key = 'some_secret_key_27'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
