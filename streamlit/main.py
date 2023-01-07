import cv2 
import streamlit as st
import numpy as np 
from procesado_en_vivo import procesado_vivo
import pickle
import os
import pygame

# Asocia cada nota musical con un archivo de audio
notas = {
    'do': 'do.mp3',
    're': 're.mp3',
    'mi': 'mi.mp3',
    'fa': 'fa.mp3',
    'sol': 'sol.mp3',
    'la': 'la.mp3',
    'si': 'si.mp3',
    'dodo':'dodo.mp3'
}

# Inicializa pygame
pygame.init()

# Reproduce el archivo de audio correspondiente a la nota musical dada
separator = os.path.sep
path_act = os.path.dirname(os.path.abspath(__file__))
dir = separator.join(path_act.split(separator)[:-1])

with open(f'{dir}/model/modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)


st.title("PIANO MUSICAL")
FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(0)


run = st.checkbox('Comenzar reconocimiento de nota musical')

last_note = "none"

while run:
    # Verifica si run sigue siendo True
        # Realiza el procesamiento de la imagen y reproduce la nota
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

    # Si la nueva nota es diferente a la última, la nota suena
    if letter != last_note:
        last_note = letter
        # Detiene la reproducción de música
        pygame.mixer.music.stop()
     # Reproduce el archivo de audio correspondiente a la nota musical 
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.putText(frame, letter, position, font, 
                            fontScale, color, thickness, cv2.LINE_AA)
        FRAME_WINDOW.image(frame)
        pygame.mixer.music.load(notas[letter])
        pygame.mixer.music.play(1)  # reproduce el archivo de audio una vez
    else:
        # Si la nueva nota es igual a la última, no reproduce el archivo de audio
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.putText(frame, letter, position, font, 
                            fontScale, color, thickness, cv2.LINE_AA)
        FRAME_WINDOW.image(frame)
else:
    st.write("You have exited the app")
    cam.release()
    cv2.destroyAllWindows()