from PIL import Image
import numpy as np
import math
#now i want to know how much time
import time
import requests

from io import BytesIO

starttime=time.time()
def rgbtogrey(img_array):
    
    imagcreated=[]
    
    for i in img_array:
        x=[]
        for red,green,blue in i:
            greyscale= 0.2989 * red + 0.5870 * green + 0.1140 * blue
            x.append(math.ceil(greyscale))
        imagcreated.append(x)
    #ek simple tarika bhi hai
    #Image.open(file).convert("L")
    return imagcreated
    

def imagetoarray(img):
    return np.array(img)

def arrtoimg(imagcreated):
    x = np.array(imagcreated)
    return Image.fromarray(x.astype('uint8'))

#                                histogram funcitons
def scalelen(greyarr):
    x=[]
    m=[]
    for i in greyarr:
        x=set(i)
        m=list(x)+m
    return list(set(m))
        

def jaimata(x):
    i=0
    m=2**i
    print(x,m)
    while x>m:
        m=2**i
        i+=1
    return m

def nopix(mp,greyarr):
    li=[]
    for i in range(mp+1):
        j=0
        for row in greyarr:
            for col in row:
                if i==col:
                    j+=1
        li.append([i,j])
    return li


def highval(nopixel):
    m=0
    for i,j in nopixel:
        m+=j
    return m

def pdff(nopixel,x):
    pdf=[]
    for i,j in nopixel:
        pdf.append([i,j,j/x])
    return pdf


def cdff(pdf):
    cdf=[pdf[0]+[pdf[0][-1]]]
    
    for i in range(1,len(pdf)-1):
        cdf.append(pdf[i]+[pdf[i][2]+cdf[i-1][3]])
    return cdf

def sxx(cdf,mp):
    m=[]
    for i,j,k,l in cdf:
        m.append([i,l*mp])
    return m

def hiss(sx):
    m=[]
    for i,j in sx:
        m.append([i,math.ceil(j)])
    return m

def greto(histo,greyarr):
    m=greyarr

    for i in range(len(m)):
        for j in range(len(m[0])):
            
            m[i][j]=histo[m[i][j]][1]
    return m

"""def rgbii(grtrnarr):
    rarr=[[0]*len(grtrnarr)]*len(grtrnarr[0])
    rarr = np.zeros((len(grtrnarr), len(grtrnarr[0], 3), dtype=np.uint8)
    for i in range(len(grtrnarr)):
        for j in range(len(grtrnarr[0])):
            rarr[i][j]=(grtrnarr[i][j],grtrnarr[i][j],grtrnarr[i][j])
        
    return rarr"""
#input of image
"""file_path = "C:/Users/ASUS/Desktop/download.jfif"


print(file_path)
img = Image.open(file_path)"""

url= input("Enter the image URL by seeing in new tab=")
#url = "https://www.simplilearn.com/ice9/free_resources_article_thumb/what_is_image_Processing.jpg"
response = requests.get(str(url))
img = Image.open(BytesIO(response.content))


#imagetoarray
img_array = imagetoarray(img)


#rgb array to greyscale array 
greyarr= rgbtogrey(img_array)


#greyscale to image
greyimg= arrtoimg(greyarr)

#print new grey image
#greyimg.show()




#now i want "HISTOGRAM EQUALIZATION"
#1) deciding the len of greyscale
pixelsc=scalelen(greyarr)
mp=jaimata(max(pixelsc))
print(mp)

#2) number of pixels counting
nopixel= nopix(mp,greyarr)
#       sum of nopixel or len(img_array)*len(img_array[0])
x=len(img_array)*len(img_array[0])



#3) probability frequency
pdf=pdff(nopixel,x)

#4) cdfNormalization
cdf=cdff(pdf)

#5) using sx
sx=sxx(cdf,mp)

#6) now histogramed image going to be ready
histo=hiss(sx)




# now our transition is ready ,for implementation in greyscale
grtrnarr=greto(histo,greyarr)



# our arr to image
grtimg=arrtoimg(grtrnarr)

grtimg.show()






#converting it in to color image
"""rgbi=rgbii(grtrnarr)
rci=arrtoimg(rgbi)

rci.show()"""



endtime=time.time()

print("Total time taken is " ,endtime-starttime,"sec")
print(len(img_array)*len(img_array[0]),len(img_array),len(img_array[0]))
