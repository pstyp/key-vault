from flask import Flask
from flask_mail import Message, Mail
from os import getenv


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TSL'] = True
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = getenv('EMAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = ('I LOVE YOU', 'benhesketh@lovesyou.com')
mail = Mail(app)

@app.route('/')
def index():
    msg = Message('FLASK EMAIL APP',
                  recipients=['lauren100398@gmail.com'])
    msg.body = f'''ARE YOU GETTING THIS?, I'm sending this through python, cos im sik
                '''
    mail.send(msg)
    return ""





if __name__ == '__main__':
    app.run(debug=True)
