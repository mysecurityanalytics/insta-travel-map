from flask import Flask, render_template
from flask_caching import Cache
import instatravel
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 3600
}
app = Flask(__name__,
            static_url_path='/assets', 
            static_folder='templates/assets',
            template_folder='templates')
app.config.from_mapping(config)
cache = Cache(app)
@app.route('/', methods=['GET'])
@cache.cached()
def hello():
    return render_template('index.html')

@app.route('/byUsername/<username>', methods=['GET'])
@cache.cached()
def user(username):
    data = instatravel.get_user_data(username)
    if "error" in data:
        return render_template('404.html', data=data), 404
    else:
        return render_template('user.html', data=data)

@app.route('/byHashtag/<hashtag>', methods=['GET'])
@cache.cached()
def hashtag(hashtag):
    data = instatravel.get_hashtag_data(hashtag)
    if "error" in data:
        return render_template('404.html', data=data), 404
    else:
        return render_template('hashtag.html', data=data)

if __name__ == '__main__':
    app.run()