# Import flask
from flask import Flask, request

# Create your app (web server)
app = Flask(__name__)


# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# You can access demobot’s greet command via <your website>/greet
@app.route('/greet', methods=['GET', 'POST'])
def greet_person():
    # Get the value of the 'name' query parameter
    # request.values is a dictionary (cool!)
    name = request.values.get('text')
    # This bot says hi to every name it gets sent!
    return f'hi {name}!'

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    temp = request.values.get('text')

    if int(temp) > 20:
        return "🔥" * int(temp)
    elif int(temp) < 0:
        return "❄️" * (int(temp) * -1)
    else:
        return f'It is {temp} degrees today'

@app.route('/lockout', methods = ['GET', 'POST'])
def lockout():
    location = request.values.get('text')
    if location == None or location == " ":
        return "Where are you locked out?"
    else:
        return f'Sending Smerity to {location} to save you'


if __name__ == '__main__':
    # Start the web server!
    app.run()
