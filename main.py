from PIL import Image

Mu = 20 ## we define the intensity with the 'mu' so if we set it higher it will only pick drastic changes 

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)


"""
prcessImage - colors the edges of the image and saves it to the 'result' folder
    @ARGS
        path (utf string) - the path of the original image [ default - path to sample image ]
        Mu (int) - we define the intensity with the 'mu' so if we set it higher it will only pick drastic changes [ default - 20 the optimal value ]
"""
def prcessImage( path = './sample-images/jpeg-home.jpeg', Mu = 20 ):

    ## We get the image and the load the pixels from it
    im = Image.open(path) # Can be many different formats.
    pix = im.load()

    ## Getting my image sizes
    width = im.size[0]
    height = im.size[1]

    ## Running of the image and changing the color of out picture to show predicted edges
    for x in range(1,width-1):
        for y in range(1,height-1):
            if (pix[x,y][0] - pix[x,y+1][0]) > Mu:
                pix[x,y] = BLACK
            elif pix[x,y][0] - pix[x,y+1][0] < -Mu:
                pix[x,y] = GREEN

            if pix[x,y][1] - pix[x,y+1][1] > Mu:
                pix[x,y] = BLACK
            elif pix[x,y][1] - pix[x,y+1][1] < -Mu:
                pix[x,y] = GREEN

            if pix[x,y][2] - pix[x,y+1][2] > Mu:
                pix[x,y] = BLACK
            elif pix[x,y][2] - pix[x,y+1][2] < -Mu:
                pix[x,y] = GREEN

    for y in range(1,height-1):
        for x in range(1,width-1):
            if pix[x,y][0] - pix[x+1,y][0] > Mu:
                pix[x,y] = BLACK
            elif pix[x,y][0] - pix[x+1,y][0] < -Mu:
                pix[x,y] = GREEN

            if pix[x,y][1] - pix[x+1,y][1] > Mu:
                pix[x,y] = BLACK
            elif pix[x,y][1] - pix[x+1,y][1] < -Mu:
                pix[x,y] = GREEN

            if pix[x,y][2] - pix[x+1,y][2] > Mu:
                pix[x,y] = BLACK
            elif pix[x,y][2] - pix[x+1,y][2] < -Mu:
                pix[x,y] = GREEN

    im.save('./result/result.jpg')  # Save the modified pixels as .png



'''
exit() #Exit the program so the second method is not effecting

count = 0
avarageChangeR = 0
avarageChangeG = 0
avarageChangeB = 0
avarageChange = 0
changeArrey = []

for x in range(1,width-1):
    for y in range(1,height-1):
        count += 1
        avarageChangeR +=  abs(pix[x,y][0] - pix[x,y+1][0])
        avarageChangeG +=  abs(pix[x,y][1] - pix[x,y+1][1])
        avarageChangeB +=  abs(pix[x,y][2] - pix[x,y+1][2])

for y in range(1,height-1):
    for x in range(1,width-1):
        count += 1
        avarageChangeR +=  abs(pix[x,y][0] - pix[x,y+1][0])
        avarageChangeG +=  abs(pix[x,y][1] - pix[x,y+1][1])
        avarageChangeB +=  abs(pix[x,y][2] - pix[x,y+1][2])

avarageChangeR = Mu*avarageChangeR/(2*count)
avarageChangeG = Mu*avarageChangeG/(2*count)
avarageChangeB = Mu*avarageChangeB/(2*count)

print("avarage  Change",avarageChange)

for x in range(1,width-1):
    for y in range(1,height-1):
        if abs(pix[x,y][0] - pix[x,y+1][0]) > avarageChangeR:
            changeArrey.append([x,y])
        elif abs(pix[x,y][1] - pix[x,y+1][1]) > avarageChangeG:
            changeArrey.append([x,y])
        elif abs(pix[x,y][2] - pix[x,y+1][2]) > avarageChangeB:
            changeArrey.append([x,y])

for y in range(1,height-1):
    for x in range(1,width-1):
        if abs(pix[x,y][0] - pix[x,y+1][0]) > avarageChangeR:
            changeArrey.append([x,y])
        elif abs(pix[x,y][1] - pix[x,y+1][1]) > avarageChangeG:
            changeArrey.append([x,y])
        elif abs(pix[x,y][2] - pix[x,y+1][2]) > avarageChangeB:
            changeArrey.append([x,y])

avarageChange = avarageChange/height

for pix_cord in changeArrey:
    x_cord = pix_cord[0]
    y_cord = pix_cord[1]
    pix[x_cord,y_cord] = BLACK

im.save('./result/alive_parrot.png')  # Save the modified pixels as .png
'''