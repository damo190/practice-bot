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
    temp = request.values.get('temp')

    if int(temp) > 30:
        return "It's too hot!"
    else:
        return f'It is {temp} degrees today'
if __name__ == '__main__':
    # Start the web server!
    app.run()
