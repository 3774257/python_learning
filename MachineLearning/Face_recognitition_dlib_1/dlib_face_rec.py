import sys, os, dlib, glob, re
import numpy as np
from skimage import io


img_path = 'jiangxin.2.jpg'
# 1.加载正脸检测器

detector = dlib.get_frontal_face_detector()

# 2.加载人脸关键点检测器
predictor_path = 'shape_predictor_68_face_landmarks.dat'
sp = dlib.shape_predictor(predictor_path)

# 3. 加载人脸识别模型
face_rec_model_path = 'dlib_face_recognition_resnet_model_v1.dat'
facerec = dlib.face_recognition_model_v1(face_rec_model_path)

# 候选人脸描述子list
descriptors = []
# 候选人名单
candidate = []

faces_folder_path = 'conditate_faces'
for file in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
    print("Processing file:{}".format(file))
    candidate.append(re.search(r'\\(.*).(.*?).jpg', file).group(1)[:-1])
    img = io.imread(file)
    # 1.人脸检测
    dets = detector(img, 1)
    # print("Number of faces detected: {}".format(len(dets)))
    for k, d in enumerate(dets):
        shape = sp(img, d)

        face_descriptor = facerec.compute_face_descriptor(img, shape)

        v = np.array(face_descriptor)
        descriptors.append(v)


img = io.imread(img_path)
dets = detector(img, 1)

dist = []

for k, d in enumerate(dets):
    shape = sp(img, d)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    d_test = np.array(face_descriptor)

    # 计算欧式距离

    for i in descriptors:
        dist_ = np.linalg.norm(i-d_test)
        dist.append(dist_)

c_d = dict(zip(candidate, dist))

cd_sorted = sorted(c_d.items(), key=lambda d:d[1])
print("The person is: ", cd_sorted[0][0])
# dlib.hit_enter_to_continue()


