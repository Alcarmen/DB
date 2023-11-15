from flask import Flask, render_template,request,url_for,redirect
from dbhelper import *

app = Flask(__name__)
#app.config['SECRET KEY']= '696969BRANDON696969'

@app.route('/')
def home():
    return render_template("Home.html")
    
@app.route('/Custom')
def Custom():
    data = getall("customers")
    head:list= ['C_id','C_name','c_email','c_address','Active', 'actions']
  
    return render_template("index.html", student=data, header=head)
    
@app.route('/Item')
def Item():
    it= getall("items")
    head:list= ['id','ISBN','Title','Author','Genre', 'Price','I_Type', 'Action']
    return render_template("itemindex.html",item=it, header=head)
 
@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        c_id,c_name,c_email,c_address=dict(request.form).values()
        addrecord('customers', c_id=c_id, c_name=c_name, c_email=c_email, c_address=c_address)
    return render_template("Create.html")
if __name__=='__main__':
    
    app.run(debug=True)