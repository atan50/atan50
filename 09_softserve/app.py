"""
Amanda Tan
SoftDev
K09 -- Reading CSV Files
2024-09-19
time spent: .8
"""

from flask import Flask
import csv
import random

app = Flask(__name__)

def fileParser(file):			#reads csv
    with open(file, newline='') as csvfile:
        csvFile = csv.reader(csvfile, delimiter='\n')
        data = []
        for line in csvFile:
            data.append(line)
    return data

def splitHeaders(dataSet):		#converts data to dictionary
    dictValues = {}
    for data in dataSet:
        for string in data:
            for count, letter in enumerate(string[:len(string)-1]):
                if letter == ',' and string[count+1].isnumeric():
                    dictValues[string[:count]] = float(string[count+1:])
    return dictValues

def randomizeJob(dict):			#randomizes job, weighted
    randVal = random.uniform(0,99.8)
    for data in dict:
        randVal -= dict[data]
        if(randVal <= 0):
            return data


@app.route("/")
def hello_world():
    allData = fileParser("occupations.csv")
    headers = allData[0][0].split(",")
    dict = splitHeaders(allData[1:len(allData)])
    randJob = f"{headers[0]}: {randomizeJob(dict)}\n"
    jobList = f"<table><tr><th>{header[0]}</th></tr>"
    for job in dict:
        jobList += f"<tr><td>{job[0]}</td></tr>"
    return f"{randJob}{jobList}"

app.debug = True
app.run()