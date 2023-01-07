# Detectar símbolos mediante MediaPipe y devolver una nota musical

## Este proyecto utiliza MediaPipe para detectar símbolos en un vídeo o imagen y devolver una nota musical en función del símbolo detectado. El objetivo es permitir a las personas crear música simplemente moviendo sus manos.

### ¿Cómo funciona?
El proyecto utiliza el flujo de trabajo de detección de objetos de MediaPipe para detectar símbolos en tiempo real a través de la cámara de un dispositivo. Cada símbolo está asociado a una nota musical específica, que se reproduce por audio.

El proyecto está escrito en Python y utiliza las siguientes bibliotecas:

- mediapipe --> 0.9.0.1 
- opencv .......... 4.7.0.68
- numpy ........... 1.24.1
- pandas .......... 1.5.2
- streamlit ....... 1.16.0


### ¿Cómo usar?
Para utilizar este proyecto, necesitarás:

- Una cámara compatible con MediaPipe
- Descarga el código fuente del proyecto y abre el archivo main.py de la carpeta streamlit.
- Conecta tu cámara a tu ordenador.
- Ejecuta el programa desde la terminal, con un "streamlit run main.py" para comenzar a detectar símbolos.
- Colocate frente a la cámara para que pueda detectar los símbolos que hagas y te devuelva las notas musicales.

Ejemplo:
Para saber a qué notas musicales representan cada símbolo:

- DO--> 1 (mostrando dedo índice) 
- RE:   2 (mostrando los dedos índice y corazón)
- MI:   3 (mostrando los dedos índice, corazón y anular)
- FA:   4 (mostraremos los dedos índice, corazón, anular y meñique)
- SOL:  5 (mostraremos los 5 dedos)
- LA:   1 (mostraremos el dedo pulgar)
- SI:   2 (mostraremos los dedos pulgar e índice)
- DODO: 3 (mostraremos los dedos pulgar, índice y corazón)

Recursos adicionales
Para obtener más información sobre cómo usar MediaPipe y PureData, consulta la siguiente documentación:

Guía de MediaPipe

Limitaciones conocidas
Actualmente, sólo se admiten ocho símbolos diferentes.
La detección de símbolos puede ser inexacta en algunos casos.

## Authors

- [@SoniaSancho84](https://github.com/SoniaSancho84/FinalProjectMusic)
