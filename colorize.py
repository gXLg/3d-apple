import cv2
import numpy as np

W, H = 480, 360
eyes = 30
black = np.uint8([0, 0, 0])

cap = cv2.VideoCapture("./original.mp4")

bg = cv2.imread("./backgrounds/fields.jpg")
h, w, l = bg.shape
y = h // 2 - H // 2
x = w // 2 - W // 2
background = bg[y:y + H, x:x + W - eyes]

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, 30, ((W - eyes) * 2, H), 1)

print("start")
i = 0
while cap.isOpened():
  i += 1
  ret, frame = cap.read()
  if not ret: break
  print("frame", i, "video", i // 30, "seconds")

  left = background.copy()
  np.putmask(left, frame[:, eyes:] < 128, black)
  right = background.copy()
  np.putmask(right, frame[:, :-eyes] < 128, black)

  pic = np.concatenate((left, right), axis = 1)
  out.write(pic)

cap.release()
out.release()