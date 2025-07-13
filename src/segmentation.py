import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

def largest_object(labelled_img, value): 
    rows, cols = labelled_img.shape 
    unique_labels, counts = np.unique(labelled_img, return_counts=True) 
    label_counts = dict(zip(unique_labels, counts)) 
    label_counts.pop(0, None)  # Not considering bg 
 
    if not label_counts: 
        print("No objects detected!") 
        return labelled_img 
 
    # Find the label of the largest object 
    largest_label = max(label_counts, key=label_counts.get) 
    for r in range(rows): 
        for c in range(cols): 
            if labelled_img[r, c] != largest_label: 
                labelled_img[r, c] = 0 
            else: 
                labelled_img[r, c] = value 
    return labelled_img 
  
def thresh(img, val): 
    threshold_val = val 
    dims = img.shape 
    rows, cols = dims 
    new_img = np.ones((rows, cols), dtype=np.float32) 
    for r in range(rows): 
        for c in range(cols): 
            if img[r, c] < threshold_val: 
                new_img[r, c] = 255 
            else: 
                new_img[r,c] = 0 
    cv2.imshow('win1', new_img) 
    cv2.waitKey() 
    return new_img 
