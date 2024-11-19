from flask import Flask, render_template, jsonify

app = Flask(__name__)

import random

width = 160
height = 90

colors = ["red", "blue", "green"]

pixel_data = [[(random.randint(0, len(colors) -1)) for _ in range(width)] for _ in range(height)]

@app.route("/")
def index():
    return render_template("index.html", width=width, height=height, colors=colors, pixels=pixel_data)

@app.route("/api/v1/getPixelData/All")
def get_pixel_data_all():
    return pixel_data

@app.route("/api/v1/getPixelData/Single/<int:x>/<int:y>")
def get_pixel_data_single(x: int, y: int):
    return jsonify(pixel_data[y][x])

if __name__ == "__main__":
    app.run(debug=True)
