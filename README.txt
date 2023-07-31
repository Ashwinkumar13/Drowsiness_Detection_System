# Drowsiness_Detection_System
An IoT based solution to detect the drowsiness level of a person . 


PROJECT REPORT 
1. INTRODUCTION
1.1 Project Overview
The system for detecting driver drowsiness in real-time and preventing accidents combines various physiological and behavioral indicators to accurately assess the driver's drowsiness level. These indicators include eye movement, head pose, and facial expressions, which are continuously monitored to identify patterns associated with drowsiness.
Eye Movement: The system tracks the driver's eye movements using specialized cameras or sensors. It analyzes factors such as blink rate, eye closure duration, and eye gaze patterns. Slow or irregular blinking, prolonged eye closures, and instances of microsleep (brief episodes of unintended sleep) can indicate drowsiness.
Head Pose: The system also observes the driver's head pose and movements. It uses cameras or sensors to track head position and orientation. A drooping or nodding head, as well as sudden jerks or head tilts, may suggest drowsiness.
Facial Expressions: By analyzing the driver's facial expressions, the system can identify specific signs of drowsiness. It looks for indicators such as drooping eyelids, yawning, or changes in facial muscle tone. These expressions can provide additional insights into the driver's level of alertness.
The system continuously analyzes and combines data from these physiological and behavioral indicators to determine the driver's drowsiness level. It uses machine learning algorithms to establish baseline patterns for each individual driver and compare real-time data against these baselines. This individualized approach helps to account for variations in drowsiness indicators across different people.
To ensure the system's accuracy, extensive training and validation are conducted using large datasets that include diverse driving scenarios, lighting conditions, and weather conditions. This allows the system to adapt and perform reliably across different environments.
When the system detects that the driver's drowsiness level is increasing and poses a potential risk, it provides timely alerts. These alerts can be in the form of visual, auditory, or haptic cues, designed to grab the driver's attention without causing distraction or panic. The nature and intensity of the alert can be customized based on the severity of drowsiness.
The ultimate purpose of this system is to prevent accidents caused by drowsy driving. By accurately detecting and addressing driver drowsiness in real-time, it aims to increase driver safety, reduce the number of accidents, and potentially save lives.



2. IDEATION & PROPOSED SOLUTION
2.1 Problem Statement Definition
The aim of this project is to develop a real-time drowsiness detection system for drivers that accurately determines the level of drowsiness and alerts the driver to prevent potential accidents. The system will utilize a combination of physiological and behavioral indicators, including eye movement, head pose, and facial expressions, to assess the driver's drowsiness level. It should be capable of distinguishing between normal and abnormal driving behavior to avoid false alarms. The system must function effectively in various lighting conditions and be capable of operating under different weather conditions. The ultimate goal is to enhance driver safety and reduce the number of accidents caused by drowsy driving.


3. REQUIREMENT ANALYSIS
3.1 Functional requirement
Real-time Drowsiness Detection: The system should continuously monitor the driver's physiological and behavioral indicators, such as eye movement, head pose, and facial expressions, to detect drowsiness in real-time.
Drowsiness Level Determination: The system should accurately analyze the collected data to determine the level of drowsiness on a scale, indicating whether the driver is alert, mildly drowsy, or severely drowsy.

Alert Mechanism: When the system detects a high level of drowsiness, it should promptly alert the driver to take necessary actions. This can be achieved through visual alerts (e.g., blinking lights), auditory alerts (e.g., sound alarms), or haptic alerts (e.g., vibrations).

False Alarm Prevention: The system should be able to differentiate between normal driving behavior and actual drowsiness to avoid unnecessary or false alarms. It should consider factors such as time of day, road conditions, and driver-specific patterns to make accurate judgments.

Lighting and Weather Adaptability: The system should be designed to function effectively in various lighting conditions, including low light or bright sunlight, as well as adapt to different weather conditions, such as rain, fog, or snow.

User-Friendly Interface: The system should have a user-friendly interface that displays the driver's drowsiness level and provides clear alerts. The interface should be easy to understand and operate without causing distraction or confusion for the driver.

Data Logging and Analysis: The system should log the collected data, including physiological and behavioral indicators, for further analysis and evaluation. This can be useful for identifying patterns, improving the system's performance, and providing insights into the driver's drowsiness patterns over time.

