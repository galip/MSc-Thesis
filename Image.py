import time

start = time.time()

import argparse
import cv2
import itertools
import os
from os import walk

import numpy as np
np.set_printoptions(precision=2)

import openface

print("startttt")
count = 0

fileDir = os.path.dirname(os.path.realpath(__file__))
modelDir = os.path.join(fileDir, '..', 'models')
dlibModelDir = os.path.join(modelDir, 'dlib')
openfaceModelDir = os.path.join(modelDir, 'openface')

print(fileDir)
print(modelDir)
print(dlibModelDir)
print(openfaceModelDir)

parser = argparse.ArgumentParser()

parser.add_argument('--imgs', type=str, nargs='+', help="Input images.")
parser.add_argument('--dlibFacePredictor', type=str, help="Path to dlib's face predictor.",
                    default=os.path.join(dlibModelDir, "shape_predictor_68_face_landmarks.dat"))
parser.add_argument('--networkModel', type=str, help="Path to Torch network model.",
                    default=os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'))
parser.add_argument('--imgDim', type=int,
                    help="Default image dimension.", default=96)
parser.add_argument('--verbose', action='store_true')

args = parser.parse_args()
print("args : ", args)

if args.verbose:
    print("Argument parsing and loading libraries took {} seconds.".format(
        time.time() - start))

start = time.time()
align = openface.AlignDlib(args.dlibFacePredictor)

net = openface.TorchNeuralNet(args.networkModel, args.imgDim)
if args.verbose:
    print("Loading the dlib and OpenFace models took {} seconds.".format(
        time.time() - start))


def getRep(imgPath, fileName):

    if args.verbose:
        print("Processing {}.".format(imgPath))
    bgrImg = cv2.imread(imgPath)

    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    if args.verbose:
        print("  + Original size: {}".format(rgbImg.shape))

    start = time.time()
    bb = align.getLargestFaceBoundingBox(rgbImg)

    #get facial landmark, save.
    #print("bb : ", bb)
    name = '/home/galip/Desktop/landmark/' + fileName + '.txt'
    file = open(name, 'a')
    file.writelines(str(bb))
    file.close()


    if bb is None:
        raise Exception("Unable to find a face: {}".format(imgPath))
    if args.verbose:
        print("  + Face detection took {} seconds.".format(time.time() - start))

    start = time.time()
    alignedFace = align.align(args.imgDim, rgbImg, bb,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    if alignedFace is None:
        raise Exception("Unable to align image: {}".format(imgPath))
    if args.verbose:
        print("  + Face alignment took {} seconds.".format(time.time() - start))

    # get alignedFace, save.
    name = '/home/galip/Desktop/alignedface/' + fileName + '.png'
    cv2.imwrite(name, alignedFace)

    start = time.time()
    rep = net.forward(alignedFace)

    #get repvector, create .txt files for each and save the vector
    name = '/home/galip/Desktop/repvector/' + fileName + '.txt'
    file = open(name, 'a')
    file.writelines(str(rep))
    file.close()

for dirpath, dirnames, filenames in walk("/home/galip/Desktop/test1/"):
    print(filenames)
    print(dirpath)

    for f in filenames:
     getRep(dirpath + f, f.partition(".")[0])
     print(f.partition(".")[0])
     count += 1
     print(count)
