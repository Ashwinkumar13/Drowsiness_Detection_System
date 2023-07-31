import cv2
import dlib
import numpy as np
import ibmiotf.application
import ibmiotf.device
import time
import pygame

# Set up IBM Watson IoT platform credentials
organization = "9gkeuo"
deviceType = "drowsydetect"
deviceId = "21122022"
authMethod = "token"
authToken = "14102108"

# Set up IBM Watson IoT platform client
options = {"org": organization,
           "type": deviceType,
           "id": deviceId,
           "auth-method": authMethod,
           "auth-token": authToken}
client = ibmiotf.device.Client(options)
client.connect()

def eye_aspect_ratio(eye):
    # Calculate the Euclidean distances between the vertical eye landmarks
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])

    # Calculate the Euclidean distance between the horizontal eye landmarks
    C = np.linalg.norm(eye[0] - eye[3])

    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    return ear


# Initialize face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:/Users/Balaji/Downloads/shape_predictor_68_face_landmarks.dat")

# Initialize constants
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 48
COUNTER = 0
ALARM_ON = False

# Initialize pygame for alarm sound
pygame.mixer.init()
sound = pygame.mixer.Sound("C:/Users/Balaji/Downloads/oversimplified-alarm-clock-113180.mp3")

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert to grayscale and detect faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    # Loop over face detections
    for rect in rects:
        # Detect landmarks and extract eye regions
        shape = predictor(gray, rect)
        leftEye = np.array([(shape.part(36).x, shape.part(36).y),
                            (shape.part(37).x, shape.part(37).y),
                            (shape.part(38).x, shape.part(38).y),
                            (shape.part(39).x, shape.part(39).y),
                            (shape.part(40).x, shape.part(40).y),
                            (shape.part(41).x, shape.part(41).y)], np.int32)
        rightEye = np.array([(shape.part(42).x, shape.part(42).y),
                             (shape.part(43).x, shape.part(43).y),
                             (shape.part(44).x, shape.part(44).y),
                             (shape.part(45).x, shape.part(45).y),
                             (shape.part(46).x, shape.part(46).y),
                             (shape.part(47).x, shape.part(47).y)], np.int32)
        
        # Calculate eye aspect ratio and check for drowsiness
    
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0
        if ear < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                if not ALARM_ON:
                    ALARM_ON = True
                    print("Drowsiness detected")
                    client.publishEvent("alert", "json", {"drowsiness": "true"})
                    # Play alarm sound
                    sound.play()
            else :
                    ALARM_ON = False
                    client.publishEvent("awake", "json", {"drowsiness": "false"})
        else:
            COUNTER = 0
            ALARM_ON = False
            # Stop alarm sound
            sound.stop()

    # Show live feed with overlay
  
        cv2.putText(frame, f"EAR: {ear:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
        cv2.imshow("Drowsiness Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
