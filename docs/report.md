# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract
Our project develops a low-cost, energy-efficient waste classification system using a Raspberry Pi 4 and deep learning algorithms. Aimed at improving waste management, the system classifies items into categories like compost, landfill, and recycle using a modified CNN model, such as MobileNetV3. Our embedded system is designed for public and personal use and features a camera for real-time classification, a user-friendly interface, and a motion sensor for power saving. The system aims to enhance recycling rates and reduce pollution by educating users on proper disposal. Key challenges include balancing cost and technological efficiency and developing an effective feedback mechanism. Success will be measured by classification accuracy, user experience, and power consumption. The project draws on current research and utilizes resources like Kaggle’s waste datasets and MobileNetV3. Its success could significantly impact waste management processes and environmental awareness.

# 1. Introduction

This section should cover the following items:

* Motivation & Objective: What are you trying to do and why? (plain English without jargon)
* State of the Art & Its Limitations: How is it done today, and what are the limits of current practice?
* Novelty & Rationale: What is new in your approach and why do you think it will be successful?
* Potential Impact: If the project is successful, what difference will it make, both technically and broadly?
* Challenges: What are the challenges and risks?
* Requirements for Success: What skills and resources are necessary to perform the project?
* Metrics of Success: What are metrics by which you would check for success?

# 2. Related Work

