#name: Qixuan Hou
#section: A04
#GTID: 903000267
#GTemail: qhou6@gatech.edu
#collaboration statement: I worked on the homework with my partner.





from Myro import*


#for the beginning part
def beginningPart():
    p=makePicture("pic1.jpg")
    p1=makePicture("pic1.jpg")
    p2=makePicture("pic2.jpg")
    p3=makePicture("pic3.jpg")
    for pix in getPixels(p3):
        setRed(pix,255)
    for pix in getPixels(p2):
        setRed(pix,140)
        setGreen(pix,140)
    for pix in getPixels(p1):
        setGreen(pix,255)
    show(p)
    wait(0.5)
    show(p3)
    wait(0.5)
    show(p2)
    wait(0.5)
    show(p1)
    wait(0.5)
    show(p)


#for the racing part

#14/15

def crossFade():
    pic=makePicture("pic14.jpg")
    pic2=makePicture("pic15.jpg")
    for y in range(getHeight(pic)):
        for x in range(getWidth(pic)):
            pix=getPixel(pic,x,y)
            pix2=getPixel(pic2,x,y)
            setRed(pix,getRed(pix2))
            setGreen(pix,getGreen(pix2))
            setBlue(pix,getBlue(pix2))
        wait(0.02)
        show(pic)




#29-33

def wetFloor():
    for i in range(29,34):
        p=makePicture("pic"+str(i)+".jpg")
        blackAndWhite(p)
        show(p)


def blackAndWhite(pic):
    for pix in getPixels(pic):
        r=getRed(pix)
        b=getBlue(pix)
        g=getGreen(pix)
    
        l=(r+b+g)/3
        if l<64:
    
            setRed(pix,64)
            setBlue(pix,64)
            setGreen(pix,64)
        elif l>=64 and l<128:
            setRed(pix,128)
            setBlue(pix,128)
            setGreen(pix,128)
        elif l>=128 and l<192:
            setRed(pix,192)
            setBlue(pix,192)
            setGreen(pix,192)
        else:
            setRed(pix,255)
            setBlue(pix,255)
            setGreen(pix,255)
    savePicture(pic,"blackAndWhite.jpg")
    show(pic)


def fade(pic):

        show(pic)
        for pix in getPixels(pic):
            r=getRed(pix)
            g=getGreen(pix)
            b=getBlue(pix)
            setRed(pix,r/2)
            setBlue(pix,b/2)
            setGreen(pix,g/2)

        show(pic)




def overlay():
    pic=makePicture("pic63.jpg")
    pic1=makePicture("1.png")
    h=getHeight(pic1)
    w=getWidth(pic1)


    for x in range(w):
        for y in range(h):
            pix1=getPixel(pic1,x,y)
            pix=getPixel(pic,x+250,y+80)
            setRed(pix,getRed(pix1))
            setGreen(pix,getGreen(pix1))
            setBlue(pix,getBlue(pix1))

    show(pic)



#performance code
def performanceCode():
    beginningPart()
    for i in range(4,14):
        p=makePicture("pic"+str(i)+".jpg")
        show(p)
        wait(0.5)
    crossFade()
    for i in range(16,29):
        p=makePicture("pic"+str(i)+".jpg")
        show(p)
        wait(0.5)
    wetFloor()
    for i in range(34,55):
        p=makePicture("pic"+str(i)+".jpg")
        show(p)
        wait(0.5)
    for i in range(55,64):
        p=makePicture("pic"+str(i)+".jpg")
        fade(p)
        wait(0.1)
    overlay()
    
        





