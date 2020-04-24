from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
import cv2
import math
# draw each face separately
def draw_faces(frame, result_list,frameno):
	# load the image
	
	data = frame
	faces = result_list
	
	# plot each face as a subplot
	for i in range(len(result_list)):
		# get coordinates
		x1, y1, width, height = result_list[i]['box']
		x2, y2 = x1 + width, y1 + height
		# define subplot
		pyplot.subplot(1, len(result_list), i+1)
		pyplot.axis('off')
		# plot face
		#pyplot.imshow(data[y1:y2, x1:x2])
		#cv2.imwrite('face'+str([i])+'.jpg',data[y1:y2, x1:x2])
		cv2.imwrite('./faces_in_frames/face_'+str([frameno])+'_'+str([i])+'.jpg',cv2.cvtColor(data[y1:y2, x1:x2],cv2.COLOR_RGB2BGR))
		



def extract_to_folder(videoFile):
        count=0
        imagesFolder ="./frames"
        cap = cv2.VideoCapture(videoFile)
        frameRate = cap.get(cv2.CAP_PROP_FPS) #frame rate
        print("video framerate is : ",frameRate)
        desiredfps=1
        print("Desired framerate extracted", desiredfps)
        desiredfps=frameRate#ye part theek karna hai math se (cap.get(cv2.CAP_PROP_FRAME_COUNT)//frameRate)*desiredfps
        x=1
        while(cap.isOpened()):
            frameId = cap.get(1) #current frame number
            print(frameId)
            ret, frame = cap.read()
            if (ret != True):
                break
            if (frameId % desiredfps == 0):
                filename = imagesFolder + "/image_" +  str(x) + ".jpg"
                x+=1
                # create the detector, using default weights
                detector = MTCNN()
                # detect faces in the image
                faces = detector.detect_faces(frame)
                # display faces on the original image
                count= count + len(faces)
                draw_faces(frame, faces,x)

                

        cap.release()
        print ("Done!")
        print(count)
        return count
