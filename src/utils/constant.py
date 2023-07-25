import utils.helper_functions as helper

SRC_PATH = helper.get_parent_folder(helper.get_parent_folder(__file__))

IMAGE_SIZE = (224, 224)

RECYCABLES = ['cardboard', 'glass', 'metal', 'paper', 'plastic']
NON_RECYCABLES = ['trash']
LABELS = RECYCABLES + NON_RECYCABLES
