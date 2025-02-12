import cv2
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def create_dataset(img,id,img_id):
        cv2.imwrite("data_train/pic." + str(id) + '.' + str(img_id) + '.jpg',img)

def draw_boundary(img,classifier,scaleFactor,minNeighbors,color):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
        coords = []
        for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                cv2.putText(img,'Face',(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
                coords=[x,y,w,h]
        return img,coords

def detect(img,faceCascade,img_id):
        img,coords=draw_boundary(img,faceCascade,1.1,10,(0,0,255))

        # Create id person
        if len(coords)== 4:
                # id = 1 # Ta
                # id = 2 # Kob
                # id = 3 # Toei
                id = 4 # Emily Sie
                result = img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
                create_dataset(result,id,img_id)
        return img

img_id=0
# id = 1 # Ta
# cap = cv2.VideoCapture("./data_test/Ta.mp4")
# id = 2 # Kob
# cap = cv2.VideoCapture("./data_test/Kob.mp4")
# id = 3 # Toei
# cap = cv2.VideoCapture("./data_test/Toei.mp4")
# id = 4 # Emily Sie.mp4
cap = cv2.VideoCapture("./data_test/Emily_Sie.mp4")

while (True):
        ret,frame = cap.read()
        frame=detect(frame,faceCascade,img_id)
        cv2.imshow('frame',frame)
        img_id+=1
        if(cv2.waitKey(1) & 0xFF== ord('q')):
            break

cap.release()
cv2.destroyAllWindows()
