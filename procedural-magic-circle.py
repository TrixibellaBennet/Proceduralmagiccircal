from PIL import Image
from PIL import ImageDraw
import random
import time
from datetime import datetime
import threading

num = 0
length = 3840
height = 2160
ran = [0]*length
numwrite = 0
threadscomplete=[0,0,0,0]
xy=[]

img = Image.new(mode="RGB", size=(length,height), color="black")

pixels = img.load()

draw = ImageDraw.Draw(img)

def imgpixels(startnum, threads):
    for i in range(startnum,img.size[0],threads):
        for j in range(img.size[1]):
            rgb=(random.randint(0,254),random.randint(0,254),random.randint(0,254))
            pixels[i,j] = (rgb)
            print("thread: " + str(startnum) + " Position: " + str(i)+","+str(j))
    threadscomplete[startnum]=1

def circle(thread, radius, number):
    rr = random.randint(0, 600)
    for i in range(600):
        rgb=(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        xy=((random.randint(0, length)),(random.randint(0, height)))
        #print(xy)
        draw.ellipse((xy[0]-rr,xy[0]+rr,xy[1]-rr,xy[1]+rr), outline=rgb)
        draw.ellipse((xy[0]+rr,xy[0]-rr,xy[1]+rr,xy[1]-rr), outline=rgb)
        draw.ellipse((xy[0]-rr,xy[0]-rr,xy[1]+rr,xy[1]+rr), outline=rgb)
        draw.ellipse((xy[0]+rr,xy[0]+rr,xy[1]-rr,xy[1]-rr), outline=rgb)

t1 = threading.Thread(target=circle, args=(0,40,2))
t2 = threading.Thread(target=circle, args=(1,40,2))
t3 = threading.Thread(target=circle, args=(2,40,2))
t4 = threading.Thread(target=circle, args=(3,40,2))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

img.save('test.jpg')
