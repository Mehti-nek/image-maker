import cv2

img = cv2.imread('sonic.jpg', 0)
img = cv2.medianBlur(img, 5)

cv2.imshow('image',img)
cv2.waitKey(0)

image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 11, 2)

cv2.imshow('image',image)
cv2.waitKey(0)

ratio = len(image)/len(image[0])
new_width = 60
new_height = int(ratio*new_width)

image = cv2.resize(image, (new_height, new_width))

cv2.imshow('image',image)
cv2.waitKey(0)

for i in range(len(image)):
    for j in range(len(image[0])):
        print("." if image[i, j] < 100 else " ", end="")
    print()
