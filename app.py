import os
from flask import Flask
from redis import Redis

redisHost = os.environ['REDIS_HOST']
appPort = int(os.environ['APP_PORT'])

app = Flask(__name__)

redis = Redis(host=redisHost, port=6379)

@app.route('/auth')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=appPort, debug=True)

