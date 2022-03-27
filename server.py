from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "guessing game"

import random

@app.route('/')
def index():
    color = "rgb(209, 209, 209)"
    session['number'] = random.randrange(1,100)
    return render_template("index.html", color=color)

@app.route('/guess', methods=['POST'])
def checkGuess():
    user_guess = int(request.form['user_guess'])
    random_number = session['number']
    if user_guess == random_number:
        message = "You guessed it!"
        color = "#3fd446"
        print(session['number'])
        return render_template("index.html", message=message, color=color)

    elif user_guess > random_number:
        message = "Too High"
        color = "red"
        print(session['number'])
        return render_template("index.html", message=message, color=color)
    else:
        message = "Too Low"
        color = "red"
        print(session['number'])
        return render_template("index.html", message=message, color=color)

@app.route('/play_again')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    