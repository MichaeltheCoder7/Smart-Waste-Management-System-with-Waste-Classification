import time

import torch
import numpy as np
from torchvision import models, transforms
from torchvision.models.quantization import MobileNet_V3_Large_QuantizedWeights

import cv2
from PIL import Image

# read from the classes file
#with open("classes.txt") as f:
#    idx2label = eval(f.read())

torch.backends.quantized.engine = 'qnnpack'

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)
cap.set(cv2.CAP_PROP_FPS, 36)

preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

weights = MobileNet_V3_Large_QuantizedWeights.DEFAULT
net = models.quantization.mobilenet_v3_large(weights=weights, quantize=True)

# jit model to take it from ~20fps to ~30fps
net = torch.jit.script(net)

started = time.time()
last_logged = time.time()
frame_count = 0

with torch.no_grad():
    while True:
        # read frame
        ret, image = cap.read()
        if not ret:
           raise RuntimeError("failed to read frame")
        
        # Show frame
        cv2.imshow('frame', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Print the probabilities of the classes
        #print() # new line
        #top = list(enumerate(output[0].softmax(dim=0)))
        #top.sort(key=lambda x: x[1], reverse=True)
        #for idx, val in top[:10]:
        #    print(f"{val.item()*100:.2f}% {idx2label[idx]}")

        # Print the classification and log model performance
        # Do this when at least 1 sec passes
        frame_count += 1
        now = time.time()
        if now - last_logged > 1:
            # convert opencv output from BGR to RGB
            image = image[:, :, [2, 1, 0]]
            permuted = image

            # preprocess
            input_tensor = preprocess(image)

            # create a mini-batch as expected by the model
            input_batch = input_tensor.unsqueeze(0)

            # run model
            output = net(input_batch)
            print() # new line
            prediction = output.squeeze(0).softmax(0)
            class_id = prediction.argmax().item()
            score = prediction[class_id].item()
            category_name = weights.meta["categories"][class_id]
            print(f"{category_name}: {100 * score}%")

            # Print FPS
            print(f"{frame_count / (now-last_logged)} fps")
            last_logged = now
            frame_count = 0

cap.release()
cv2.destroyAllWindows()
