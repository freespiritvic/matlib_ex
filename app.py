from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story 

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
toolbar = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    """Madlib form with questions"""
    prompts = story.prompts
    return render_template('homepage.html', prompts=prompts)

@app.route('/story')
def story_x():
    """Show the story"""
    text = story.generate(request.args)
    return render_template('story.html', text=text)
    

