from flask import Flask, render_template
from dbhelper import *

app = Flask(__name__)
#app.config['SECRET KEY']= '696969BRANDON696969'

@app.route('/')
def home():
    return render_template("Home.html")
@app.route('/Custom')
def Custom():
    data = getall("customers")
    head:list= ['idno','lastname','firstname','course','level', 'actions']
    return render_template("index.html", student=data, header=head)
@app.route('/Item')
def Item():
    return render_template("Item.html")
if __name__=='__main__':
    
    app.run(debug=True)