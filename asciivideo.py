#let's import the libraries we are going to use
import numpy as np 
import cv2
from pandas import cut
from os import system,get_terminal_size
from time import sleep

from PIL import ImageGrab
#function to turn an image to ascii
def image_to_ascii(img):
    #converting it to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #get the new dimensions based on the cmd window
    new_width=get_terminal_size().columns
    new_height=get_terminal_size().lines
    #resize 
    img_array=cv2.resize(img,(new_width,new_height))
    chars=["@","#","S","%","?","*","+",";",":",",","."]
    interv=list(cut(img_array.ravel(),len(chars),labels=chars[::-1]))
    pixel_count=img_array.shape[0]*img_array.shape[1]
    ascii_image="\n".join("".join(interv[i:(i+new_width)]) for i in range(0,pixel_count,new_width))
    return ascii_image

#let's start recording
cam=cv2.VideoCapture(0)
#we are going to save all the frames in the frames list
frames=[]
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        cam.release()
        break
    frames.append(image_to_ascii(frame))
    cv2.imshow("Press q to quit",frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        print("End recording..")
        cv2.destroyAllWindows()
        break
cam.release()
print("Now processing....")
sleep(4)
for frame in frames:
    system("cls")
    print(frame)
    sleep(1/20)