# 3. Technical Approach
![alt text](https://github.com/MichaeltheCoder7/Smart-Waste-Management-System-with-Waste-Classification/blob/main/docs/image2.png?raw=true)

## Hardware components
Raspberry Pi 4 serves as the central processing unit for the system, handling the computations needed for image processing and waste classification.
Pi Camera v2 is integrated with the Raspberry Pi, the camera captures real-time images of the waste items for classification. I2C LCD1602 display Screen displays the classification results to the user, including the category of waste and additional sorting suggestions.
Infrared Motion Sensor is used to detect human motion, triggering the activation of the camera and the deep learning model only when needed, which aids in power saving.

## Real-time image/video processing
Utilizing the OpenCV library, the system captures and reads frames from the Pi Camera. These frames are resized to the required dimensions for the waste classification model. The frame rate was set to the highest feasible level (approximately 36 FPS) to facilitate real-time processing. As OpenCV processes images in BGR format, a conversion to RGB format was implemented for the inference task.

## Waste Classification Model
For the waste classification task, we opted for the pre-trained quantized MobileNet V3 Large model, chosen for its suitability with embedded platforms and robust performance. Originally trained on the extensive ImageNet dataset, which includes 14 million images across 1,000 classes, this model provided a solid foundation for our application.

To tailor the model to our specific needs, we utilized the Pytorch framework to perform transfer learning on dedicated waste datasets. We sourced our data primarily from this Kaggle dataset: 'Garbage Classification' (12 classes). To counteract the large number of clothes and shoes images, we reduced the number to about 2000 and 1000 respectively. Due to a lack of ‘trash’ category data and ‘biological’ data, we also added images from other Kaggle datasets ('Waste Classification data’, ‘Garbage Image Dataset’, and ‘Garbage Classification’). These were combined to create a balanced dataset that accurately represents the categories of compost, recycle, and landfill, totaling approximately 14,000 images.

The transfer learning process involved dividing this dataset into training and validation subsets. To preserve the integrity and performance of the original MobileNet V3 Large model, we froze all the pre-trained weights during training. This approach ensures that the nuanced features learned from the expansive ImageNet dataset are retained in our adapted model.

For the training process, we employed the Adam optimizer with a learning rate set at 0.001, striking a balance between efficient learning and avoiding overshooting the minima in the loss landscape. The model was trained over 10 epochs, a duration found to be sufficient for achieving high accuracy without overfitting.

In an effort to optimize the model for real-time execution on the Raspberry Pi 4, we employed Just-In-Time (JIT) compilation on the model. This technique significantly enhances the inference speed, allowing us to achieve higher frames per second (FPS) during real-time classification. This optimization was crucial for the seamless and responsive operation of our waste classification system in a live environment.

## Power Saving
To efficiently manage power consumption, our system employs a strategic power-saving mechanism centered around the use of an Infrared Motion Sensor. This sensor is crucial in controlling the activation of the system's high-energy components: the camera and the deep learning model. In its default state, the system remains in a low-power sleep mode, significantly reducing CPU usage and conserving energy. Activation occurs only when the Infrared Motion Sensor detects human motion, triggering the camera and the waste classification model into operation. A red LED serves as an indicator of this active state, providing visual feedback and assisting in monitoring the system’s operational status.

Post-activation, the system is designed to revert to sleep mode after a predetermined interval of 10-15 seconds. This duration is optimized to balance the need for user interaction and classification accuracy with the overarching goal of minimizing energy consumption. By swiftly transitioning back to sleep mode, where the LED is also turned off, the system ensures that power usage is kept to a minimum, making it more sustainable and practical for long-term deployment in various settings. This approach effectively balances the system's functional requirements with the critical need for energy efficiency.


# 4. Evaluation and Results
## Transfer learning metrics
The implementation of transfer learning in our project yielded highly encouraging results. After undergoing 10 epochs of training, the system achieved a validation accuracy of 91.30%. This level of accuracy is indicative of the model's robust ability to accurately classify waste into the correct categories, demonstrating its effectiveness for real-world applications. Furthermore, the model attained a low validation loss of 0.2831, which underscores the efficiency of the learning process and the model's precision in making predictions. These metrics collectively affirm the success of the transfer learning approach in adapting the MobileNet V3 Large model to the specific requirements of our waste classification system.

![alt text](https://github.com/MichaeltheCoder7/Smart-Waste-Management-System-with-Waste-Classification/blob/main/docs/image1.png?raw=true)

## Real-time Results
In our practical testing, which involved approximately 50 distinct waste items, the system demonstrated a promising accuracy rate of around 77% in correctly classifying items into recycle, landfill, and compost categories. While this accuracy is commendable, particularly for a real-world application, we identified several factors that may contribute to the classification errors observed. These include varying lighting conditions, the distance of the waste item from the camera, background noise, camera quality, and potential imbalances in the training dataset. Addressing these factors could further improve the system's accuracy and will be a focus for future enhancements.

Alongside the classification system, other hardware components like the LCD screen and the Infrared motion sensor performed effectively. The LCD screen provided clear and useful feedback to the users, while the motion sensor reliably activated the system upon detecting human presence. These elements contributed to a responsive and user-friendly interface, enhancing the overall user experience. The seamless integration and functionality of these components are crucial to the system's practicality, ensuring it is both accessible and efficient for everyday use.

## Power Consumption Estimate
In evaluating the power consumption of our system, we faced time constraints that limited our ability to conduct detailed measurements. As a practical workaround, we assessed the system's energy usage indirectly by monitoring the CPU usage on the Raspberry Pi. This was accomplished using the "top" command, a standard tool for task management in Unix-based systems.

Our observations indicated that the CPU usage was close to 0% when the system was in sleep mode, signifying minimal power consumption during periods of inactivity. During activation, which occurs when the system is processing images and classifying waste, the CPU usage increased to approximately 70%. This contrast in CPU usage between the active and idle states provides a rough estimate of the system's power consumption patterns. While it's not an exact measure of power usage in watts, it gives a useful indication of the relative energy efficiency of the system during its different operational phases. Going forward, a more precise measurement of power consumption could offer deeper insights into the system's energy efficiency and potential areas for improvement.


# 5. Discussion and Conclusions
In summary, our waste classification system represents an innovative solution designed to meet the needs of both individual users and the broader public, all while prioritizing energy efficiency and affordability. With a user-friendly interface that offers practical waste disposal tips, the system is accessible to a wide audience, promoting proper waste management practices.

One of the system's standout features is its effective power management strategy, which conserves energy by activating high-power components only when human motion is detected, seamlessly transitioning back to sleep mode when not in use. While achieving a commendable 77% accuracy in waste classification, we recognize the potential for improvement. Future enhancements could include refining the waste classification model to address errors, expanding the training dataset for increased accuracy and adaptability, and incorporating advanced sensory capabilities to further enhance system responsiveness and accuracy. By pursuing these avenues, our system has the potential to significantly contribute to waste management and environmental sustainability efforts, offering an impactful and practical solution to address the pressing global issue of waste disposal.


# 6. References
