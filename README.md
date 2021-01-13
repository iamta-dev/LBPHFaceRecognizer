# Face Recognition
face-recognition using opencv LBPHFaceRecognizer

### AI ตรวจจับเเละจดจำใบหน้า

### Package Install

```
 $ pip install opencv-python==3.4.2.17 
 $ pip install numpy
 $ pip install pillow
 $ pip install opencv-contrib-python
```

### Training model

Edit file CreateDataSet.py Create id person
```
# Create id person
if len(coords)== 4:
        # id = 1 # Ta
        # id = 2 # Kob
        # id = 3 # Toei
        id = 4 # Emily Sie
        result = img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
        create_dataset(result,id,img_id)
return img
```

compile
```
 $ python CreateDataSet.py
 ... output file data_train/pic.id.img_id.jpg
 $ python Train.py
```

### Test - AI  
Edit file FaceRecognition.py Add id person
```
# Add id person
if id == 1:
    name = "Ta " + " {0}%".format(round(100 - con))
if id == 2:
    name = "Kob " + " {0}%".format(round(100 - con))
if id == 3:
    name = "Toei " + " {0}%".format(round(100 - con))
if id == 4:
    name = "Emily Sie " + " {0}%".format(round(100 - con))
cv2.putText(img,name,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
```

compile
```
$ python FaceRecognition.py
```
<p align="center"><img width="200" src="/markdown/Emily_Sie-test.png" /> </p>
<p align="center"><img width="200" src="/markdown/app/Kob-test.png" /> </p>
<p align="center"><img width="200" src="/markdown/app/Ta-test.png" /> </p>
<p align="center"><img width="200" src="/markdown/app/Team1-test.png" /> </p>
