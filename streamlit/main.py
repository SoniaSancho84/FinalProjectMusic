import cv2 
import streamlit as st
import numpy as np 
from procesado_en_vivo import procesado_vivo
import pickle
import os

separator = os.path.sep
path_act = os.path.dirname(os.path.abspath(__file__))
dir = separator.join(path_act.split(separator)[:-1])

with open(f'{dir}/model/modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)


st.title("PIANO MUSICAL")
run = st.checkbox('Comenzar reconocimiento de nota musical')
FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(0)

while run:
    ret, frame = cam.read()
    data = procesado_vivo(frame)
    data = np.array(data)
    y_pred = modelo.predict(data.reshape(-1,63))
    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (50, 100)
    fontScale = 3
    color = (255, 255, 255)
    thickness = 5
    letter = str(y_pred[0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.putText(frame, letter, position, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    FRAME_WINDOW.image(frame)
else: 
    st.write("You have exited the app")
    cam.release()
    cv2.destroyAllWindows()