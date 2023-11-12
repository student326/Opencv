import cv2 

path = input ('Enter the path of your Image ')
tpy = input ("Enter the type of your Image Grayscale and Color ")

if tpy == "Grayscale":
    img = cv2.imread(path, 0)
    img = cv2.resize(img, (720 , 720))
    cv2.imshow('Grayscale_img',img)

if tpy == "Color"  :
    img = cv2.imread(path, -1)
    img = cv2.resize(img, (720 , 720))
    cv2.imshow('Color_img',img)

a = cv2.waitKey(0)

if a == ord("s"):
    save = input ("Enter the path where do you want to save the image with filename.jpg or .png ")
    cv2.imwrite(save,img)

else:
    cv2.destroyAllWindows()     