import os

SRC_PATH = os.path.dirname(os.path.dirname((__file__)))

IMAGE_SIZE = (224, 224)

RECYCABLES = ['cardboard', 'glass', 'metal', 'paper', 'plastic']
NON_RECYCABLES = ['trash']
LABELS = RECYCABLES + NON_RECYCABLES

RECYCLE_POINTS = 10
