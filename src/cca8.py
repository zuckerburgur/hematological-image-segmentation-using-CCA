import numpy as np
import cv2 
import matplotlib.pyplot as plt 

def ccn8(img): 
    eq_list = {} 
    label = 10 
    dims = img.shape 
    rows, cols = dims 
    a = np.zeros((rows, cols), dtype=np.uint8) 
 
    # First pass: Initial labeling 
    for r in range(rows): 
        for c in range(cols): 
            if img[r, c] > 215:  # Ignoring background 
                a[r, c] = 0 
            elif img[r, c]  < 255:  # Define foreground pixel condition 
                top = a[r - 1, c] if r > 0 else 0 
                left = a[r, c - 1] if c > 0 else 0 
                top_left = a[r - 1, c - 1] if (r > 0 and c > 0) else 0 
                top_right = a[r - 1, c + 1] if (r > 0 and c < cols - 1) else 0 
 
                # Collect nonzero neighbors 
                neighbors = [top, left, top_left, top_right] 
                neighbors = [n for n in neighbors if n > 0]  # Remove background (0) 
 
                if not neighbors: 
                    a[r, c] = label 
                    eq_list[label] = label 
                    label += 5 
                else: 
                    min_label = min(neighbors) 
                    a[r, c] = min_label 
 
                    # Update equivalence for all neighboring labels 
                    for n in neighbors: 
                        eq_list[n] = min(eq_list.get(n, n), min_label) 
            else: 
                a[r, c] = img[r, c] 
 
    # Second pass: Update equivalency list 
    for r in range(rows): 
        for c in range(cols): 
            a[r, c] = eq_list.get(a[r, c], a[r, c]) 
 
    # Iterative pass to propagate equivalence correctly 
    for r in range(rows): 
        for c in range(cols): 
            if a[r, c] != 0: 
                while a[r, c] != eq_list.get(a[r, c], a[r, c]): 
                    eq_list[a[r, c]] = eq_list.get(eq_list[a[r, c]], eq_list[a[r, c]]) 
                    a[r, c] = eq_list[a[r, c]] 
 
    unique_labels, counts = np.unique(a, return_counts=True) 
 
    print("Number of distinct objects:", len(np.unique(a))) 
    print(np.unique(a)) 
 
    plt.figure(figsize=(6, 6)) 
    plt.imshow(a, cmap='jet', interpolation='nearest') 
    plt.title("Relabeled Image") 
    plt.axis("off")  
    plt.show() 
 
    return a
