import numpy as np
import cv2

# Capturing video through webcam to real-time input
webcam = cv2.VideoCapture(0)
  
# Start a while loop to run
while(1):
      
    # Reading the video from the webcam in image frames
    _, imageFrame = webcam.read()

    # Convert the imageFrame in BGR(RGB color space) to HSV
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
  
    # Blue color (surgical mask) and define mask
    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
    
    # White color (surgical mask) and define mask
    white_lower = np.array([150, 150,150], np.uint8)
    white_upper = np.array([255,255,255], np.uint8)
    white_mask = cv2.inRange(hsvFrame, white_lower, white_upper)

    # Black color (surgical mask) and define mask
    black_lower = np.array([0, 0,0 ], np.uint8)
    black_upper = np.array([50,50,50], np.uint8)
    black_mask = cv2.inRange(hsvFrame, black_lower, black_upper)

    # Morphological Transform, Dilation for each color and bitwise_and operator
    # between imageFrame and mask determines to detect only that particular color
    kernal = np.ones((5, 5), "uint8")
      
    # For blue color
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = blue_mask)
     
    # Creating contour to track blue color
    contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 1500):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)
              
            cv2.putText(imageFrame, "Surgical mask (sky blue)", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))  
            
    # For white color
    black_mask = cv2.dilate(black_mask, kernal)
    res_white = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = white_mask)
     
    # Creating contour to track white color
    contours, hierarchy = cv2.findContours(white_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 1500):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)
              
            cv2.putText(imageFrame, "KN95 mask (white)", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))  
            
    # For black color
    black_mask = cv2.dilate(black_mask, kernal)
    res_black = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = black_mask)
     
    # Creating contour to track black color
    contours, hierarchy = cv2.findContours(black_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 1500):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)
              
            cv2.putText(imageFrame, "Surgical mask (black)", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))
              
    # Finally
    cv2.imshow("Mask Color Detection in Real-TIme", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

