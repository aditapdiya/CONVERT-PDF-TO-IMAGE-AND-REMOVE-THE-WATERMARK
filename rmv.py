import cv2
import numpy as np
from pdf2jpg import pdf2jpg
def sort():
    inputpath = r"INSERT THE PATHH OF FILE"
    outputpath = r" OUTPUT PATH FILE NAME"
    result = pdf2jpg.convert_pdf2jpg(inputpath,outputpath, pages="ALL")
    rem()


def rem():
 for i in range( 0, 21):

    img = cv2.imread("IMAGE PATH ")

    alpha = 2.0
    beta = -170
    new = alpha * img + beta
    new = np.clip(new, 0, 255).astype(np.uint8)

    cv2.imwrite("OUTUT IMAGE SAVE PATH",new)

sort()
