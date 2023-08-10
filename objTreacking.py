import cv2
import numpy as np
from object_detection import ObjectDetection
import math 


od = ObjectDetection()

capture = cv2.VideoCapture("/Users/ramahalharbi/Desktop/projectComputerVision/source_code/los_angeles.mp4")

count = 0
center_prev_freame = []
tracking_objects = {}
track_id = 0

while True:
    ret, frame = capture.read()
    count += 1
    if not ret:
       break
    # point current freame 
    center_current_freame = []
     
    (class_ids, scores, boxes)= od.detect(frame)

    for box in boxes:
      (x, y, w, h) = box
      centerX = int((x + x + w )/2)
      centerY = int((y + y + h )/2)
      center_current_freame.append((centerX,centerY))
      # print("fream number  ", count, " ", x, y, w, h)
      
      # cv2.circle(frame, (centerX,centerY), 5, (255,0,0), -1)
      cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2) 

    # only at the beginning we compare previous and curr frame
    if count <= 2:
      for pt in center_current_freame:
          for pt2 in center_prev_freame:
            distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1] )

            if distance < 20:
              tracking_objects[track_id] = pt
              track_id += 1

    else: 
        tracking_objects_copy = tracking_objects.copy()
        center_current_freame_copy = center_current_freame.copy()

        for object_id, pt2 in tracking_objects_copy.items():
            is_obj_exists = False 
            for pt in center_current_freame_copy:
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1] )

                # update obj position
                if distance < 20:
                   tracking_objects[object_id] = pt
                   is_obj_exists = True
                   if pt in center_current_freame:
                      center_current_freame.remove(pt)
                      continue   
                
            # remove ID    
            if not is_obj_exists:
               tracking_objects.pop(object_id)

        # add new id found 
        for pt in center_current_freame: 
            tracking_objects[track_id] = pt 
            track_id += 1 

    for object_id, pt in tracking_objects.items():
        cv2.circle(frame, pt, 5, (255,0,0), -1)
        cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (255, 0, 0), 2)

         
    print("track object")         
    print(tracking_objects)

    print("tracking obj ")         
    print(tracking_objects) 
       
    print("current frame left point ")
    print(center_current_freame)


    cv2. imshow("Fream", frame)

    # copy of the points
    center_prev_freame = center_current_freame.copy()

    key = cv2.waitKey(0)
    if key == 27:
        break

capture.release()
capture.destroyAllWindows()