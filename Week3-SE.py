
#Will make color vibe darker/deeper, and enlarge image by factor of 1.5
#Image window will show original image along with recolored/enlarged image
#As such, size of new grid is 2.5 x original width (to accommodate both)
#Height of new grid is the height of the enlarged image

from image import*

def LighterPixel(oldPixel):
    newRed = max(oldPixel.getRed()-15, 0)
    newGreen = max(oldPixel.getGreen()-20, 0)
    newBlue = max(oldPixel.getBlue()-35, 0)
    newPixel = Pixel(newRed, newGreen, newBlue)
    return newPixel

def pixelMapper(fileImage, rgbFunction):
    width = fileImage.getWidth()
    height = fileImage.getHeight()
    newIm = EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            oldPixel = fileImage.getPixel(col, row)
            newPixel = rgbFunction(oldPixel)
            newIm.setPixel(col, row, newPixel)
    return newIm

def AlteredImage(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    myImageWindow = ImageWin(width * 2.5, height * 1.5, "1.5x original")
    ReColored = pixelMapper(oldImage, LighterPixel)
    #ReColored.draw(myImageWindow)
    #ReColored.save("deepti-colorchange.jpg")
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(round(width * 1.5), round(height * 1.5))
    for row in range(newIm.getHeight()):
        for col in range(newIm.getWidth()):
            originalCol = col // 1.5
            originalRow = row // 1.5
            oldPixel = ReColored.getPixel(originalCol, originalRow)
            newIm.setPixel(col, row, oldPixel)
    newIm.setPosition(width + 1, -1)
    newIm.save("deepti_Altered")
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()
    return newIm

def main():
    deeps = "Deepti_LIB.jpg"
    AlteredImage(deeps)
main()
