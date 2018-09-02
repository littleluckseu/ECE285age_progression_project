import re
IMAGE_PATH = "./data/UTKFace"
EPOCHS = 100
IMAGE_LENGTH = 128
IMAGE_DEPTH = 3


BATCH_SIZE = 64
KERNEL_SIZE = 2
STRIDE_SIZE = 2

NUM_ENCODER_CHANNELS = 64
NUM_Z_CHANNELS = 100
NUM_GEN_CHANNELS = 1024

NUM_AGES = 10
NUM_GENDERS = 2
LABEL_LEN = NUM_AGES + NUM_GENDERS

NUM_GENDERS_EXPANDED = NUM_GENDERS * (NUM_AGES // NUM_GENDERS)
LABEL_LEN_EXPANDED = NUM_AGES + NUM_GENDERS_EXPANDED


UTKFACE_ORIGINAL_IMAGE_FORMAT = re.compile('^(\d+)_(\d+)_\d+_(\d+)\.jpg\.chip\.jpg$')


MALE = 0
FEMALE = 1

UTKFACE_DEFAULT_PATH = './data/UTKFace'
utkface_path = UTKFACE_DEFAULT_PATH

TRAINED_MODEL_EXT = 'dat'
TRAINED_MODEL_FORMAT = "{}." + TRAINED_MODEL_EXT
