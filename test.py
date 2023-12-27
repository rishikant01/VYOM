import cv2

# Check if cv2.face submodule is present
if hasattr(cv2, 'face'):
    print("cv2.face is available.")
else:
    print("cv2.face is not available.")
