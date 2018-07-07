import cv2
import numpy as np
import os

from os import walk

for dirpath, dirnames, filenames in walk ("/home/galip/Desktop/uva/"):
 print(filenames)

 for f in filenames:
  cap = cv2.VideoCapture(dirpath + f)
  length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

  #I need 3 frames. lastframe is the middle frame in all video and second frame is between the middle frame and first frame.
  firstFrameIndex = 0
  lastFrameIndex = int(length / 2)
  secondFrameIndex = int(lastFrameIndex / 2)

  try:
    if not os.path.exists('data'):
        os.makedirs('data')
  except OSError:
    print ('Error: Creating directory of data')

  cap.set(1,firstFrameIndex)
  ret, frame = cap.read()

  currentFrame = firstFrameIndex
  name = '/home/galip/Desktop/data/' + f.partition(".")[0] + '_' + str(currentFrame) + '.jpg'
  cv2.imwrite(name,frame)

  cap.set(1,secondFrameIndex)
  ret, frame = cap.read()

  currentFrame = secondFrameIndex
  name = '/home/galip/Desktop/data/' + f.partition(".")[0] + '_' + str(currentFrame) + '.jpg'
  cv2.imwrite(name, frame)

  #lastFrame
  cap.set(1,lastFrameIndex)
  ret, frame = cap.read()

  currentFrame = lastFrameIndex
  name = '/home/galip/Desktop/data/' + f.partition(".")[0] + '_' + str(currentFrame) + '.jpg'
  cv2.imwrite(name, frame)

  print(f)

  # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
