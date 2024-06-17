import cv2
import os
from math import ceil

# Read the video
cam = cv2.VideoCapture('test.mp4')

# Create a directory to store the frames if it doesn't exist
try:
    if not os.path.exists('frames'):
        os.makedirs('frames')
except OSError:
    print('Error: Creating directory of frames')

# Get the frames
currentframe = 0

frame_per_second = ceil(cam.get(cv2.CAP_PROP_FPS))

while True:
    ret, frame = cam.read()

    if ret:
        name = './frames/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        
        if currentframe % (frame_per_second) == 0:
            cv2.imwrite(name, frame)

        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()


