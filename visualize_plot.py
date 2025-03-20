import os
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True)

# Specify the exact folder containing your images
DATA_DIR = './data/0'  # Adjust this path to your specific folder

# Check if the directory exists
if not os.path.isdir(DATA_DIR):
    print(f"Error: {DATA_DIR} is not a valid directory")
    exit()

# Get all files in the directory
image_files = [f for f in os.listdir(DATA_DIR) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Process each image
for img_file in image_files:
    img_path = os.path.join(DATA_DIR, img_file)
    
    # Read and process the image
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(img_rgb)
    
    # Visualize the image
    plt.figure(figsize=(8, 8))
    plt.imshow(img_rgb)
    
    # Draw hand landmarks if detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                img_rgb,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )
    
    plt.title(f"Image: {img_file}")
plt.show()