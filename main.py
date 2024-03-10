import random
from flask import Flask, render_template
from flask import request

app = Flask(__name__, template_folder='templates', static_folder='static')
messages = {0: "<h4>Tie</h4> Beginner's luck! Fight again and lose!",
            1: "<h4>You Win!</h4> Your victory will be short lived.",
            -1: "<h4>You Lose!</h4>You will not recover from this defeat!"}
options = ['Rock', 'Paper', 'Scissors']
results = [[0, -1, 1],
           [1, 0, -1],
           [-1, 1, 0]]
score = [0, 0, 0]
sound = {0: "sound_tie.mp3", 1: "sound_win.mp3", -1: "sound_lose.mp3"}


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        user_selection = request.form['selected'].rstrip()
        computer_selection = random.choice(options)
        result = results[options.index(user_selection)][options.index(computer_selection)]
        score[0] += 1 if result == 1 else 0
        score[1] += 1 if result == -1 else 0
        score[2] += 1 if result == 0 else 0
        color = "#7CB9E8" if result == 1 else ("lightgreen" if result == -1 else "")
        return render_template('index.html',
                               reset_visible='visible', win_color=color,
                               winner=messages[result],
                               user_select=user_selection + '.png',
                               ai_select=computer_selection + '.png',
                               scores=score, sound_file=sound[result])
    else:
        score[0] = 0
        score[1] = 0
        score[2] = 0
        instructions = "<span class='pc_only'><h3>" \
                       "To Play - Press:</h3>" \
                       "1 - Rock<br> 2 - Paper<br> 3 - Scissors<br>" \
		                   "Or</span> Click Button to Play"
        return render_template('index.html',
                               reset_visible='hidden', winner=instructions,
                               user_select='fist-smash.gif',
                               ai_select='fist-smash.gif',
                               scores=score, sound_file="sound_start.mp3")


app.run(host="0.0.0.0", port=8080, debug=False)
