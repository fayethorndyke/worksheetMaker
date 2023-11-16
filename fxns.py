import fitz
from PIL import Image

#returns True if param is num else returns False
def isNum(num):
    try:
        int(num)
        return True
    except:
        return False

#Takes in user input and formats into list of nums with pg num first and prob nums after
def getUserInput():
    output = []    
    raw = input("Enter page number then problem numbers then enter:\n")
    
    index = 0
    new = True
    tempNum = 0

    while index < len(raw):
        if isNum(raw[index]):
            if new:
                tempNum = int(raw[index])
            else:
                tempNum *= 10
                tempNum += int(raw[index])
            new = False
        else:
            if tempNum > 0:
                output.append(tempNum)
            tempNum = 0
            new = True
        index += 1
    
    if tempNum != 0:
        output.append(tempNum)
    
    return output


def captureRegion(pdfPath, pageNum, coords):
    pdfDoc = fitz.open(pdfPath)
    page = pdfDoc[pageNum - 1]
    x1, y1, x2, y2 = coords
    rect = fitz.Rect(x1, y1, x2, y2)
    pixmap = page.get_pixmap(rect = rect)
    img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
    return img

def createPDF(pdfName, probNums):
    return 0

def allLetters(input):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in input:
        if alphabet.find(letter) < 0:
            return False
    return True

def findCoords(pageNum, probNum):
    return 0

def genProbImg(pageNum, coords):
    return 0

def placeImg(pdfPath, img):
    return 0


