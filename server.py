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
    folder = random.choice(['helltakerpics', 'hentai'])
    choice = random.choice(os.listdir(f"/root/yanpdb/nsfw_cdn/images/{folder}"))
    raw_image = f"https://i.hosst.gay/{choice}"
    print(raw_image)
    return await render_template('index.html', host=request.host, raw=raw_image)

    


@app.route('/api/v1/helltaker')
async def helltaker():
    choice = random.choice(os.listdir("/root/yanpdb/nsfw_cdn/images/helltakerpics"))
    image = os.path.join("/root/yanpdb/nsfw_cdn/images/helltakerpics", choice)
    raw_image = f"https://i.hosst.gay/{choice}"
    return jsonify(url=f"{raw_image}")

@app.route('/api/v1/hentai')
async def hentai():
    choice = random.choice(os.listdir("/root/yanpdb/nsfw_cdn/images/hentai"))
    image = os.path.join("/root/yanpdb/nsfw_cdn/images/hentai", choice)
    raw_image = f"https://i.hosst.gay/{choice}"
    return jsonify(url=f"{raw_image}")


app.run(debug=True, port=2030)