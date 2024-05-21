import cv2 as cv
import numpy as np
#import tkinter as tk
import json

# def opening_screen():
#     # create main window
#     root = tk.Tk()
#     root.title("Multi-Node UI")

#     # Create a label for the title
#     title_label = tk.Label(root, text="Percept: Multi-Node Interface", font=("Helvetica", 24))
#     title_label.pack(pady=20)

#     # Create a button to start the game
#     start_button = tk.Button(root, text="Run", command=visualizer)
#     start_button.pack()

#     # Create button to exit program
#     end_button = tk.Button(root, text="Exit", command=root.destroy)
#     end_button.pack()

#     # Run the GUI
#     root.mainloop()

# def update_pos():



def visualizer():
	# create window
	screen_width = 1800
	screen_height = 900
	img = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)

	position_x = 1300  				# x-coordinate of the line
	box_width = 2  					# width of the line
	white_color = 255, 255, 255  	# white color
	black_color = 0, 0, 0			# black color
	gray_color = 211, 211, 211		# gray color
	red_color = 20, 70, 220			# red color
	blue_color = 220, 100, 50		# blue color
	green_color = 100, 190, 0		# green color

	# draw rectangle to separate screen
	img = cv.rectangle(img, (0, 0), (position_x, screen_width), white_color, -1)				# main display
	img = cv.rectangle(img, (position_x, 0), (position_x+10, screen_height), gray_color, -1)	# vertical border
	img = cv.rectangle(img, (position_x+10, 295), (screen_width, 305), gray_color, -1)			# horizontal border
	img = cv.rectangle(img, (position_x+10, 595), (screen_width, 605), gray_color, -1)			# horizontal border
	img = cv.rectangle(img, (position_x+10, 0), (screen_width, 295), red_color, -1)				# top info screen
	img = cv.rectangle(img, (position_x+10, 305), (screen_width, 595), blue_color, -1)			# middle info screen
	img = cv.rectangle(img, (position_x+10, 605), (screen_width, 900), green_color, -1)			# bottom info screen

	
	# parameters of rectangle for data box
	rec_width = 163
	rec_height = 80
	font = cv.FONT_HERSHEY_SIMPLEX
	font_size = 1.1
	font_thickness = 2

	# text and data box for Frame #
	img = cv.rectangle(img, (1332, 118), (1332 + rec_width, 118 + rec_height), white_color, -1)
	img = cv.putText(img, "Frame #", (1338, 97), font, font_size, white_color, font_thickness, cv.LINE_AA)

	# text and data box for Elapsed time (ms)
	img = cv.rectangle(img, (1537, 118), (1603 + rec_width, 118 + rec_height), white_color, -1)
	img = cv.putText(img, "Runtime (ms)", (1535, 97), font, font_size, white_color, font_thickness, cv.LINE_AA)


	# Node 1 title
	img = cv.putText(img, "Node 1", (1480, 355), font, font_size+0.5, white_color, font_thickness+2, cv.LINE_AA)
	img = cv.line(img, (1480, 365), (1655, 365), white_color, 3)
	# text and data box for "Angle"
	img = cv.rectangle(img, (1372, 438), (1372 + rec_width, 438 + rec_height), white_color, -1)
	img = cv.putText(img, "Range", (1397, 420), font, font_size, white_color, font_thickness, cv.LINE_AA)
	# text and data box for "Angle"
	img = cv.rectangle(img, (1600, 438), (1600 + rec_width, 438 + rec_height), white_color, -1)
	img = cv.putText(img, "Angle", (1635, 420), font, font_size, white_color, font_thickness, cv.LINE_AA)

	# Node 1 title
	img = cv.putText(img, "Node 2", (1480, 655), font, font_size+0.5, white_color, font_thickness+2, cv.LINE_AA)
	img = cv.line(img, (1480, 665), (1663, 665), white_color, 3)
	# text and data box for "Angle"
	img = cv.rectangle(img, (1372, 738), (1372 + rec_width, 738 + rec_height), white_color, -1)
	img = cv.putText(img, "Range", (1397, 720), font, font_size, white_color, font_thickness, cv.LINE_AA)
	# text and data box for "Angle"
	img = cv.rectangle(img, (1600, 738), (1600 + rec_width, 738 + rec_height), white_color, -1)
	img = cv.putText(img, "Angle", (1635, 720), font, font_size, white_color, font_thickness, cv.LINE_AA)

	# Node 1 box
	img = cv.rectangle(img, (10, 370), (110, 470), black_color, -1)
	img = cv.putText(img, "1", (40, 440), font, font_size+1, white_color, 6, cv.LINE_AA)

	# Node 2 box
	img = cv.rectangle(img, (605, 790), (705, 890), black_color, -1)
	img = cv.putText(img, "2", (635, 860), font, font_size+1, white_color, 6, cv.LINE_AA)

	# Scale tick mark parameters
	num_ticks = 11
	tick_length = 10

	# vertical line adjacent to node 1
	line1_start = (110, 50)
	line1_end = (110, 790)
	img = cv.line(img, line1_start, line1_end, black_color, 2)
	# tick marks
	# Calculate the interval between tick marks
	interval1 = (line1_end[1] - line1_start[1]) // (num_ticks - 1)

	# bottom horizontal line
	line3_start = (110, 790)
	line3_end = (850, 790)
	img = cv.line(img, line3_start, line3_end, black_color, 2)
	# Calculate the interval between tick marks
	interval3 = (line3_end[0] - line3_start[0]) // (num_ticks - 1)

	# vertical line adjacent to node 2
	line2_start = (1200, 790)
	line2_end = (1200, 50)
	img = cv.line(img, line2_start, line2_end, black_color, 2)
	# tick marks
	# Calculate the interval between tick marks
	interval2 = (line2_end[1] - line2_start[1]) // (num_ticks - 1)

	# top horizontal line
	line4_start = (1200, 50)
	line4_end = (110, 50)
	img = cv.line(img, line4_start, line4_end, black_color, 2)
	# Calculate the interval between tick marks
	interval4 = (line4_end[0] - line4_start[0]) // (num_ticks - 1)

	
	# Draw tick marks perpendicular to the line
	for i in range(num_ticks):
		tick_position = (line1_start[0], line1_start[1] + i * interval1)
		cv.line(img, (tick_position[0] - tick_length, tick_position[1]),
			(tick_position[0] + tick_length, tick_position[1]), black_color, 2)
		
	# Draw tick marks perpendicular to the line
	for i in range(num_ticks):
		tick_position = (line2_start[0], line2_start[1] + i * interval2)
		cv.line(img, (tick_position[0] - tick_length, tick_position[1]),
			(tick_position[0] + tick_length, tick_position[1]), black_color, 2)

	# Draw tick marks perpendicular to the line
	for i in range(num_ticks):
		tick_position = (line3_start[0] + i * interval3, line3_start[1])
		cv.line(img, (tick_position[0], tick_position[1] - tick_length),
				 (tick_position[0], tick_position[1] + tick_length), black_color, 2)

	# Draw tick marks perpendicular to the line
	for i in range(num_ticks):
		tick_position = (line4_start[0] + i * interval4, line4_start[1])
		cv.line(img, (tick_position[0], tick_position[1] - tick_length),
				 (tick_position[0], tick_position[1] + tick_length), black_color, 2)

	# label the scale
	img = cv.putText(img, "Distance (m)", (570, 30), font, 1.0, black_color, 4, cv.LINE_AA)

	# legend
	img = cv.putText(img, "1m intervals", (25, 1050), font, 0.8, black_color, 4, cv.LINE_AA)

	'''
	# Circle for each for triangulation
	red_color = 0, 0, 255
	# Must extract dimensions from node range circles
	node1Circle = (100, 500, 430)  # more code needed to find radius of circle from data (last number)
	node2Circle = (800, 1000, 600)  # more code needed to find radius of circle from data (last number)

	# Node 1
	img = cv.circle(img, (node1Circle[0], node1Circle[1]), node1Circle[2], red_color, 2)
	# Node 2
	img = cv.circle(img, (node2Circle[0], node2Circle[1]), node2Circle[2], red_color, 2)
	'''

	cv.imshow("Multi-Node UI", img)
	cv.waitKey(0)

