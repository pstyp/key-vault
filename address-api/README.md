# Address API Flask App

This app calls an address api, when you put a postcode in the url, it will return the houses at the post code.

### Example

http://localhost:5000/ty765fv would return the addresses with the post code TY76 5FV.

### Running

You will an API key from getAddress.io for this app to work.

These are the commands you will need to run the app.

```bash
export ADDRESS_API_KEY=[YOUR API KEY]
pip3 install flask
python3 app.py
```