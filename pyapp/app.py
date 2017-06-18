from flask import Flask
from redis import Redis
import socket

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    whichhost = socket.gethostname()
    hosthits = redis.incr(whichhost)

    return 'Hello from docker in EC2! I have been seen {0} times total, but {1} times from host {2}.\n'.format(count,hosthits,whichhost)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