# Triangulation Calculation
# Function to find intersection points of two circles
def find_circle_intersections(circle1, circle2):
	# Unpack circle parameters
	(x1, y1, r1) = circle1
	(x2, y2, r2) = circle2

	# Calculate distance between circle centers
	d = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

	# Check if circles intersect or touch
	if np.isclose(d, r1 + r2, 0.001):
		# Circles are touching, find point of tangency
		a = r1 / (r1 + r2)
		x0 = x1 + a * (x2 - x1)
		y0 = y1 + a * (y2 - y1)
		intersection = (int(x0), int(y0))
		return intersection, None
	elif d < r1 + r2:
		# Circles intersect, find intersection points
		a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
		h = np.sqrt(r1 ** 2 - a ** 2)
		x0 = x1 + a * (x2 - x1) / d
		y0 = y1 + a * (y2 - y1) / d
		intersection1 = (int(x0 + h * (y2 - y1) / d), int(y0 - h * (x2 - x1) / d))
		intersection2 = (int(x0 - h * (y2 - y1) / d), int(y0 + h * (x2 - x1) / d))
		return intersection1, intersection2
	else:
		# Circles do not intersect or touch
		return None, None
	

# # Find intersection points
# intersect1, intersect2 = find_circle_intersections(node1Circle, node2Circle)

# # Draw point if intersection is found
# if intersect1 is not None:
# 	cv.circle(img, intersect1, 10, (0, 255, 0), -1)
# if intersect2 is not None:
# 	cv.circle(img, intersect2, 10, (0, 255, 0), -1)

if __name__ == "__main__":
	visualizer()

