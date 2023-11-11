#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python311\python.exe
from flask import Flask, url_for,render_template, jsonify,request
app = Flask(__name__)
qrimg = None
check = False

@app.route('/',methods =["GET","POST"])
def generator():
    check= False
    return render_template('generator.html',qrimg= qrimg,check=check)
@app.route('/Generator/Qrcode',methods =["GET","POST"])
def check():
    check =True
    
    qrdetail = None
    if request.method == "POST":
        qrdetail = request.form.get("qrdetail")
    import qr_api as api
    qrimg= api.Creator.qrcreator(qrdetail)
    return render_template('generator.html',qrimg= qrimg,check=check)

#app.run(debug=True)
