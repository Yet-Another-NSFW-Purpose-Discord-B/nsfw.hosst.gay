from flask import Flask, jsonify, send_from_directory, url_for, request
import random
import os

app = Flask(__name__)

@app.route('/imgs/<filename>')
def sendfile(filename=None):
    dir = "/root/yanpdb/nsfw_cdn/images"
    image = os.path.join(dir, filename)

    return send_from_directory(dir,filename)


@app.route('/helltaker')
def helltaker():
    choice = random.choice(os.listdir("/root/yanpdb/nsfw_cdn/images"))
    image = os.path.join("/root/yanpdb/nsfw_cdn/images", choice)
    raw_image = url_for('sendfile',filename=choice)
    return jsonify(url=f"https://{request.host}{raw_image}")


if __name__ == "__main__":
    app.run(debug=True, port=2030)