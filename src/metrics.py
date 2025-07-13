import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

def dice_coefficient(img, mask, val): 
    true = 0 
    false = 0 
    rowsd, colsd = img.shape 
    itotal = 0 
    mtotal = 0 
    for r in range(rowsd): 
        for c in range(colsd): 
            if img[r, c] == val and mask[r, c] == val: 
                true += 1 
            else: 
                false += 1 
            if img[r, c] == val: 
                itotal += 1 
            if mask[r, c] == val: 
                mtotal += 1 
 
    if (mtotal + itotal) == 0: 
        return 0  # Avoid division by zero 
 
    dice = (2 * true) / (mtotal + itotal) 
    print(f"Dice Coefficient for {val}: {dice:.4f}") 
    return dice 
