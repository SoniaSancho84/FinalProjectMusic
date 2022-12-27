import os
from pprint import isreadable
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands (
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:

imagen = cv2.imread
imagen=os.imagen.join("manos", "manos1.jpg")
isreadable(imagen)
height, widt, _ = imagen.shape

imagen = cv2.flip(imagen, 1)
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

results = hands.process(imagen_rgb)

# HANDEDNESS
print('Handedness:', results.multi_handedness)
# HAND LANDMARKS
print('Hand landmarks:', results.multi_hand_landmarks)


