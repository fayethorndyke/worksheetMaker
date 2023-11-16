import fitz
from fxns import *
from PIL import Image


selection = getUserInput()

pgNum = selection[0]
probNums = selection[1, len(selection) - 1]

createPDF()

addProbs(pgNum, probNums)

print("Done.")



    
