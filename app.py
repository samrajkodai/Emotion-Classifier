from re import template
from flask import Flask,render_template,url_for,request
import os
from prediction_service import predictions


webapp_root="webapp"
static_dir=os.path.join(webapp_root,"static")
template_dir=os.path.join(webapp_root,"templates")

app=Flask(__name__,static_folder=static_dir,template_folder=template_dir)

@app.route("/")


def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if request.form['new_freq']!="":
            data=request.get_data()
            print("data",request.form['new_freq'])
            return predictions.predict(request.form['new_freq'])
        else:
            return "empty text detected"
    
    else:
        return "server error"

        
if __name__=="__main__":
    app.run(host="127.0.0.1",port=9090,debug=True)