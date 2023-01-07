# Detectar símbolos mediante MediaPipe y devolver una nota musical

## Este proyecto utiliza MediaPipe para detectar símbolos en un vídeo o imagen y devolver una nota musical en función del símbolo detectado. El objetivo es permitir a las personas crear música simplemente mueven sus manos o tocando una superficie con símbolos específicos.

### ¿Cómo funciona?
El proyecto utiliza MediaPipe para detectar símbolos en un vídeo o imagen en tiempo real. Una vez que se detecta un símbolo, se utiliza un algoritmo de reconocimiento de patrones para determinar qué nota musical corresponde al símbolo y se reproduce el sonido de la mencionada nota.

### ¿Cómo usar?
Para utilizar este proyecto, necesitarás:

- Una cámara compatible con MediaPipe
- Descarga el código fuente del proyecto y abre el archivo main.pd.
- Conecta tu cámara a tu ordenador.
- Haz clic en el botón "Iniciar" para comenzar a detectar símbolos.
- Colocate frente a la cámara para que pueda detectar los símbolos que hagas.

Ejemplo
Para saber a qué notas musicales representan cada símbolo:

DO: 1 (mostrando dedo índice)
RE: 2 (mostrando los dedos índice y corazón)
MI: 3 (mostrando los dedos índice, corazón y anular)
FA: 4 (mostraremos los dedos índice, corazón, anular y meñique)
SOL: 5 (mostraremos los 5 dedos)
LA: 1 (mostraremos el dedo pulgar)
SI: 2 (mostraremos los dedos pulgar e índice)
DODO: 3 (mostraremos los dedos pulgar, índice y corazón)

Recursos adicionales
Para obtener más información sobre cómo usar MediaPipe y PureData, consulta la siguiente documentación:

Guía de MediaPipe

Limitaciones conocidas
Actualmente, sólo se admiten ocho símbolos diferentes.
La detección de símbolos puede ser inexacta en algunos casos.
