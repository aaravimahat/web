import cv2
import numpy as np

def filter(image,filter_type):
    filtered_image=image.copy()

    if filter_type=="red_tint":
        filtered_image[:,:,1]=0
        filtered_image[:,:,0]=0

    elif filter_type=="green_tint":
        filtered_image[:,:,2]=0
        filtered_image[:,:,0]=0

    elif filter_type=="blue_tint":
        filtered_image[:,:,1]=0
        filtered_image[:,:,2]=0

    elif filter_type=="sobel":
        g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        sobelx=cv2.Sobel(g,cv2.CV_64F,1,0,ksize=3)
        sobely=cv2.Sobel(g,cv2.CV_64F,0,1,ksize=3)
        combined_sobel=cv2.bitwise_or(sobelx.astype('uint8'),sobely.astype('uint8'))
        filtered_image=cv2.cvtColor(combined_sobel,cv2.COLOR_GRAY2BGR)
    elif filter_type=="canny":
        g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        edge=cv2.Canny(g,150,200)
        filtered_image=cv2.cvtColor(edge,cv2.COLOR_GRAY2BGR)


    return filtered_image

image_path="b.jpg"
image=cv2.imread(image_path)

if image is None:
    print("image not found")

else:
    filter_type="orignal"

    print("press these keys to apply filter")
    print("r-red tint")
    print("g-green tint")
    print("b-blue tint")
    print("s-sobel detection")
    print("c-canny detection")
    print("q-quit")

    while True:
        filtered_image=filter(image,filter_type)
        cv2.imshow("filtered image", filtered_image)

        key=cv2.waitKey(0) & 0xFF

        if key==ord("r"):
            filter_type="red_tint"

        elif key==ord("g"):
            filter_type="green_tint"
        elif key==ord("b"):
            filter_type="blue_tint"
        elif key==ord("s"):
            filter_type="sobel"
        elif key==ord("c"):
            filter_type="canny"

        elif key==ord("q"):
            filter_type="exiting"

        else:
            print("invalid key")

cv2.destroyAllWindows()

        


        








    