Integration with Vehicle Systems: The drowsiness detection system should be designed for integration with existing vehicle systems, such as onboard computers or infotainment systems, to provide seamless functionality and enable easy installation in different vehicle models.

System Reliability and Stability: The system should be reliable and stable, capable of running continuously without experiencing frequent crashes or malfunctions. It should undergo thorough testing and quality assurance processes to ensure its robustness and reliability.

Privacy and Data Security: The system should adhere to privacy regulations and ensure the security of collected data. Driver data should be anonymized, encrypted, and stored securely to protect driver privacy and prevent unauthorized access.

Calibration and Personalization: The system should allow for calibration and personalization to adapt to individual driver characteristics, such as baseline behavior and physiological variations, for enhanced accuracy and reliability.

System Compatibility: The system should be designed to be compatible with a wide range of vehicles, including cars, trucks, and buses, to promote widespread adoption and maximize its impact in reducing drowsy driving accidents.


3.2 Non-Functional requirements
Performance: The drowsiness detection system should provide real-time monitoring and analysis with minimal latency. It should be capable of processing data quickly and accurately to ensure timely alerts and responses.
Accuracy: The system should strive for a high level of accuracy in detecting drowsiness levels, minimizing false positives and false negatives. It should undergo rigorous testing to validate its performance and calibration.
Robustness: The system should be able to handle variations in environmental conditions, such as different lighting and weather conditions, without compromising its performance. It should be resilient to external factors that may impact its functionality.
Usability: The system should have an intuitive and user-friendly interface that is easy to navigate and understand. It should be designed with driver safety in mind, ensuring that interactions with the system do not cause distraction or compromise attention on the road.
Reliability: The system should operate consistently and reliably without frequent failures or errors. It should be capable of recovering from failures gracefully and resume normal operation without manual intervention.
Scalability: The system should be scalable to accommodate different vehicle models and sizes. It should be able to handle increased data processing demands as more sensors and inputs are added to support future enhancements or upgrades.
Maintainability: The system should be designed with modular components and well-documented code to facilitate easy maintenance and updates. It should support future improvements, bug fixes, and compatibility with new technologies.
Data Privacy and Security: The system should adhere to privacy regulations and ensure the secure handling of driver data. Data transmission and storage should be encrypted, and access to sensitive information should be strictly controlled to prevent unauthorized access or breaches.
Integration: The system should be compatible and easily integratable with existing vehicle systems, such as CAN bus or vehicle control units, for seamless operation and minimal disruption to the vehicle's functionality.
Power Efficiency: The system should be designed to minimize power consumption to avoid draining the vehicle's battery. It should employ efficient algorithms and utilize hardware components that are optimized for low power usage.
Compliance: The system should comply with relevant industry standards, regulations, and safety requirements for automotive systems. It should undergo appropriate testing and certification processes to ensure compliance and adherence to legal and regulatory frameworks.
Adaptability: The system should be adaptable to evolving technologies and advancements in drowsiness detection methodologies. It should be designed with flexibility to incorporate new features or upgrades without requiring significant system overhaul.

4. PROJECT DESIGN

