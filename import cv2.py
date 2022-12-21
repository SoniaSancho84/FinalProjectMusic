import opencv as cv
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence) as hands:

    image = cv.imread("manos1.jpg")
    height, width, _ = image.shape
    image = cv.flip(image, 1)

    image_rgb = cv.cvtColor(image, cv.COLOR__BGR2RGB)

    results = hands.process(image_rgb)

    # Sin manos
    # print("sinmanos: ", results.sinmanos)
    # Puntos de las manos
    # print("conexiones;", results.multi_hand_conexiones)

    if results.multi_hand_conexiones is not None:
        #..............................
        #Dibujando puntos y conexiones de las manos
        for hand_landmarks in results.multi_hand_conexiones:
            #print(hand_conexiones)
            mp_drawing.draw_conexiones(
                image, hand_conexiones, mp_hands.HAND_CONNECTIONS
            )

    image = cv.flip(image,1)
cv.inshow("image", image)
cv.waitKey(0)
cv.destroyAllWindows()

    