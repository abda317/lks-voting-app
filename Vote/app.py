from flask import Flask, render_template, request
import socket
import os
import redis

app = Flask(__name__)
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = 6379
r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vote = request.form["vote"]
        r.incr(vote, 1)
    cat_votes = int(r.get("cat") or 0)
    dog_votes = int(r.get("dog") or 0)
    return render_template("index.html", cat=cat_votes, dog=dog_votes, hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
