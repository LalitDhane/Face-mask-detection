import cv2 as cv

# 0 is for webcam  
capture = cv.VideoCapture(0)


while True:
	#read a frame of a video
    ret, frame = capture.read()
    #show that frame
    cv.imshow("Video", frame)
    #to get out of a loop 
    if cv.waitKey(20) & 0xFF == ord("q"):
        break

        
capture.release()
cv.destroyAllWindows()


# final year project 