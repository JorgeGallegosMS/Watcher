import os
from dotenv import load_dotenv
from flask import Flask, render_template
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

host = os.environ.get('MONGODB_URI')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()

# games = db.games

league_of_legends = {
    'name': 'League of Legends',
    'image': 'https://dotesports-media.nyc3.cdn.digitaloceanspaces.com/wp-content/uploads/2019/09/12195522/league-of-legends.jpg'
}

dota2 = {
    'name': 'Dota 2',
    'image': 'https://esportsobserver.com/wp-content/uploads/2019/05/dota-2-russia.png'
}

csgo = {
    'name': 'Counter-Strike: Global Offensive',
    'image': 'https://www.oratoryprepomega.org/wp-content/uploads/2018/04/Feature-Image-1-1200x1200.jpg'
}
rocket_league = {
    'name': 'Rocket League',
    'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW64dCTYk1c662BQdDgnUsHaJeR1kdQvxOlyFOOf7zeA9zBs2m'
}

games = [league_of_legends, dota2, csgo, rocket_league]

@app.route('/')
def index():
    """Show all games"""
    return render_template('index.html.j2', games=games)

@app.route('/games/new')
def games_new():
    """Show form for new game"""
    return render_template('games_new.html.j2')

if __name__ == '__main__':
    app.run(debug=True)