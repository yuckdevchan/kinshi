from pathlib import Path
import pickle

# Format of objects:
# tuple:
#     0: object type (0: plane, 1: cube, 2: sphere)
#     1: position (x, y, z)
#     2: scale (x, y, z)
#     3: rotation (x, y, z)
#     4: color (r, g, b, a)

kscene = {
    "metadata": {
        "name": "demo",
        "author": "Ethan Martin",
        "version": "0.1",
        "desc": "A demo scene for Kinshi"
    },
    "scene": {
        "objects": (
            (0, (0, 0, 0), (1, 1, 1), (0, 0, 0), (255, 0, 0, 1)),
        )
    }
}

with open(Path(f"../scenes/{kscene["metadata"]["name"]}.ksd"), "wb") as f:
    pickle.dump(kscene, f)
