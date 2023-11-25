#!/usr/bin/env python3
from flask import Flask, render_template_string, request 

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
  user = request.args.get('user') or None

  template = '''
  <html><head><title>SSTI demo app</title><style>body {margin: 90px; background-image: url('{{url_for('static', filename='bg.jpg')}}');}</style></head><body>
  '''

  if user == None:
    template = template + '''
    <div>
    <h1 >Hacker Forum</h1>
    <form>
    <input name="user" style="border: 2px solid #C21010; padding: 10px; border-radius: 10px; margin-bottom: 25px;" value="Username"><br>
    <input type="submit" value="Log In" style="border: 0px; padding: 5px 20px ; color: #C21010;">
    </form>
    </div>
    '''.format(user)
  else:
    template = template + '''
    <h1 style="color: white"> Hi {}</h1>
    <p style="color: white">Welcome to the hacker forum, do you know about S*TI?</p>
    '''.format(user)
  
  return render_template_string(template)

if __name__ == "__main__":
  app.run(debug=False, host='0.0.0.0', port=8089)