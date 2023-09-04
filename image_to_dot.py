import tkinter as tk
from tkinter import filedialog
import cv2

def inputConfirmation(question):
    while True:
        input_text = input(question)
        if input_text == "y":
            print("Continuing...")
            return True
            break
        elif input_text == "n":
            print("Stopping...")
            return False
            break
        else:
            print("Invalid input.")

def inputInt(question):
    while True:
        value = input(question)
        if value.isdigit():
            print("The value is " + value)
            value = int(value)
            return value
        else:
            print("The value is not a number.")

def dotValue():
    fg_value = input("The value for forground: ")
    bg_value = input("The value for background: ")
    return fg_value, bg_value


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
img = cv2.imread(file_path, 0)
# img = cv2.imread('sonic.jpg', 0)

while True:
    blurvalue = inputInt("Enter a value for blur: normal(5) ")
    
    img = cv2.medianBlur(img, blurvalue)
    image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # cv2.imshow('image',image)
    # cv2.waitKey(0)

    if inputConfirmation("Do you want to continue? (y/n) "):
        break


while True:
    ratio = len(image)/len(image[0])
    new_width = inputInt("Enter a value for width of the line: ")
    new_height = int(ratio*new_width)

    image = cv2.resize(image, (new_height, new_width))

    # cv2.imshow('image',image)
    # cv2.waitKey(0)

    if inputConfirmation("Do you want to continue? (y/n) "):
        break


while True:
    fg, bg = dotValue()

    if inputConfirmation("Do you want to continue? (y/n) "):
        break

for i in range(len(image)):
    for j in range(len(image[0])):
        print(fg if image[i, j] < 100 else bg, end="")
    print()
