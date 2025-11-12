import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST'), port=6379)

@app.route('/')
def hello():
    count = redis.incr('visitor_count')
    return f'Hello! You are visitor number - {count}.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
