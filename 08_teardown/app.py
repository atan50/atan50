'''
Amanda Tan
Dancing Elmo
SoftDev
K08 -- Learnination Via Deconstruction
2024-09-20
time spent: .5

DISCO:
1. We discovered that whenever the linked server is accesssed/refreshed,
    "__main__
    127.0.0.1 - - [21/Sep/2024 14:39:47] "GET / HTTP/1.1" 200 -"
    will get printed to the terminal.
2. We cannot run inspect on the webpage in the browser.
3. The script cannot be run from inside Thonny.

QCC:
0. @app.route("/") reminds us of React in Javascript. They could have similar purposes.
1. 
2. 
3. 
4. 
5. 
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?			A:We have seen similar syntax in C#/Java in creating instances of classes.

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?		A: One point of reference of the '/', is that it represents the root directory.This resembles the home page, index.html in web development.
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print? 			A: It prints to the terminal/shell where the Flask server is running. It prints "_main_"
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?						A: It appears as the first line printed on "127.0.0.1:5000."We figured this out as we observed it present when we pressed the link.

app.run()                                # Q5: Where have you seen similar constructs in other languages?	A: We have seen similar constructs of 'app.run()' as methods accessed on an object to achieve a certain action in java, python and javascript.



