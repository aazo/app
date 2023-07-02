from flask import Flask , redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
        return "Soon..."

@app.route('instagram')
def ref_to_instagram():
    return redirect("https://www.instagram.com/u.ryy/",code=302)










if __name__ == "__main__":
        app.run()