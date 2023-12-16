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
## Motivation & Objective
Waste management is a significant global problem due to the increasing amount of waste we produce and the harm it causes to the environment and human health. The world is currently facing limited availability of space for landfill sites and increasing costs for waste disposal. To help address this problem, we decided to use a Raspberry Pi 4 microprocessor to design and implement an embedded system with deep learning assistance, capable of classifying waste items using a camera into categories like compost, landfill, and recycle. The system could be placed above public waste bins or in facilities to aid and educate users about proper waste disposal, ensuring waste is correctly sorted for efficient recycling and disposal. This can lead to better resource management and reduction of environmental pollution.

## State of the Art & Its Limitations
Today, waste classification typically involves manual sorting and categorization by waste management workers at recycling facilities. This process often relies on visual inspection and basic knowledge of waste types. The limitation of manual sorting is that it is time-consuming, expensive, and prone to human error. In recent years, a few companies have developed deep learning classification algorithms to help sort waste more efficiently. For example, the company AMP Robotics employs AI and robotics techniques to enhance the accuracy and efficiency of waste sorting to improve recycling rates. However, the limitation lies in the fact that these robots are designed for use in recycling facilities, making them less suitable for household or public use, and their production costs are relatively high.

## Novelty & Rationale
Our embedded waste management system is designed for personal or public use and is built to operate with low power consumption and at a low cost. We aim to assist users in correctly sorting their waste, thereby enhancing recycling rates right from the initial phase of waste disposal. In addition, with the implementation and modification of a CNN model like MobileNetV3, we achieved high accuracy. With our system, users can effortlessly classify their waste and dispose of it properly when they are unsure about which trash bin to use. Furthermore, we customized the feedback system that can provide users with proper tips. For example, we suggest users remove any food leftover from the box and place them into the correct bins, and empty the bottle before disposal. Additionally, we prioritize user-friendly design to enhance the system’s practicality and promote user adoption, contributing to its potential success.

## Potential Impact
The project makes a dual impact, both technically and broadly. On a technical level, the use of high-accuracy deep learning algorithms would transform the waste management processes, significantly reducing the time required for waste sorting at recycling facilities. In terms of broad impact, our embedded waste management system aims to help raise awareness of the growing environmental issues. By making recycling easier, we hope to increase recycling rates and, in turn, do our part in reducing pollution.

## Challenges
There are three major challenges in this project. The first challenge is cost constraints. It is essential to minimize both power consumption and production costs. Balancing cost and technological advancements is challenging. The second challenge is the implementation of the customized feedback system. Our goal is to provide users with valuable suggestions that can help them make the right choices, but assessing the effectiveness of these suggestions comes with its own set of challenges. The third challenge is attaining high accuracy. While we trained our CNN model using a large dataset, the real-time scenario introduces complexities due to environmental factors and camera influences. These variables pose obstacles in achieving consistently high accuracy during runtime.

## Requirements for Success
The project involves utilizing a Raspberry Pi 4, a Raspberry Pi Camera Module, an LCD Display Screen, and an Infrared Motion Sensor. Knowledge and proficiency in CNN models that yield high accuracy in waste classification, as well as programming skills to adapt the code, are necessary. Additionally, establishing a feedback system, such as setting up an LCD display and an infrared motion sensor, requires a certain level of expertise and understanding.

## Metrics of Success
Firstly, the system should achieve a high level of real-time accuracy, aiming for around 70%, to be considered successful. Secondly, prioritizing a positive user experience is crucial, and creating a user-friendly interface will greatly enhance the project’s success. Thirdly, evaluating the power consumption of the system is essential to ensure it is operating at a low cost.


# 2. Related Work
## Papers
CleverTrash: An ML-based IoT system for waste sorting with continuous learning cycle. [1]

In this paper, the authors utilize seven different CNN algorithms, conducting a comparative analysis of their outcomes. Their primary emphasis lies in the classification of recyclable waste items such as plastic PET, cardboard, and plastic packaging. Aligning with our objectives, their aim is to educate individuals on recycling sorting to minimize sorting errors. Furthermore, they encounter a challenge similar to ours, addressing the configuration of a Pi camera with specific parameters to obtain clear images.

A smart recycling bin using waste image classification at the edge. [2]

In this paper, the authors address both accuracy and power consumption concerns. Their models achieve an impressive accuracy of approximately 96%, and they successfully reduce the power consumption of one of their systems from the previous work by about 30% to 4.7W. These aspects align with our project considerations, and we can use their findings as a valuable reference to explore effective options for low power consumption.

## Datasets
We used datasets from Kaggle: Garbage Classification (12 classes) [3], Waste Classification data [4], Garbage Image Dataset [5], and Garbage Classification [6].

## Software
We employed the CNN MobileNetV3 model for waste classification and utilized Python to configure the LCD display APIs. We crafted a program to display the output classification category and provide proper suggestions to the user. Additionally, we used Python to configure the infrared motion sensor, enabling it to detect motion effectively.


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

## Feedback Mechanism
To customize our feedback system, we incorporated a 16x2 LCD display to present the results and messages. We used the I2C LCD API to facilitate communication between the display and the processor. Initially, the display shows the output classification categories (compost, recycle, landfill), accompanied by a corresponding score indicating the probability of the waste belonging to that category. This informs users about the percentage of the waste falling into a specific category.

Subsequently, based on the 12 subcategories, we offer distinctive and personalized suggestions to guide users in ensuring accurate waste disposal. Given the limited dimensions of the 16x2 display, we organized messages across two or three pages, each displayed for 2.5 seconds. This deliberate approach allows users sufficient time to fully comprehend the information. By adopting this strategy, users gain clarity on which bin to use for disposal and understand the specific actions required for correct waste disposal.

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
[1] Foukia, N. (2022). CleverTrash: An ML-based IoT system for waste sorting with continuous learning cycle. The Institute of Electrical and Electronics Engineers, Inc. (IEEE) Conference Proceedings. https://doi.org/10.1109/ICECET55527.2022.9872943

[2] Li, X., & Grammenos, R. (2022). A smart recycling bin using waste image classification at the edge. arXiv.org. https://arxiv.org/abs/2210.00448

[3] Garbage Classification (12 classes): https://www.kaggle.com/datasets/mostafaabla/garbage-classification

[4] Waste Classification data: https://www.kaggle.com/datasets/techsash/waste-classification-data

[5] Garbage Image Dataset https://www.kaggle.com/datasets/farzadnekouei/trash-type-image-dataset

[6] Garbage Classification https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification

[7] MobileNetV3: https://keras.io/api/applications/mobilenet/

[8] LCD API: https://github.com/dhylands/python_lcd/tree/master
