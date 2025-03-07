from notes import Notebook

from flask import (
    Flask,
    jsonify,
    request,
    redirect,
    url_for,
    render_template,
    Response
)

app = Flask(__name__)

nb = Notebook()

@app.route("/", methods=['GET', 'POST'])
def index():
    """Index/home page of the website which supports either GET/POST

    Returns:
        a rendered website from a template
    """
    notes = nb.notes()

    if request.method == 'POST':
        search_term = request.form.get("search", "").strip()
        name = request.form.get("name", "").strip()
        text = request.form.get("text", "").strip()

        if search_term:
            notes = nb.find(search_term)

        elif name and text:
            nb.add(name, text)
            return redirect(url_for('index'))

    return render_template('homepage.html', notes=notes)


@app.get('/help')
def help():
    return "<p>Getting extremely minimal help via a GET request</p>"


@app.route('/notes')
def fetch_notes():
    """Load a note's contents in the page `/notes`

    Returns:
        a rendered page displaying contents of a note
    """
    note_name = request.args.get("name")
    note_text = nb[note_name].text()

    return render_template('contents.html', note_name=note_name, note_text=note_text)


@app.route('/clear', methods=['POST'])
def clear_notes():
    """Clear current notebook

    Returns:
        return to homepage
    """
    nb.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)