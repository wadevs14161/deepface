from deepface import DeepFace
import os
from time import time
from pprint import pprint


if __name__ == '__main__':
    # face_analysis = DeepFace.analyze(
    #     "database/dome-1.jpg",
    #     actions=["emotion"])
    # pprint(face_analysis[0])
    
    angry, disgust, fear, happy, neutral, sad, surprise = 0, 0, 0, 0, 0, 0, 0

    start = time()

    for image in os.listdir("database"):
        face_analysis = DeepFace.analyze(
            f"database/{image}",
            actions=["emotion"])
        angry += face_analysis[0]["emotion"]["angry"]
        disgust += face_analysis[0]["emotion"]["disgust"]
        fear += face_analysis[0]["emotion"]["fear"]
        happy += face_analysis[0]["emotion"]["happy"]
        neutral += face_analysis[0]["emotion"]["neutral"]
        sad += face_analysis[0]["emotion"]["sad"]
        surprise += face_analysis[0]["emotion"]["surprise"]

    print("Angry:", angry)
    print("Disgusted:", disgust)
    print("Fearful:", fear)
    print("Happy:", happy)
    print("Neutral:", neutral)
    print("Sad:", sad)
    print("Surprised:", surprise)

    end = time()
    print("Time taken:", end - start)
