from flask import Flask, request, render_template
from stories import Story
app = Flask(__name__)

@app.route('/')
def index():
    "Returns Madlibs form"

    word_list = story.prompts

    return render_template('base.html', word_list=word_list)

@app.route('/story')
def results():
    "returns the Madlibs story"   

    resulting_story = story.generate(request.args)

    # request.args returns an object so we don't need to make a separate object to loop through 
    # ImmutableMultiDict([('place', 'SF'), ('noun', 'mouse'), ('verb', 'ran'), ('adjective', 'red'), ('plural_noun', 'mice')])

    return resulting_story


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
