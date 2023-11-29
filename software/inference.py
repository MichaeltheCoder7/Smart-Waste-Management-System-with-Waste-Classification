import time

import torch
import torch.nn as nn
import numpy as np
from torchvision import models, transforms
from torchvision.models.quantization import MobileNet_V3_Large_QuantizedWeights

import cv2
from PIL import Image

torch.backends.quantized.engine = 'qnnpack'

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)
cap.set(cv2.CAP_PROP_FPS, 36)

preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

weights = models.MobileNet_V3_Large_Weights.DEFAULT
#net = models.quantization.mobilenet_v3_large(weights=weights, quantize=True)
device = torch.device('cpu') # Map it to CPU since Pi4 does not have GPU
model = models.quantization.mobilenet_v3_large(weights=weights, quantizated=True)

# Modify the number of classes from 1000 to 12 to match the dataset
model.classifier[3] = nn.Linear(model.classifier[3].in_features, 12)
model.load_state_dict(torch.load('quantized_mobilenet_v3_large.pth', map_location=device))
model.eval()

# jit model to take it from ~20fps to ~30fps
model = torch.jit.script(model)

# Labels
labels = ["battery", "biological", "brown-glass", "cardboard", "clothes", "green-glass", "metal", "paper", "plastic", "shoes", "trash", "white-glass"]
label_map = {"battery":"None", "biological":"Compost", "brown-glass":"Recycle", "cardboard":"Recycle", "clothes":"Recycle", "green-glass":"Recycle", "metal":"Recycle", "paper":"Recycle", "plastic":"Recycle", "shoes":"Landfill", "trash":"Landfill", "white-glass":"Recycle"}

#started = time.time()
#last_logged = time.time()
#frame_count = 0

with torch.no_grad():
    while True:
        # read frame
        ret, image = cap.read()
        if not ret:
           raise RuntimeError("failed to read frame")

        image_copy = image # Make a copy of the frame
        
        # convert opencv output from BGR to RGB
        image = image[:, :, [2, 1, 0]]

        # preprocess
        input_tensor = preprocess(image)

        # create a mini-batch as expected by the model
        input_batch = input_tensor.unsqueeze(0)

        # run model
        output = model(input_batch)

        # Print the classification and log model performance
        print() # new line
        prediction = output.squeeze(0).softmax(0)
        class_id = prediction.argmax().item()
        score = prediction[class_id].item()
        #category_name = weights.meta["categories"][class_id]
        #_, predicted_labels = torch.max(output, 1)
        category_name = label_map[labels[class_id]]

        print(f"{category_name}: {100 * score}%")

        #frame_count += 1
        #now = time.time()
        #if now - last_logged > 1:
            # Print FPS
        #    print(f"{frame_count / (now-last_logged)} fps")
        #    last_logged = now
        #    frame_count = 0

        # Show frame
        cv2.putText(image_copy, f"{category_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', image_copy)
        # press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the opencv resources
cap.release()
cv2.destroyAllWindows()
