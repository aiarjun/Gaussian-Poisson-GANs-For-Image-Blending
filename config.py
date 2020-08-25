'''DATA'''
CROPPED_SAMPLES_DIR = '../../../cropped_images'
NUM_TRAIN_SAMPLES = 100000 # IMPORTANT
CENTER_SQUARE_RATIO = 0.5
SCALING_SIZE = 64
OUTPUT_SIZE = 64
TRAIN_BATCH_SIZE = 64 # IMPORTANT
TRAIN_SHUFFLE = True
TRAIN_NUM_WORKERS = 0
VAL_BATCH_SIZE = 8 # IMPORTANT
VAL_SHUFFLE = False
VAL_NUM_WORKERS = 0
VAL_RATIO = 0.1
NUM_VAL_SAMPLES = 64 # IMPORTANT

'''NET'''
NUM_ENCODER_FILTERS = 64
NUM_DECODER_FILTERS = 64
NUM_BOTTLENECK = 4000
NUM_OUTPUT_CHANNELS = 3

'''TRAINING'''
G_LR = 5e-4 # IMPORTANT
D_LR = 5e-4 # IMPORTANT
ADAM_BETA1 =0.5
START_EPOCH = 0
NUM_EPOCHS = 15 # IMPORTANT
D_ITERS = 5 # IMPORTANT
D_CLAMP_RANGE = [-0.01, 0.01] # IMPORTANT

'''TRAINING - LOGGING'''

PRINT_EVERY = 1 # gen_iter iterations 
LOGGING_K = 5
CHECKPOINT_DIR = 'experiments'
SAVE_TO_CLOUD_EVERY = 1 # EPOCHS