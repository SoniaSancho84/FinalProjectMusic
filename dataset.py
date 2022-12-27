import numpy as np
import cv2 as cv
from pathlib import Path

def crear_nota():
    nota = input('Qué nota te gustaría agregar? -> ')
    Path('dataset/'+nota).mkdir(parents=True, exist_ok=True)
    webcam = cv.VideoCapture(0)
    i = 0    
    while True:
       
        _, frame = webcam.read()
        i+= 1
        if i % 5==0:
            cv.imwrite(f'dataset/{nota}/{str(i)}.png',frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q') or i > 500:
            break
    webcam.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
   crear_nota()