4.2 Solution & Technical Architecture
Solution Architecture:
The drowsiness detection system can be designed using a combination of hardware and software components. Here is a high-level overview of the solution architecture:
➢ Sensors: Various sensors are used to capture the driver's physiological and behavioral indicators. This may include eye trackers, head pose sensors, and facial expression analysis tools. These sensors collect real-time data, which serves as input for the drowsiness detection system.
➢ Data Acquisition: The acquired data from the sensors is processed and transmitted to the central processing unit (CPU) for further analysis. Data acquisition techniques, such as analog-to-digital conversion, are employed to convert the sensor data into a digital format that can be processed by the system.
➢ Data Preprocessing: The raw data is preprocessed to remove noise, normalize signals, and enhance the quality of the data. Preprocessing techniques may involve filtering, signal conditioning, or feature extraction to prepare the data for subsequent analysis.
➢ Drowsiness Detection Algorithm: The preprocessed data is analyzed using a drowsiness detection algorithm. This algorithm utilizes machine learning techniques, such as deep learning models or pattern recognition algorithms, to extract meaningful features from the data and determine the driver's drowsiness level. The algorithm should be trained on a labeled dataset to enable accurate classification.
➢ Alert Mechanism: Based on the output of the drowsiness detection algorithm, an alert mechanism is triggered when a high level of drowsiness is detected. This can include visual alerts (e.g., blinking lights on the dashboard), auditory alerts (e.g., sound alarms), or haptic alerts (e.g., vibrating steering wheel). The alerts are designed to grab the driver's attention and prompt them to take necessary actions to prevent accidents.
User Interface: A user-friendly interface is provided to display the driver's drowsiness level and provide interaction options. The interface can be integrated into the vehicle's infotainment system or displayed on a dedicated screen. It should present information in a clear and concise manner to avoid distractions while driving.
Technical Architecture:
➢ Hardware Components: The hardware components include sensors (e.g., eye trackers, head pose sensors), microcontrollers or embedded systems to interface with the sensors, and communication modules for data transmission. These components are responsible for capturing and transmitting data to the central processing unit.
➢ Central Processing Unit (CPU): The CPU serves as the core processing unit of the system. It receives the sensor data, performs data preprocessing, executes the drowsiness detection algorithm, and triggers the alert mechanism. The CPU can be a high-performance processor capable of real-time data processing and analysis.
➢ Software Modules: The software modules include drivers or interfaces to interact with the hardware components, data preprocessing algorithms, the drowsiness detection algorithm, and the alert mechanism. These modules are implemented using programming languages such as Python, C++, or Java.
➢ Integration with Vehicle Systems: The drowsiness detection system needs to integrate with existing vehicle systems. This may involve integrating with the vehicle's onboard computer, infotainment system, or CAN bus. APIs or communication protocols like Bluetooth or Wi-Fi can be used for seamless integration and data exchange.
➢ Data Storage and Management: Collected data can be stored in a database or a cloud storage solution for further analysis, system improvement, and compliance with privacy regulations. Data security measures, such as encryption and access controls, should be implemented to protect sensitive driver information.
➢ System Monitoring and Maintenance: The architecture should include mechanisms for system monitoring, error handling, and logging. This allows for real-time monitoring of system performance, identification of potential issues, and maintenance activities, such as software updates and bug fixes.
➢ Scalability and Performance: The architecture should be designed to handle large-scale deployments and accommodate a growing number


5. CODING & SOLUTIONING
CODE EXPLANATION - NODE RED
The code provided appears to be a configuration file for a Node-RED flow. Here are the features identified in the code:
➢ IBM Watson IoT Platform Integration: The code includes an IBM Watson IoT node (ibmiot in) that is used to connect to the IBM Watson IoT Platform. It enables communication with IoT devices and the exchange of events and commands.
➢ Debug Node: There is a debug node that allows you to inspect the message payload during runtime for debugging purposes. It can be used to view and analyze the data flowing through the flow.
➢ Function Node: A function node is used to define custom JavaScript code logic. In this case, it receives a message payload and performs a conditional check. Depending on the value of the payload, it sets a corresponding message payload for the output.
➢ UI Text Node: The ui_text node is used to display text on the Node-RED Dashboard. It receives the message payload from the previous function node and displays it as dynamic text on the dashboard.
➢ Node-RED Dashboard: The code includes configuration for the Node-RED Dashboard. It defines the appearance and settings of the dashboard, such as the theme, site name, and layout.
These features collectively form a flow that integrates with the IBM Watson IoT Platform, processes data using custom JavaScript logic, and presents the results on a Node-RED Dashboard.

