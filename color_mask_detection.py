import cv2                          #liberia vision por comp
import matplotlib.pyplot as lt      #libria graficos matematicos
import numpy as pn                  #numerical python, arreglos matrices, matematica en general
# %matplotlib inline

def process_frame(frame, bounds):
    lower_bound, upper_bound = bounds
    frame = frame.copy()            #se define el proceso de deteccion por frames
    mask = cv2.inRange(frame, lower_bound, upper_bound)
    return mask

file_name = "sample_video.mp4"
cap = cv2.VideoCapture(file_name)
print("Total number of frames:", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
cap.set(cv2.CAP_PROP_POS_FRAMES, 50)
ret, frame = cap.read()
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,20))
if ret:
    ax1.imshow(frame)
    ax2.imshow(process_frame(frame, (np.array([150, 150,150 ]), np.array([255,255,255]))), cmap='gray') #se configura a detectar color blanco y negro em ,ascarillas
    ax3.imshow(process_frame(frame, (np.array([0, 0,0 ]), np.array([50,50,50]))), cmap='gray')
cap.release()

cap = cv2.VideoCapture("sample_video.mp4")
white_bounds = (np.array([150, 150,150 ]), np.array([255,255,255]))
black_bounds = (np.array([0, 0,0 ]), np.array([50,50,50]))

while(cap.isOpened()):
      
    # Capture the video frame
    # by frame
    ret, frame = cap.read()
  
    # Display the resulting frame
    if ret:
        cv2.imshow('Original Frame', frame)
        cv2.imshow('White Mask', process_frame(frame,  white_bounds))
        cv2.imshow('Black Mask', process_frame(frame,  black_bounds))
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

plt.imshow(process_frame(frame), cmap='gray')

frame[frame < [10,10,10]]

