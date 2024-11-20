from flask import Flask, render_template, jsonify
from pathlib import Path
from PIL import Image

import kinshi
Kinshi = kinshi.Kinshi()

app = Flask(__name__)

@app.route("/")
def index():
    pixel_data = Kinshi.get_pixel_data()
    return render_template("index.html", width=Kinshi.width, height=Kinshi.height, pixels=pixel_data, number_of_pixels="{:,}".format(Kinshi.width * Kinshi.height), version=Kinshi.version)

@app.route("/api/v1/getPixelBuffer")
def api_v1_get_pixel_buffer():
    pixel_data = Kinshi.get_pixel_data()
    return jsonify(pixel_data)

if __name__ == "__main__":
    print("Starting server...")
    app.run(debug=True)
