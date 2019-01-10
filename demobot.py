# Import flask
from flask import Flask, request
import re

# Create your app (web server)
app = Flask(__name__)
b_user_states = {}
b_user_order = {}

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
    if location == None or location == " " or location == "":
        return "Where are you locked out?"
    else:
        return f'Sending Smerity to {location} to save you'
@app.route('/burger', methods=['GET', 'POST'])
def burger():
    user_id = request.values.get('user_id')
    if user_id not in b_user_states:
        b_user_states[user_id] = "NO QUERY"
    if user_id == "NO QUERY":
        return "What would you like to order?"
    if "burger" in request.values.get('text'):
        b_user_states[user_id] = "BURGER TYPE REQ"
        m = re.search(r'(cheese|beef|chicken|original) burger',request.values.get('text'))
        if m:
            if user_id in b_user_order:
                b_user_order[user_id][0] = m.group(1)
                b_user_states[user_id] = "ORDER COMPLETE"
            else:
                b_user_order[user_id] = [m.group(1)]
                b_user_states[user_id] = "DRINK ORDER REQ"
    if "drink" in request.values.get('text'):
        b_user_states[user_id] = "DRINK TYPE REQ"
        m = re.search(r'(water|sprite|fanta|coke) drink',request.values.get('text'))
        if m:
            if user_id in b_user_order:
                b_user_order[user_id].append(m.group(1))
                b_user_states[user_id] = "ORDER COMPLETE"
            else:
                b_user_order[user_id] = [None, m.group(1)]
                b_user_states[user_id] = "BURGER ORDER REQ"
    if b_user_states[user_id] == "BURGER TYPE REQ":
        return "Please specify a type for the burger; cheese, beef, chicken or original"
    if b_user_states[user_id] == "DRINK TYPE REQ":
        return "Please specify a type for the drink; water, coke, fanta or sprite"
    if b_user_states[user_id] == "DRINK ORDER REQ":
        return "Burger order complete, now please order a drink"
    if b_user_states[user_id] == "BURGER ORDER REQ":
        return "Drink order complete, now please order a drink"
    if b_user_states[user_id] == "ORDER COMPLETE":
        order = f"You have ordered a {b_user_order[user_id][0]} burger and a {b_user_order[user_id][1]} drink."
        return order
    return input("Flask?")

if __name__ == '__main__':
    # Start the web server!
    app.run()
