from notebook import app
from notebook.notes import Notebook

from flask import (
    Flask,
    jsonify,
    request,
    redirect,
    url_for,
    render_template,
    Response
)


@app.route("/", methods=['GET', 'POST', 'DELETE'])
def index():
    """Index/home page of the website which supports either GET/POST

    Returns:
        a rendered website from a template
    """

    if request.method == 'POST':
        search_term = request.form.get("search_term", "").strip()
        name = request.form.get("title", "").strip()
        text = request.form.get("content", "").strip()

        # While user searches any note containing a term
        if search_term:
            notes = Notebook.find(term=search_term)
            return render_template("homepage.html", notes=notes)

        # While user adds a new note
        elif name and text:
            result = Notebook.add_note(name=name, text=text)

            if result is not True:
                return result

            return redirect("/")

    if request.method == 'DELETE':
        Notebook.clear()
        return jsonify({"message": "All notes are removed successfully!"}), 200

    # Default: displaying names of exisiting notes in DB
    notes = Notebook.show_all_note_names()

    return render_template('homepage.html', notes=notes)


@app.get('/help')
def help():
    return "<p>Getting extremely minimal help via a GET request</p>"


@app.route('/<string:name>', methods=['GET', 'POST', 'DELETE'])
def fetch_note(name: str):
    note = Notebook.fetch_note(name)

    if not note:
        return redirect(url_for('index'))

    if request.method == 'POST':
        comment_text = request.form.get('text', '').strip()

        if comment_text:
            comment = Notebook.add_comment(comment_text, note.id)
            return jsonify({
                'comment_text': comment.text,
                'comment_date': comment.date
            })

    if request.method == 'DELETE':
        Notebook.delete_note(note.id)
        return jsonify({'message': 'Note deleted successfully!'}), 200

    comments = note.comments

    return render_template(
        "contents.html",
        note_id=note.id,
        note_name=note.name,
        note_text=note.text,
        comments=comments
    )
