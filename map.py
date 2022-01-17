from re import I
from flask import Flask, send_file, make_response
from PIL import Image
from io import BytesIO
from os import path

app = Flask(__name__)

red = Image.open(path.join(path.dirname(__file__), "sprites/red.png"))
yellow = Image.open(path.join(path.dirname(__file__), "sprites/yellow.png"))
blank = Image.open(path.join(path.dirname(__file__), "sprites/blank.png"))


@app.route("/map/<map>")
def render_map(map):
    if len(map) != 42:
        return make_response("Invalid map size", 403)

    im = Image.new("RGBA", (7*16, 6*16), color=(0, 86, 143))
    for i in range(len(map)):
        x = i % 7
        y = i // 7

        if map[i] == "0":
            sprite = blank
        elif map[i] == "1":
            sprite = red
        elif map[i] == "2":
            sprite = yellow
        else:
            raise "ouch"

        im.paste(sprite, (x * 16, y*16))

    img_io = BytesIO()
    im.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype="image/jpg")
