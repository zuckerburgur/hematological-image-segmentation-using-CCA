import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

def conv(img, mask_size, mask_val): 
    dims = img.shape 
    rows, cols = dims 
    midval = mask_size // 2  # Padding size 
    ifilter = np.ones((mask_size, mask_size), dtype=np.int8) * (mask_val/mask_size**2) #blurring filter 
    padded_image = np.zeros((rows + 2 * midval, cols + 2 * midval), dtype=np.uint8) 
    padded_image[midval:midval + rows, midval:midval + cols] = img 
    output_image = np.zeros((rows, cols), dtype=np.uint8) 
 
    for r in range(rows): 
        for c in range(cols): 
            sub_image = padded_image[r:r + mask_size, c:c + mask_size] 
            result_value = np.sum(sub_image * ifilter) 
            output_image[r, c] = result_value 
 
    cv2.imshow('win1', output_image) 
    cv2.waitKey() 
    cv2.destroyAllWindows() 
    return output_image 

def power_law(img, gamma): 
    dims = img.shape 
    rows, cols = dims 
    new_img = np.zeros((rows, cols), dtype=np.uint8) 
    for r in range(rows): 
        for c in range(cols): 
            new_img[r, c] = int(255 * np.power(img[r, c]/255, gamma)) 
 
    fig, axes = plt.subplots(1, 2, figsize=(10, 5)) 
    axes[0].imshow(img, cmap='gray') 
    axes[0].set_title("Original Image") 
    axes[0].axis("off") 
 
    axes[1].imshow(new_img, cmap='gray') 
    axes[1].set_title(f"Enhanced (Gamma={gamma})") 
    axes[1].axis("off") 
 
    plt.show() 
    return new_img 
