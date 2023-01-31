import cv2
import numpy as np
for i in range( 0, 21):

    img = cv2.imread("F:\\office\\Python-Remove-Watermark-master\\output\\image1.png\\CW-01.pdf_dir\\"+str(i)+"_CW-01.pdf.jpg")

    alpha = 2.0
    beta = -170
    new = alpha * img + beta
    new = np.clip(new, 0, 255).astype(np.uint8)

    cv2.imwrite("F:\\office\\Python-Remove-Watermark-master\\output\\cleaned"+str(i)+".png",new)