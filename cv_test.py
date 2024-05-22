import cv2 as cv
import numpy as np

screen_width = 1450
screen_height = 900
img = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
radius=100
axes = (radius,radius)
angle=0;
startAngle=180;
endAngle=360;
center=(500,500)
color=255, 255, 255

img = cv.ellipse(img, center, axes, angle, startAngle, endAngle, color, 5, cv.LINE_AA)
cv.imshow("Display window", img)
cv.waitKey(0)

# cv.ellipse(ui_img, center_mw, axes, -90, 90, yellow_color, 4, cv.LINE_AA)
# cv.ellipse(ui_img, center_mw, axes, 180, 360, yellow_color, 4, cv.LINE_AA)