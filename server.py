import pathlib
import secrets
import aiohttp
import aiofiles
from quart import Quart, jsonify, send_from_directory, url_for, request, render_template
import random
import os

app = Quart(__name__)

@app.route("/")
async def home():
    choice = random.choice(os.listdir("/root/yanpdb/nsfw_cdn/images/helltakerpics"))
    image = os.path.join("/root/yanpdb/nsfw_cdn/images/helltakerpics", choice)
    raw_image = url_for('sendfile',filename=choice)
    print(raw_image)
    return await render_template('index.html', host=request.host, raw=raw_image)

    
    

@app.route('/imgs/<filename>')
async def sendfile(filename=None):
    dir = "/root/yanpdb/nsfw_cdn/"
    p = pathlib.Path(dir)

    for f in p.rglob(filename):
        print(str(f.parent))
    
    return await send_from_directory(str(f.parent),filename)


@app.route('/helltaker')
async def helltaker():
    choice = random.choice(os.listdir("/root/yanpdb/nsfw_cdn/images/helltakerpics"))
    image = os.path.join("/root/yanpdb/nsfw_cdn/images/helltakerpics", choice)
    raw_image = url_for('sendfile',filename=choice)
    return jsonify(url=f"https://{request.host}{raw_image}")

@app.route('/hentai')
async def hentai():
    choice = random.choice(os.listdir("/root/yanpdb/nsfw_cdn/images/hentai"))
    image = os.path.join("/root/yanpdb/nsfw_cdn/images/hentai", choice)
    raw_image = url_for('sendfile',filename=choice)
    return jsonify(url=f"https://{request.host}{raw_image}")


app.run(debug=True, port=2030)