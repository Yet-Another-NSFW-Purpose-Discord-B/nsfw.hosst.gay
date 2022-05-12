import logging
import pathlib
import secrets
import aiohttp
import aiofiles
from quart import Quart, jsonify, send_from_directory, url_for, request, render_template
import random
import os
import quart.flask_patch  
import thino

app = Quart(__name__)
from swagger_ui import quart_api_doc
logger = logging.getLogger('thino.pics')
fh = logging.FileHandler('logs/home.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

quart_api_doc(app, config_path="openapi.json", url_prefix='/docs', title='API doc')

@app.route("/search/<filename>")
async def search(filename):
    dir = "/mnt/volume_nyc1_02/images/"
    p = pathlib.Path(dir)


    for f in p.rglob(filename):
        print(str(f.parent))

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/hentai"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/hentai", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/helltakerpics"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/helltaker", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/neko"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/neko", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/tomboy"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/tomboy", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/femboy"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/femboy", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)
    
    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/thighs"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/thighs", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/dildo"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/dildo", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/porn"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/porn", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)


@app.route("/")
async def home():

    folder = random.choice(['helltakerpics', 'hentai', 'neko', 'tomboy', 'thighs', 'porn', 'dildo'])
    choice = random.choice(os.listdir(f"/mnt/volume_nyc1_02/images/{folder}"))
    

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://thino.pics/search/{choice}") as res:
            data = await res.json()
            endpoint = data['url']
            filename = data['filename']
            raw_image = data['image']
            logger.debug(endpoint)
            logger.debug(raw_image)
            logger.debug(filename)


            return await render_template('index.html',  raw=raw_image, endpoint=endpoint, filename=filename)

@app.route("/dildo")
async def dildo_show():
    choice = random.choice(os.listdir(f"/mnt/volume_nyc1_02/images/dildo"))
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://thino.pics/search/{choice}") as res:
            data = await res.json()
            raw_image = data['image']
            filename = data['filename']
            endpoint = data['url']

            logger.debug(endpoint)
            logger.debug(raw_image)
            logger.debug(filename)
            return await render_template("image_show.html", host=request.host, raw=raw_image, filename=filename)




@app.route("/tomboy")
async def tomboy_show():
    choice = random.choice(os.listdir(f"/mnt/volume_nyc1_02/images/tomboy"))
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://thino.pics/search/{choice}") as res:
            data = await res.json()
            endpoint = data['url']
            raw_image = data['image']
            filename = data['filename']

            logger.debug(endpoint)
            logger.debug(raw_image)
            logger.debug(filename)
            return await render_template("image_show.html", host=request.host, raw=raw_image, endpoint=endpoint, filename=filename)


@app.route('/api/v1/helltaker')
async def helltaker():
    choice = random.choice(os.listdir("/mnt/volume_nyc1_02/images/helltakerpics"))
    image = os.path.join("/mnt/volume_nyc1_02/images/helltakerpics", choice)
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}", endpoint="https://thino.pics/api/v1/helltaker",filename=choice, status=200)

@app.route('/api/v1/hentai')
async def hentai():
    choice = random.choice(os.listdir("/mnt/volume_nyc1_02/images/hentai"))
    image = os.path.join("/mnt/volume_nyc1_02/images/hentai", choice)
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}", endpoint="https://thino.pics/api/v1/hentai",filename=choice, status=200)

@app.route("/api/v1/neko")
async def neko():
    choice = random.choice(os.listdir("/mnt/volume_nyc1_02/images/neko"))
    image = os.path.join("/mnt/volume_nyc1_02/images/neko", choice)
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}",  endpoint="https://thino.pics/api/v1/neko",filename=choice, status=200)

@app.route("/api/v1/tomboy")
async def tomboy():
    choice = random.choice(os.listdir(f"/mnt/volume_nyc1_02/images/tomboy"))
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}", endpoint="https://thino.pics/api/v1/tomboy",filename=choice, status=200)

@app.route("/api/v1/femboy")
async def femboy():
    choice = random.choice(os.listdir(f"/mnt/volume_nyc1_02/images/femboy"))
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}", endpoint="https://thino.pics/api/v1/femboy",filename=choice, status=200)

@app.route("/api/v1/thighs")
async def thighs():
    choice = random.choice(os.listdir(f"/mnt/volume_nyc1_02/images/thighs"))
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}", endpoint="https://thino.pics/api/v1/thighs",filename=choice, status=200)

@app.route("/api/v1/dildo")
async def dildo():
    choice = random.choice(os.listdir(f"/mnt/volume_nyc1_02/images/dildo"))
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}", endpoint="https://thino.pics/api/v1/dildo",filename=choice, status=200)

@app.route('/api/v1/porn')
async def porn():
    choice = random.choice(os.listdir("/mnt/volume_nyc1_02/images/porn"))
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}", endpoint="https://thino.pics/api/v1/porn",filename=choice, status=200)

@app.route('/api/v1/feet')
async def feet(): #:vomit:
    choice = random.choice(os.listdir("/mnt/volume_nyc1_02/images/feet"))
    raw_image = f"https://i.thino.pics/{choice}"
    return jsonify(url=f"{raw_image}", endpoint="https://thino.pics/api/v1/feet",filename=choice, status=200)


@app.route('/check', methods=['POST']) #this route is made to be checked with stuff like uptime kuma and other stuff 
async def uptime_check():
    return "Checked",200

app.run(debug=True, port=2030)