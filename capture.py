import cv2
import os

cam_port = 0
cam = cv2.VideoCapture(cam_port)

inp = input('Enter person name')

directory = "Training_images"
if not os.path.exists(directory):
    os.makedirs(directory)

while True:
    result, image = cam.read()
    cv2.imshow(inp, image)
    
    if cv2.waitKey(0):
        image_path = os.path.join(directory, f"{inp}.png")
        cv2.imwrite(image_path, image)
        print(f"Image saved at {image_path}")
        break

cam.release()
cv2.destroyAllWindows()