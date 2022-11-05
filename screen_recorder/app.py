
from cv2 import COLOR_BGR2RGB
import Pillow 
from PIL import ImageGrab
import  numpy  as np
import cv2
import pywin32_system32 
from win32api  import GetSystemMetrics
import datetime
height= GetSystemMetrics(0)

width= GetSystemMetrics(1)
time_stamp=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
print(height , width)
file_name= f'{time_stamp}.mp4'
storage= cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # that store the video in computer : 
capture= cv2.VideoWriter('file_name', storage, 20.0 , (height,  width ))
#                        name , varable , frame rate , frame size 
img=cv2.VideoCapture(1)

while True : 
    img=ImageGrab.grab(bbox=(0, 0 ,  width, height ))
    img_np= np.array(img) # we store the imaege as array : 
    img_col= cv2.cvtColor(img_np , cv2,COLOR_BGR2RGB)
    cv2.imshow('Secret Capture ', img_np)
    capture.write(img_col)
    
    if cv2.waitKey(10) == ord('q'): 
        break 
      
    
    
    
    