# Smart Waste Management System
This is a project for UCLA ECEM202A / CSM213A.  

**Hardware Setup**  
Raspberry Pi 4  
Pi Camera v2  
I2C LCD1602 Display Screen  
Infrared Motion Sensor  

**Software Setup**  
Python3  
Pytorch  
RPi.GPIO  
numpy  
OpenCV  

**Raspberry Pi 4 settings**   
Edit the /boot/config.txt file to enable the camera:  
start_x=1 # Enables the extended features such as the camera

gpu_mem=128 # This needs to be at least 128M for the camera processing

#camera_auto_detect=1 # You need to remove the existing camera_auto_detect line

**Command to Run the Program in Software Directory**  
Python main.py