CODE EXPLANATION - PYTHON
➢ Importing librariesThe necessary libraries are imported, including cv2 for computer vision operations, dlib for face detection and landmark prediction, numpy for numerical operations, ibmiotf for IBM Watson IoT Platform integration, time for time-related operations, and pygame for playing audio.
➢ IBM Watson IoT Platform Setup:
◼ The code sets up the credentials and connection options for the IBM Watson IoT Platform.
◼ The organization, device type, device ID, authentication method, and authentication token are provided.
◼ An options dictionary is created with the configuration details.
➢ IBM Watson IoT Platform Client Connection:
◼ An IBM Watson IoT Platform client is created using the provided options.
◼ The client is connected to the IBM Watson IoT Platform.
➢ Eye Aspect Ratio Calculation:
◼ The eye_aspect_ratio function is defined, which calculates the eye aspect ratio based on the given eye landmarks.
◼ The function uses the Euclidean distances between the eye landmarks to compute the eye aspect ratio.
➢ Initialization:
◼ The code initializes the face detector and landmark predictor using the dlib library.
◼ Constants such as EYE_AR_THRESH (eye aspect ratio threshold) and EYE_AR_CONSEC_FRAMES (number of consecutive frames for drowsiness detection) are defined.
◼ Variables like COUNTER (counts consecutive frames with low eye aspect ratio), and ALARM_ON (tracks if the alarm is already on) are initialized.
◼ Pygame is initialized to play the alarm sound.
➢ Video Capture and Processing Loop:
◼ The code starts capturing frames from the video source (webcam).
◼ The captured frame is converted to grayscale for face detection and landmark prediction.
◼ The detector is used to detect faces in the grayscale frame.
◼ For each detected face, the landmarks are predicted using the predictor.
◼ The eye regions are extracted based on the predicted landmarks.
◼ The eye aspect ratio is calculated using the eye_aspect_ratio function.
◼ If the eye aspect ratio is below the threshold, the COUNTER is incremented.
◼ If the COUNTER exceeds the consecutive frames threshold, it indicates drowsiness. The alarm is activated, and a message is published to the IBM Watson IoT Platform.
◼ If the eye aspect ratio is above the threshold, the COUNTER is reset, and the alarm is turned off.
◼ The eye aspect ratio is displayed on the frame.
◼ The processed frame is displayed in a window.
◼ The loop continues until the user presses 'q' to quit.
◼ Once the loop ends, the video capture is released, and the windows are closed.

FEATURES OF NODE RED
Video Capture: The code uses OpenCV (cv2) to capture video frames from the default webcam. It continuously processes each frame to detect drowsiness.
Face Detection: It utilizes the dlib library to perform face detection in the captured frames. The get_frontal_face_detector() function is used to create a face detector object, which is then applied to the grayscale frame to detect faces.
Landmark Detection: After detecting a face, the code uses a pre-trained shape predictor from dlib (shape_predictor_68_face_landmarks.dat) to identify the specific landmarks on the face, particularly the eyes. The shape.predictor() function is used to detect landmarks for each face detected.
Eye Region Extraction: Using the detected landmarks, the code extracts the regions of interest (ROI) corresponding to the left and right eyes. These regions will be used to calculate the eye aspect ratio.
Eye Aspect Ratio (EAR) Calculation: The eye_aspect_ratio() function calculates the eye aspect ratio based on the coordinates of the eye landmarks. EAR is a measure of eye openness and is determined by the ratio of the vertical distance between the upper and lower eye landmarks to the horizontal distance between the inner and outer eye corners. It provides an indication of whether the eyes are closed or open.
Drowsiness Detection: The calculated eye aspect ratio is compared against a threshold value (EYE_AR_THRESH) to determine if the eyes are sufficiently closed, indicating drowsiness. If the average eye aspect ratio falls below the threshold for a certain number of consecutive frames (EYE_AR_CONSEC_FRAMES), an alarm is triggered.
Alarm and Sound: The code uses the pygame library to play an alarm sound when drowsiness is detected. It initializes the pygame mixer and loads an alarm sound file. The alarm sound is played when the drowsiness condition is met and is stopped when the eyes are open again.
IBM Watson IoT Platform Integration: The code connects to the IBM Watson IoT platform using the provided credentials and options. It publishes events related to drowsiness detection, sending messages indicating whether drowsiness is detected or not.
Visualization: The code overlays the calculated eye aspect ratio value on the video frame and displays it in a window. It also shows the live video feed with the overlay.
These features collectively enable the code to detect drowsiness by monitoring the eye aspect ratio and triggering an alarm when drowsiness is detected, while also integrating with the IBM Watson IoT platform for event reporting.

AMES (number of consecutive frames for drowsiness detection).
Consecutive Frame Counting: The code tracks the number of consecutive frames in which the eye aspect ratio is below the threshold to determine drowsiness.
Grayscale Conversion: The code converts the captured frames to grayscale before performing face detection and landmark prediction.
Real-time Display: The processed frames, eye aspect ratio, and alarm status are displayed in real-time in a separate window.
Keyboard Input Handling: The code listens for keyboard input and exits the loop when the user presses 'q' to quit.



