from pathlib import Path
from PIL import Image
import random, json

class Kinshi:
    def config_loader(self):
        with open("config.json") as f:
            return json.load(f)    
    
    def __init__(self):
        self.config = self.config_loader()
        self.version = self.config["version"]

        self.scale = self.config["output"]["scale"]
        self.width = round(self.config["output"]["width"] * self.scale)
        self.height = round(self.config["output"]["height"] * self.scale)

        self.pixel_data = [[[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 1] for x in range(self.width)] for y in range(self.height)]
        # self.pixel_data = [[[0, 0, 0, 1] for x in range(self.width)] for y in range(self.height)]

        image = self.decode_png(Path("textures/wotang.png"))
        center_x = self.width // 2
        center_y = self.height // 2

        # self.add_image(image, center_x, center_y)

    def add_image(self, image, x, y):
        image_width = len(image[0])
        image_height = len(image)
        for y in range(image_height):
            for x in range(image_width):
                target_y = y - image_height // 2 + y
                target_x = x - image_width // 2 + x
                if 0 <= target_y < self.height and 0 <= target_x < self.width:
                    self.pixel_data[target_y][target_x] = image[y][x]

    def decode_png(self, image_path: Path):
        try:
            with open(image_path, "rb") as f:
                data = f.read()
        except FileNotFoundError:
            image_path = Path("textures/missing.png")
            with open("textures/missing.png", "rb") as f:
                data = f.read()
        img = Image.open(image_path)
        img = img.convert("RGBA")
        img_data = img.load()
        
        img_width, img_height = img.size
        
        # convert the image to the pixel_data format
        pixel_data_img = [[[0, 0, 0, 1] for x in range(img_width)] for y in range(img_height)]
        for y in range(img_height):
            for x in range(img_width):
                r, g, b, a = img_data[x, y]
                pixel_data_img[y][x] = [r, g, b, a]
        return pixel_data_img
    
    def get_pixel_data(self):
        return self.pixel_data
