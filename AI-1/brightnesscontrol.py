import cv2
import mediapipe as mp
import math
import os  # Used to call macOS brightness CLI tool

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Webcam setup
cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    if not success:
        print("Sorry, couldn't fetch frame.")
        break

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            landmarks = []
            h, w, _ = image.shape
            for lm in hand_landmarks.landmark:
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append((cx, cy))

            if len(landmarks) >= 9:
                x1, y1 = landmarks[4]  # Thumb tip
                x2, y2 = landmarks[8]  # Index tip

                length = math.hypot(x2 - x1, y2 - y1)

                brightness = int(max(0, min(100, (length - 30) * 2)))
                brightness_value = max(0.0, min(1.0, brightness / 100))

                # ✅ macOS brightness setting
                os.system(f"brightness {brightness_value}")

                # Draw visuals
                cv2.circle(image, (x1, y1), 7, (255, 0, 0), cv2.FILLED)
                cv2.circle(image, (x2, y2), 7, (255, 0, 0), cv2.FILLED)
                cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
                cv2.putText(image, f"Brightness: {brightness}", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)

            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gesture Brightness Control", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
