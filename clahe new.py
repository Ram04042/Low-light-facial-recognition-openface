import cv2 
import os
import glob
import onlyvideo

imdir = './faces_in_frames'
outputfolder='./clahed'
onlyvideo.load_ram()

if not os.path.exists(outputfolder): os.mkdir(outputfolder)
images = [file for file in glob.glob('./faces_in_frames/*.jpg')]
for index,image in enumerate(images):
    img = cv2.imread(image)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
    output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    #ye dono kaam karre hai wiener ya bm3d bhi blur hi karre the tu try karke dekh
    #output = cv2.bilateralFilter(output,9,75,75)
    #output = cv2.medianBlur(output,5)
    path2 = outputfolder + "/image_" +  str(index) + ".jpg"
    match_path = onlyvideo.match_pathpack(output)
    print(match_path)
    cv2.imwrite(path2,output)


