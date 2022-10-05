from flask import Flask #import the flask class

app = Flask(__name__)   #create instance of a flask app

@app.route("/") #python decorator which flask used used to connect url endpoints with code contained in functions
def hello_world(): #what should be executed (flask runs this)
    return "Hello World" #what user will see when load it

if __name__ == "__main__":
    app.debug = True
    app.run()