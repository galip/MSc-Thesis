# MSc-Thesis
In this study, I will compare video based deep learning face recognition systems.
First aim is to working on Openface project which is developped by Carnegie Mellon University and licensed under the Apache 2.0 License(https://cmusatyalab.github.io/openface/). The code can be downloaded from github(https://github.com/cmusatyalab/openface).
We will have image dataset from uVa-Nemo video dataset. UvA-NEMO Smile Database (http://www.uva-nemo.org/).
The second deep learning architecture will be resnet-50 model which is trained on VGGFace2. We will compare the results with these datasets.
The third one is InsightFace architecture (https://github.com/deepinsight/insightface) and the model is LResNet100E-IR,ArcFace@ms1m-refine-v2. They used Mtcnn alignment process but we skipped this since we used dlib's alignment as it is used in the OpenFace project already.

You will find the technical details in the techNotes folder.
