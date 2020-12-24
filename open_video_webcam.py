import cv2 as cv
capture = cv.VideoCapture(0)
while True:
    ret, frame = capture.read()
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF == ord("q"):
        break
capture.release()
cv.destroyAllWindows()
