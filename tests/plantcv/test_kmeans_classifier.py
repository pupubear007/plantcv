import numpy as np
import cv2
import os
from plantcv.plantcv.kmeans_classifier import mask_kmeans
from plantcv.plantcv.kmeans_classifier import predict_kmeans
from plantcv import plantcv as pcv


def test_kmeans_classifier(test_data):
    """Test for PlantCV."""
    input_dir = test_data.kmeans_classifier_dir
    labeled_img = predict_kmeans(img=input_dir+"/test_image.png", model_path=input_dir+"/kmeans_out.fit")
    test_labeled, _, _ = pcv.readimage(input_dir+"/labeled_image.png")
    assert (labeled_img == test_labeled).all()
    
    mask_dict = mask_kmeans(labeled_img=labeled_img, K=5)
    for i in range(5):
        assert (pcv.readimage(input_dir+"/label_example_"+str(i)+".png")[0] == mask_dict[str(i)]).all()

    combo_mask = mask_kmeans(labeled_img=labeled_img, K=5, cat_list=[1,2,3])
    combo_example, _, _ = pcv.readimage(input_dir+"/combo_mask_example.png")
    assert (combo_mask == combo_example).all()
    