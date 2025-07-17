# 레이블 감지 코드

# Object Detection
# 객체 감지
# AWS -> Rekognition -> 레이블 감지

import boto3  # AWS와 데이터를 주고 받기 위한 라이브러리!
# 주의할 점 !! pip install boto3 <- python 2버전 이하로 설치!

def detect_labels_local_file(photo):

    client = boto3.client('rekognition')
   
    with open(photo, 'rb') as image:   # photo
        response = client.detect_labels(Image={'Bytes': image.read()})

    result = []

    # Dog : 85.22%

    for i in response["Labels"]:
        name = i["Name"]
        confidence = i["Confidence"]

        result.append(f"{name}  : {confidence:.2f}%")

    r = "<br/>".join(map(str, result))

    # "Dog : 85.22% <br/> Cat : 11.22%
    return r 

def compare_faces(sourceFile, targetFile):

    client = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=0,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        similarity = (faceMatch['Similarity'])


    imageSource.close()
    imageTarget.close()
    return f"두 얼굴의 일치율 : {similarity:.2f}%"