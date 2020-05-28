from flask import Flask, render_template
import requests
import json
from os import getenv


app = Flask(__name__)

api_key = getenv('ADDRESS_API_KEY')

@app.route('/<post_code>')
def address(post_code):
    params = {'api-key': api_key }
    address_list = requests.get('https://api.getAddress.io/find/'+post_code, params=params)

    addresses = address_list.json()['addresses']

    return render_template('index.html', addresses=addresses)



if __name__ == "__main__":
    app.run(debug=True)