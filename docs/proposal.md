# Project Proposal

## 1. Motivation & Objective

Waste management is a significant global problem due to the increasing amount of waste we produce and the harm it causes to the environment and human health. The world is currently facing limited availability of space for landfill sites and increasing costs for waste disposal. To help address this problem, we decided to use a Raspberry Pi 4 microprocessor to design and implement an embedded system with deep learning assistance, capable of classifying waste items using a camera into categories like compost, landfill, and recycle. The system could be placed above public waste bins or in facilities to aid and educate users about proper waste disposal, ensuring waste is correctly sorted for efficient recycling and disposal. This can lead to better resource management and reduction of environmental pollution.


## 2. State of the Art & Its Limitations

Today, waste classification typically involves manual sorting and categorization by waste management workers at recycling facilities. This process often relies on visual inspection and basic knowledge of waste types. The limitation of manual sorting is that it is time-consuming, expensive, and prone to human error. In recent years, a few companies have developed deep learning classification algorithms to help sort waste more efficiently. For example, the company AMP Robotics employs AI and robotics techniques to enhance the accuracy and efficiency of waste sorting to improve recycling rates. However, the limitation lies in the fact that these robots are designed for use in recycling facilities, making them less suitable for household or public use, and their production costs are relatively high.


## 3. Novelty & Rationale

Our embedded waste management system is designed for personal or public use and is built to operate with low power consumption and at a low cost. Our aim is to assist users in correctly sorting their waste, thereby enhancing recycling rates right from the initial phase of waste disposal. In addition, with the implementation and modification of a CNN model like MobileNetV2, we intend to achieve high accuracy. With our system, users can effortlessly classify their waste and dispose of it properly when they are unsure about which trash bin to use. Furthermore, we will customize the feedback system that can provide users with proper tips. For example, we could suggest users remove pizza from the box and place them into the correct bins. Additionally, we will record data on the frequency and types of disposed waste, offering valuable insights for extracting waste patterns and developing effective waste management strategies. We are confident in the success of our embedded system, as we employ high-accuracy deep learning algorithms for waste classification. Additionally, we prioritize user-friendly design to enhance the system’s practicality and promote user adoption, contributing to its potential success.


## 4. Potential Impact

If the project is successful, it could make a dual impact, both technically and broadly. On a technical level, the use of high-accuracy deep learning algorithms would transform the waste management processes, significantly reducing the time required for waste sorting at recycling facilities. In terms of broad impact, our embedded waste management system aims to help raise awareness of the growing environmental issues. By making recycling easier, we hope to increase recycling rates and, in turn, do our part in reducing pollution.


## 5. Challenges

There are two major challenges in this project. The first challenge is cost constraints. It is essential to minimize both power consumption and production costs. Balancing cost and technological advancements can be challenging. The second challenge is the implementation of the customized feedback system. Our goal is to provide users with valuable suggestions that can help them make the right choices, but assessing the effectiveness of these suggestions comes with its own set of challenges.


## 6. Requirements for Success

The project involves utilizing a Raspberry Pi 4, a Raspberry Pi Camera Module, and an iPhone. Knowledge and proficiency in CNN models that yield high accuracy in waste classification, as well as programming skills to adapt the code, are necessary. Additionally, creating a feedback system resembling an iPhone program demands skills in designing the software and establishing a reliable connection to the microprocessor for accurate feedback.


## 7. Metrics of Success

Firstly, the system should achieve a high level of accuracy, aiming for around 90%, to be considered successful. Secondly, prioritizing a positive user experience is crucial, and creating a user-friendly interface will greatly enhance the project’s success. Thirdly, evaluating the power consumption of the system is essential to ensure it can operate continuously for an extended period, such as several days.


## 8. Execution Plan

We divided the project into 6 steps, with each member assigned specific tasks. The task allocation is as follows:

1. Camera Integration: Connect the camera module to the embedded system board for capturing real-time images of waste items. (Minkai)

2. Waste Classification Model: Implement a CNN model like MobileNetV2, which is trained on a dataset of waste items. This dataset should include images of waste in compost, landfill, and recycle categories. (Minkai)

3. Real-time Classification: When an item is placed in front of the bin or disposal area, the camera captures the image, and the deep learning model classifies the waste. (Minkai)

4. Feedback Mechanism: Once the waste is classified, the screen will display the appropriate bin for disposal and provide users with suggestions on separating their waste into different categories if needed. (Yuhan)

5. Data Logging: Store data regarding the frequency and type of waste being disposed of. This can be useful for understanding waste patterns and planning waste management strategies. (Yuhan)

6. User Interface: Design an interface that is able to view real-time classifications, access historical data on waste classification, and modify feedback or add new categories. (Yuhan) 


## 9. Related Work

### 9.a. Papers

CleverTrash: An ML-based IoT system for waste sorting with continuous learning cycle. [1]

In this paper, the authors utilize seven different CNN algorithms, conducting a comparative analysis of their outcomes. Their primary emphasis lies in the classification of recyclable waste items such as plastic PET, cardboard, and plastic packaging. Aligning with our objectives, their aim is to educate individuals on recycling sorting to minimize sorting errors. Furthermore, they encounter a challenge similar to ours, addressing the configuration of a Pi camera with specific parameters to obtain clear images.

A smart recycling bin using waste image classification at the edge. [2]

In this paper, the authors address both accuracy and power consumption concerns. Their models achieve an impressive accuracy of approximately 96%, and they successfully reduce the power consumption of one of their systems from the previous work by about 30% to 4.7W. These aspects align with our project considerations, and we can use their findings as a valuable reference to explore effective options for low power consumption.

### 9.b. Datasets

We plan to use datasets from Kaggle: Garbage Classification (12 classes) and Waste Classification data.

### 9.c. Software

We plan to use Python and the model CNN MobileNetV2 for waste classification, and the iOS app Termius to access the command line interface of the Raspberry Pi remotely to show text feedback to users.


## 10. References

[1] Foukia, N. (2022). CleverTrash: An ML-based IoT system for waste sorting with continuous learning cycle. The Institute of Electrical and Electronics Engineers, Inc. (IEEE) Conference Proceedings. https://doi.org/10.1109/ICECET55527.2022.9872943

[2] Li, X., & Grammenos, R. (2022). A smart recycling bin using waste image classification at the edge. arXiv.org. https://arxiv.org/abs/2210.00448

[3] Bobulski, J., & Kubanek, M. (2021). Deep Learning for Plastic Waste Classification System. Applied Computational Intelligence and Soft Computing, 2021, 1–7. https://doi.org/10.1155/2021/6626948

[4] Saha, H. N., Auddy, S., Pal, S., Kumar, S., Pandey, S., Singh, R., Singh, A. K., Banerjee, S., Ghosh, D., & Saha, S. (2017). Waste management using Internet of Things (IoT). 2017 8th Annual Industrial Automation and Electromechanical Engineering Conference (IEMECON), 359–363. https://doi.org/10.1109/IEMECON.2017.8079623

[5] Garbage Classification (12 classes): https://www.kaggle.com/datasets/mostafaabla/garbage-classification

[6] Waste Classification data: https://www.kaggle.com/datasets/techsash/waste-classification-data

[7] MobileNetV2: https://keras.io/api/applications/mobilenet/

[8] Termius: Terminal & SSH client: https://apps.apple.com/us/app/termius-terminal-ssh-client/id549039908
