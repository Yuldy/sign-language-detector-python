# import os

# import cv2


# DATA_DIR = './data'
# if not os.path.exists(DATA_DIR):
#     os.makedirs(DATA_DIR)

# number_of_classes = 3
# dataset_size = 100
# # Slight change let's do 0 or 1 to access Camera for laptop
# cap = cv2.VideoCapture(1)
# for j in range(number_of_classes):
#     if not os.path.exists(os.path.join(DATA_DIR, str(j))):
#         os.makedirs(os.path.join(DATA_DIR, str(j)))

#     print('Collecting data for class {}'.format(j))

#     done = False
#     while True:
#         ret, frame = cap.read()
#         cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
#                     cv2.LINE_AA)
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(25) == ord('q'):
#             break

#     counter = 0
#     while counter < dataset_size:
#         ret, frame = cap.read()
#         cv2.imshow('frame', frame)
#         cv2.waitKey(25)
#         cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

#         counter += 1

# cap.release()
# cv2.destroyAllWindows()



import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Move hands back and forth
#number_of_classes = 3
number_of_classes = 26

# can also modify dataset size
dataset_size = 100

# Change camera index if needed (0 for default, 1 for external)
cap = cv2.VideoCapture(1)  # Try 1 if 0 doesn't work


# 21 redo V baloon

# do  25 Z

# Reshoot
#classes_to_capture = [21, 25]
classes_to_capture = [25]
for j in classes_to_capture:
#for j in range(number_of_classes):

    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't read frame.")
            break  # Stop if frame capture fails

        cv2.putText(frame, 'Ready? Press "Q" to start or "ESC" to exit', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break  # Start collecting images
        elif key == 27:  # Press "ESC" to exit
            cap.release()
            cv2.destroyAllWindows()
            exit()

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't read frame.")
            break

        cv2.imshow('frame', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key to exit
            cap.release()
            cv2.destroyAllWindows()
            exit()

        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)
        counter += 1

cap.release()
cv2.destroyAllWindows()

