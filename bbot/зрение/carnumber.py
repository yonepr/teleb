import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
hands =  mp.solutions.hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break

    success, image = cap.read()
    image = cv2.flip(image, 1)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(imageRGB)


    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h,w,c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

            draw.draw_landmarks(image,handLms,mp.solutions.hands.HAND_CONNECTIONS )





    cv2.imshow("Hand detector", image)
