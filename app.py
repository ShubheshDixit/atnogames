from flask import Flask, render_template, jsonify, request
import json, os
from get_data import get_game_details
app = Flask(__name__, template_folder='./templates/', static_folder='./static/')

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/games')
def get_games():
    with open('game_info.json', 'r') as f:
        data = json.load(f)
    return render_template('games_view.html', pages = data['game_pages'])

@app.route('/details')
def get_data():
    link = request.args.get('url')
    with open('game_info.json', 'r') as f:
        data = json.load(f)
    pages = data['game_pages']
    for page in pages:
        g_list = page['games_list']
        for game in g_list:
            g_link = game['link']
            meta = game['meta_details']
            if g_link == link:
                return jsonify(meta)

if __name__ == '__main__':
    app.run(host='192.168.1.16', port=5000)