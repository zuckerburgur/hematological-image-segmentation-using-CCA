from src.preprocessing import conv, power_law
from src.cca8 import ccn8
from src.segmentation import thresh, largest_object
from src.metrics import dice_coefficient

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
  
    # Reading the test image and mask in grayscale 
    image_path = "data/test/219.bmp" # substitute with actual paths
    mask_path = "data/test/219.png"

    img = cv2.imread(image_path, 0)
    mask = cv2.imread(mask_path, 0)

    # Visualize
    plt.imshow(img, cmap="gray")
    plt.title("Original Image")
    plt.colorbar()
    plt.show()

  # Applying an averaging blur filter to smoothen the image 
  firstblur = conv(imagebmp, 5,1) 
 
  # 8-Connected CCA to label the WBC 
  first_seg = ccn8(firstblur) 
 
  # Eliminating everything other than the cell body 
  cyto = largest_object(first_seg, 128) 
  cv2.namedWindow('Cytoplasm', cv2.WINDOW_NORMAL) 
  cv2.imshow('Cytoplasm', cyto) 
  cv2.waitKey() 
 
  # Power transform to enhance contrast 
  cont = power_law(img, 2.0) 
 
  # Masking the image with the cytoplasm mask to isolate cell body 
  cont_dim = cont.shape 
  rowc, colc = cont_dim 
  for rc in range(rowc): 
      for cc in range(colc): 
          if cyto[rc, cc] == 0: 
              cont[rc, cc] = 0 
 
  # Applying the blur filter to smoothen the image again
  blur = conv(cont, 5, 1) 
 
  # Thresholding to identify the nucleus 
  nucleus = thresh(blur, 75) 
   
  # Combining cytoplasm and nucleus for mask 
  rows, cols = cyto.shape 
  for r in range(rows): 
      for c in range(cols): 
          if cyto[r, c] != 0: 
              if nucleus[r, c] > cyto[r, c]: 
                  cyto[r, c] = nucleus[r, c] 
  cv2.imshow('Computed Mask', cyto) 
  cv2.waitKey() 

  
  # Dice Coefficient
  print("Dice (BG):", dice_coefficient(final_mask, mask, 0))
  print("Dice (Cyto):", dice_coefficient(final_mask, mask, 128))
  print("Dice (Nucleus):", dice_coefficient(final_mask, mask, 255))

if __name__ == "__main__":
    main()
