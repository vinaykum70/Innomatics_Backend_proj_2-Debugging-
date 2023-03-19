from flask import Flask , render_template , redirect ,request , session

from flask_session import Session

app = Flask(__name__)
app.secret_key="vinay"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []


#####################################################

@app.route('/', methods=['GET', 'POST'])
def add_note():
    if not session.get("name"):
        return redirect("/login")
    
    else:
        note = request.form.get('note')
        notes.append(note)

    return render_template('index.html' , notes=notes)
    
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

@app.route('/logout')
def logout():
     if 'name' in session:  
        session.pop('name',None)  
        #session["name"] = None
        return redirect("/")


######################################################



if __name__=='__main__':
    app.run(debug=True)