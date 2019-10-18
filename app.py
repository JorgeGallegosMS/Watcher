import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

host = os.environ.get('MONGODB_URI')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()

games = db.games
# client.drop_database(db)

@app.route('/')
def games_index():
    """Show all games"""
    return render_template('games_index.html.j2', games=games.find())

@app.route('/games/new')
def games_new():
    """Show form for new game"""
    return render_template('games_new.html.j2', game={}, title='New Game')

@app.route('/games', methods=['POST'])
def games_submit():
    """Submit game to database"""
    game = {
        'name': request.form.get('name'),
        'image': request.form.get('image')
    }
    game_id = games.insert_one(game).inserted_id

    return redirect(url_for('games_show', game_id=game_id))

@app.route('/games/<game_id>')
def games_show(game_id):
    """Show one game"""
    game = games.find_one({'_id': ObjectId(game_id)})
    return render_template('games_show.html.j2', game=game)

@app.route('/games/<game_id>/edit')
def games_edit(game_id):
    """Show form to edit a game"""
    game = games.find_one({'_id': ObjectId(game_id)})
    return render_template('games_edit.html.j2', game=game, title='Edit Game')

@app.route('/games/<game_id>', methods=['POST'])
def games_update(game_id):
    """Submit updated game to database"""
    updated_game = {
        'name': request.form.get('name'),
        'image': request.form.get('image')
    }

    games.update_one(
        {'_id': ObjectId(game_id)},
        {'$set': updated_game}
    )

    return redirect(url_for('games_show', game_id=game_id))

@app.route('/games/<game_id>/delete', methods=['POST'])
def games_delete(game_id):
    """Delete a game"""
    games.delete_one({'_id': ObjectId(game_id)})
    return redirect(url_for('games_index'))




if __name__ == '__main__':
    app.run(debug=True)