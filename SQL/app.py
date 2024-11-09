from flask import Flask, render_template
from model.user_model import Bwp
app = Flask(__name__)
bwp = Bwp()
@app.route('/')
def hello_world():
    return bwp.user_signup()



# if __name__ == '__main__':
#     app.run(debug=True)