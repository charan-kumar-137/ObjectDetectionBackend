from detection.mrcnn.config import Config
import detection.mrcnn.model as modellib
from detection.mrcnn.visualize import display_instances
from django.conf import settings
import tensorflow as tf
import skimage, skimage.io
import numpy as np


class InferenceConfig(Config):
    NAME = "images"
    NUM_CLASSES = 1 + 80
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


def color_splash(image, mask):
    """Apply color splash effect.
    image: RGB image [height, width, 3]
    mask: instance segmentation mask [height, width, instance count]
    Returns result image.
    """
    # Make a grayscale copy of the image. The grayscale copy still
    # has 3 RGB channels, though.
    gray = skimage.color.gray2rgb(skimage.color.rgb2gray(image)) * 255
    # Copy color pixels from the original color image where mask is set
    if mask.shape[-1] > 0:
        # We're treating all instances as one, so collapse the mask into one layer
        mask = (np.sum(mask, -1, keepdims=True) >= 1)
        splash = np.where(mask, image, gray).astype(np.uint8)
    else:
        splash = gray.astype(np.uint8)
    return splash


class Model:

    def __init__(self):
        config = InferenceConfig()
        self.session = tf.Session()
        tf.python.keras.backend.set_session(self.session)
        self.model = modellib.MaskRCNN(mode="inference", model_dir=settings.MODEL_DIR, config=config)
        self.model.load_weights(settings.COCO_MODEL_PATH, by_name=True)
        # self.graph = tf.get_default_graph()
        self.model.keras_model._make_predict_function()

    class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
                   'bus', 'train', 'truck', 'boat', 'traffic light',
                   'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
                   'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
                   'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
                   'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
                   'kite', 'baseball bat', 'baseball glove', 'skateboard',
                   'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
                   'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
                   'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
                   'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
                   'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
                   'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
                   'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
                   'teddy bear', 'hair drier', 'toothbrush']

    def detect(self, image_list=None, *args, **kwargs):
        with self.session.as_default():
            with self.session.graph.as_default():
                results = self.model.detect(image_list, verbose=1)
                r = results[0]
                # img = color_splash(image_list[0], r['masks'])
                img = display_instances(image_list[0], r['rois'], r['masks'], r['class_ids'], self.class_names,
                                        r['scores'])
                return img
