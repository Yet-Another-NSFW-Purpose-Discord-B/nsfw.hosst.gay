import logging
import pathlib
import secrets
import aiohttp
import aiofiles
from quart import Quart, jsonify, send_from_directory, url_for, request, render_template
import random
import os
import quart.flask_patch    




app = Quart(__name__)
from swagger_ui import quart_api_doc
logger = logging.getLogger('thino.pics')
fh = logging.FileHandler('thino.pics.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

quart_api_doc(app, config_path="openapi.json", url_prefix='/docs', title='API doc')



@app.route("/")
async def home():
    folder = random.choice(['helltakerpics', 'hentai', 'neko', 'tomboy'])
    choice = random.choice(os.listdir(f"/root/yanpdb/nsfw_cdn/images/{folder}"))
    print(choice)
    

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://i.thino.pics/search/{choice}") as res:
            data = await res.json()
            endpoint = data['url']
            raw_image = data['image']


            logger.debug(endpoint)
            logger.debug(raw_image)
            return await render_template('index.html', host=request.host, raw=raw_image, endpoint=endpoint)





@app.route('/api/v1/helltaker')
async def helltaker():
    choice = random.choice(os.listdir("/root/yanpdb/nsfw_cdn/images/helltakerpics"))
    image = os.path.join("/root/yanpdb/nsfw_cdn/images/helltakerpics", choice)
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}")

@app.route('/api/v1/hentai')
async def hentai():
    choice = random.choice(os.listdir("/root/yanpdb/nsfw_cdn/images/hentai"))
    image = os.path.join("/root/yanpdb/nsfw_cdn/images/hentai", choice)
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}")

@app.route("/api/v1/neko")
async def neko():
    choice = random.choice(os.listdir("/root/yanpdb/nsfw_cdn/images/neko"))
    image = os.path.join("/root/yanpdb/nsfw_cdn/images/neko", choice)
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}")

@app.route("/api/v1/tomboy")
async def tomboy():
    choice = random.choice(os.listdir(f"/root/yanpdb/nsfw_cdn/images/tomboy"))
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}")

@app.route('/check', methods=['POST'])
async def uptime_check():
    return "Checked!"

app.run(debug=True, port=2030)