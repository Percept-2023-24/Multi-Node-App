import cv2 as cv
import numpy as np
import json
import os

'''Important parameters for drawing UI'''
font = cv.FONT_HERSHEY_SIMPLEX
font_size = 1.1
font_thickness = 2

white_color = 255, 255, 255  	# white
black_color = 0, 0, 0			# black
gray_color = 211, 211, 211		# gray
red_color = 20, 70, 220			# red
blue_color = 220, 100, 50		# blue
green_color = 100, 190, 0		# green
brown_color = 50, 56, 75		# brown
cyan_color = 255, 255, 0		# cyan
purple_color = 200, 120, 232	# bright purple
gold_color = 48, 180, 238		# gold

# For drawing data boxes
rec_width = 163
rec_height = 80

# Node positions
center_mw = (110, 420)
center_p = (480, 790)

# For main node-object display
axis_length = 740 				# axis length in pixels
max_range = 9					# axis length in meters (change this based on test setup)

# Size of visualizer window
screen_width = 1450
screen_height = 900

# Scale tick mark parameters
num_ticks = 11
tick_length = 10

def draw_vis(ui_img):
	# Node 1 box
	ui_img = cv.rectangle(ui_img, (10, 370), (110, 470), black_color, -1)
	ui_img = cv.putText(ui_img, "1", (40, 440), font, font_size+1, white_color, 6, cv.LINE_AA)

	# Node 2 box
	ui_img = cv.rectangle(ui_img, (430, 790), (530, 890), black_color, -1)
	ui_img = cv.putText(ui_img, "2", (460, 860), font, font_size+1, white_color, 6, cv.LINE_AA)

	# vertical line adjacent to node 1
	line1_start = (110, 50)
	line1_end = (110, 790)
	ui_img = cv.line(ui_img, line1_start, line1_end, black_color, 2)
	# tick marks
	# Calculate the interval between tick marks
	interval1 = (line1_end[1] - line1_start[1]) // (num_ticks - 1)

	# bottom horizontal line
	line3_start = (110, 790)
	line3_end = (850, 790)
	ui_img = cv.line(ui_img, line3_start, line3_end, black_color, 2)
	# Calculate the interval between tick marks
	interval3 = (line3_end[0] - line3_start[0]) // (num_ticks - 1)

	# vertical line adjacent to node 2
	line2_start = (850, 790)
	line2_end = (850, 50)
	ui_img = cv.line(ui_img, line2_start, line2_end, black_color, 2)
	# tick marks
	# Calculate the interval between tick marks
	interval2 = (line2_end[1] - line2_start[1]) // (num_ticks - 1)

	# top horizontal line
	line4_start = (850, 50)
	line4_end = (110, 50)
	ui_img = cv.line(ui_img, line4_start, line4_end, black_color, 2)
	# Calculate the interval between tick marks
	interval4 = (line4_end[0] - line4_start[0]) // (num_ticks - 1)

	# Draw tick marks perpendicular to the line
	for i in range(num_ticks):
		tick_position = (line1_start[0], line1_start[1] + i * interval1)
		cv.line(ui_img, (tick_position[0] - tick_length, tick_position[1]),
			(tick_position[0] + tick_length, tick_position[1]), black_color, 2)
		
	# Draw tick marks perpendicular to the line
	for i in range(num_ticks):
		tick_position = (line2_start[0], line2_start[1] + i * interval2)
		cv.line(ui_img, (tick_position[0] - tick_length, tick_position[1]),
			(tick_position[0] + tick_length, tick_position[1]), black_color, 2)

	# Draw tick marks perpendicular to the line
	for i in range(num_ticks):
		tick_position = (line3_start[0] + i * interval3, line3_start[1])
		cv.line(ui_img, (tick_position[0], tick_position[1] - tick_length),
				 (tick_position[0], tick_position[1] + tick_length), black_color, 2)

	# Draw tick marks perpendicular to the line
	for i in range(num_ticks):
		tick_position = (line4_start[0] + i * interval4, line4_start[1])
		cv.line(ui_img, (tick_position[0], tick_position[1] - tick_length),
				 (tick_position[0], tick_position[1] + tick_length), black_color, 2)
		
	# X-axis label
	ui_img = cv.putText(ui_img, "Distance (m)", (370, 30), font, 1.0, black_color, 4, cv.LINE_AA)

	# Y-axis label
	ui_img = cv.putText(ui_img, "D", (885, 330), font, 1.0, black_color, 4, cv.LINE_AA)
	ui_img = cv.putText(ui_img, "i", (890, 360), font, 1.0, black_color, 4, cv.LINE_AA)
	ui_img = cv.putText(ui_img, "s", (886, 385), font, 1.0, black_color, 4, cv.LINE_AA)
	ui_img = cv.putText(ui_img, "t", (888, 415), font, 1.0, black_color, 4, cv.LINE_AA)
	ui_img = cv.putText(ui_img, "a", (885, 440), font, 1.0, black_color, 4, cv.LINE_AA)
	ui_img = cv.putText(ui_img, "n", (885, 465), font, 1.0, black_color, 4, cv.LINE_AA)
	ui_img = cv.putText(ui_img, "c", (885, 490), font, 1.0, black_color, 4, cv.LINE_AA)
	ui_img = cv.putText(ui_img, "e", (885, 515), font, 1.0, black_color, 4, cv.LINE_AA)
	ui_img = cv.putText(ui_img, "(m)", (865, 550), font, 1.0, black_color, 4, cv.LINE_AA)
		
	return ui_img

def draw_text(ui_img):
	# text and data box for Frame #
	ui_img = cv.rectangle(ui_img, (987, 118), (987 + rec_width, 118 + rec_height), white_color, -1)
	ui_img = cv.putText(ui_img, "Frame #", (995, 97), font, font_size, white_color, font_thickness, cv.LINE_AA)

	# text and data box for Elapsed time (ms)
	ui_img = cv.rectangle(ui_img, (1192, 118), (1258 + rec_width, 118 + rec_height), white_color, -1)
	ui_img = cv.putText(ui_img, "Runtime (ms)", (1190, 97), font, font_size, white_color, font_thickness, cv.LINE_AA)

	# Node 1 title
	ui_img = cv.putText(ui_img, "Node 1", (1110, 355), font, font_size+0.5, white_color, font_thickness+2, cv.LINE_AA)
	ui_img = cv.line(ui_img, (1110, 365), (1285, 365), white_color, 3)
	# text and data box for "Angle"
	ui_img = cv.rectangle(ui_img, (1012, 438), (1012 + rec_width, 438 + rec_height), white_color, -1)
	ui_img = cv.putText(ui_img, "Range (m)", (1002, 420), font, font_size, white_color, font_thickness, cv.LINE_AA)
	# text and data box for "Angle"
	ui_img = cv.rectangle(ui_img, (1240, 438), (1240 + rec_width, 438 + rec_height), white_color, -1)
	ui_img = cv.putText(ui_img, "Angle (deg)", (1225, 420), font, font_size, white_color, font_thickness, cv.LINE_AA)

	# Node 2 title
	ui_img = cv.putText(ui_img, "Node 2", (1110, 655), font, font_size+0.5, white_color, font_thickness+2, cv.LINE_AA)
	ui_img = cv.line(ui_img, (1110, 665), (1295, 665), white_color, 3)
	# text and data box for "Angle"
	ui_img = cv.rectangle(ui_img, (1012, 738), (1012 + rec_width, 738 + rec_height), white_color, -1)
	ui_img = cv.putText(ui_img, "Range (m)", (1002, 720), font, font_size, white_color, font_thickness, cv.LINE_AA)
	# text and data box for "Angle"
	ui_img = cv.rectangle(ui_img, (1240, 738), (1240 + rec_width, 738 + rec_height), white_color, -1)
	ui_img = cv.putText(ui_img, "Angle (deg)", (1225, 720), font, font_size, white_color, font_thickness, cv.LINE_AA)

	return ui_img

def base_ui():
	img = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)				# main window

	# Draw rectangle to separate screen
	img = cv.rectangle(img, (0, 0), (950, screen_width), white_color, -1)			# main visualizer
	img = cv.rectangle(img, (950, 0), (960, screen_height), gray_color, -1)			# vertical border
	img = cv.rectangle(img, (960, 295), (screen_width, 305), gray_color, -1)		# horizontal border
	img = cv.rectangle(img, (960, 595), (screen_width, 605), gray_color, -1)		# horizontal border
	img = cv.rectangle(img, (960, 0), (screen_width, 295), red_color, -1)			# top info screen
	img = cv.rectangle(img, (960, 305), (screen_width, 595), blue_color, -1)		# middle info screen
	img = cv.rectangle(img, (960, 605), (screen_width, 900), green_color, -1)		# bottom info screen

	img = draw_text(img)	# Draw main text fields
	img = draw_vis(img)		# Draw main visualizer (axis + nodes)

	return img

def clear_text(ui_img):
	# Clear General Text
	ui_img = cv.rectangle(ui_img, (987, 118), (987 + rec_width, 118 + rec_height), white_color, -1)
	ui_img = cv.rectangle(ui_img, (1192, 118), (1258 + rec_width, 118 + rec_height), white_color, -1)

	# Clear Node 1 Text
	ui_img = cv.rectangle(ui_img, (1012, 438), (1012 + rec_width, 438 + rec_height), white_color, -1)
	ui_img = cv.rectangle(ui_img, (1240, 438), (1240 + rec_width, 438 + rec_height), white_color, -1)

	# Clear Node 2 Text
	ui_img = cv.rectangle(ui_img, (1012, 738), (1012 + rec_width, 738 + rec_height), white_color, -1)
	ui_img = cv.rectangle(ui_img, (1240, 738), (1240 + rec_width, 738 + rec_height), white_color, -1)
	
	return ui_img

def clear_vis(ui_img):
	ui_img = cv.rectangle(ui_img, (0, 0), (950, screen_width), white_color, -1)	# main visualizer
	ui_img = draw_vis(ui_img)
	return ui_img

def find_circle_intersections(circle1, circle2):
	# Unpack circle parameters
	(x1, y1, r1) = circle1
	(x2, y2, r2) = circle2

	# Calculate distance between circle centers
	d = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

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
	
def triangulate(ui_img, circle1, circle2, obj1, obj2):
	# Find intersection points
	intersect1, intersect2 = find_circle_intersections(circle1, circle2)

	# check distance between actual points and each intersection point 
	# to determine final object location here

	if (intersect1 != None and intersect2 != None):
		d_mw_1 = np.sqrt((obj1[0] - intersect1[0])**2 + (obj1[1] - intersect1[1])**2)
		d_mw_2 = np.sqrt((obj1[0] - intersect2[0])**2 + (obj1[1] - intersect2[1])**2)
		d_p_1 = np.sqrt((obj2[0] - intersect1[0])**2 + (obj2[1] - intersect1[1])**2)
		d_p_2 = np.sqrt((obj2[0] - intersect2[0])**2 + (obj2[1] - intersect2[1])**2)

		if (d_mw_1 < d_mw_2):
			mw_which_intersect = intersect1
		else:
			mw_which_intersect = intersect2
		
		if (d_p_1 < d_p_2):
			p_which_intersect = intersect1
		else:
			p_which_intersect = intersect2

		if (p_which_intersect == mw_which_intersect):
			ui_img = cv.circle(ui_img, p_which_intersect, 13, purple_color, -1)
		else:
			ui_img = cv.circle(ui_img, intersect1, 13, purple_color, -1)
			ui_img = cv.circle(ui_img, intersect2, 13, purple_color, -1)

	elif (intersect1 != None and intersect2 == None):
		ui_img = cv.circle(ui_img, intersect1, 13, purple_color, -1)
		
	elif (intersect1 == None and intersect2 != None):
		ui_img = cv.circle(ui_img, intersect2, 13, purple_color, -1)
	
	return ui_img

def update_ui(frame, fname_mw, fname_p, ui_img):
	data_mw = json.load(open(fname_mw))
	data_p = json.load(open(fname_p))

	angle_mw = data_mw['Angle']
	range_mw = data_mw['Range']
	angle_p = data_p['Angle']
	range_p = data_p['Range']
	runtime = data_p['Elapsed Time (ms)']

	# Clear UI before adding new text/shapes
	ui_img = clear_text(ui_img)
	ui_img = clear_vis(ui_img)

	# Place text for new frame data
	ui_img = cv.putText(ui_img, str(frame), (1035, 172), font, 1.4, black_color, font_thickness, cv.LINE_AA)
	ui_img = cv.putText(ui_img, str(runtime), (1200, 172), font, 1.4, black_color, font_thickness, cv.LINE_AA)
	ui_img = cv.putText(ui_img, str(angle_mw), (1255, 492), font, 1.4, black_color, font_thickness, cv.LINE_AA)
	ui_img = cv.putText(ui_img, str(angle_p), (1255, 792), font, 1.4, black_color, font_thickness, cv.LINE_AA)
	ui_img = cv.putText(ui_img, str(range_mw), (1060, 492), font, 1.4, black_color, font_thickness, cv.LINE_AA)
	ui_img = cv.putText(ui_img, str(range_p), (1060, 792), font, 1.4, black_color, font_thickness, cv.LINE_AA)

	# For semicircles (node FOV based on range)
	radius_mw = round(0.5*range_mw*axis_length/max_range)
	radius_p = round(0.5*range_p*axis_length/max_range)
	node1Circle = (center_mw[0], center_mw[1], radius_mw)
	node2Circle = (center_p[0], center_p[1], radius_p)

	# Determine object location reported by each node
	if(angle_mw <= 0):
		theta_mw = (angle_mw+90)*np.pi/180
		x_mw = round(radius_mw*np.sin(theta_mw))
		y_mw = round(radius_mw*np.cos(theta_mw))
		obj_mw = (center_mw[0]+x_mw, center_mw[1]-y_mw)	# Node 1 object location
	else:
		theta_mw = (90-angle_mw)*np.pi/180
		x_mw = round(radius_mw*np.sin(theta_mw))
		y_mw = round(radius_mw*np.cos(theta_mw))
		obj_mw = (center_mw[0]+x_mw, center_mw[1]+y_mw) # Node 1 object location
	
	if(angle_p <= 0):
		theta_p = (angle_p+90)*np.pi/180
		x_p = round(radius_p*np.cos(theta_p))
		y_p = round(radius_p*np.sin(theta_p))
		obj_p = (center_p[0]-x_p, center_p[1]-y_p) # Node 2 object location
	else:
		theta_p = (90-angle_p)*np.pi/180
		x_p = round(radius_p*np.cos(theta_p))
		y_p = round(radius_p*np.sin(theta_p))
		obj_p = (center_p[0]+x_p, center_p[1]-y_p) # Node 2 object location

	# Draw node semicircles
	ui_img = cv.ellipse(ui_img, center_mw, (radius_mw, radius_mw), 0, -90, 90, brown_color, 1, cv.LINE_AA)		# Node 1
	ui_img = cv.ellipse(ui_img, center_p, (radius_p, radius_p), 0, 180, 360, brown_color, 1, cv.LINE_AA)		# Node 2

	# Draw object locations (can remove later)
	ui_img = cv.circle(ui_img, obj_mw, 6, gold_color, -1)
	ui_img = cv.circle(ui_img, obj_p, 6, gold_color, -1)

	# Triangulate object location
	ui_img = triangulate(ui_img, node1Circle, node2Circle, obj_mw, obj_p)
	
	return ui_img

def vis_loop():
	win_path = '/mnt/c/Users/adity/Programming/Capstone/Multi-Node-App/frame_data/'
	linux_path = '/home/aditya/Programming/Capstone/Multi-Node-App/frame_data/'
	frame = 1
	num_frames = 10
	fname_mw = linux_path + 'Mike_Frame{}.json'.format(frame)
	fname_p = linux_path + 'Patrick_Frame{}.json'.format(frame)

	winname = "Multi-Node Visualizer"
	curr_img = base_ui()

	while (True):
		if(os.path.isfile(fname_mw) and os.path.isfile(fname_p)):
			curr_img = update_ui(frame, fname_mw, fname_p, curr_img)
			frame+=1
			fname_mw = linux_path + 'Mike_Frame{}.json'.format(frame)
			fname_p = linux_path + 'Patrick_Frame{}.json'.format(frame)
		
		cv.imshow(winname, curr_img)
		# cv.moveWindow(winname, 1, 0)
		cv.waitKey(1)

		if(frame == num_frames):
			break
	cv.waitKey()
	

if __name__ == "__main__":
	vis_loop()
	# win_path = '/mnt/c/Users/adity/Programming/Capstone/Multi-Node-App/frame_data/'
	# linux_path = '/home/aditya/Programming/Capstone/Multi-Node-App/frame_data/'
	# winname = "Multi-Node Visualizer"
	# base_img = base_ui()
	# cv.imshow(winname, base_img)
	# cv.moveWindow(winname, 1, 0)
	# cv.waitKey(500)

	# num_frames = 10
	# frame = 1
	# while (frame <= num_frames):
	# 	fname_mw = linux_path + 'Mike_Frame{}.json'.format(frame)
	# 	fname_p = linux_path + 'Patrick_Frame{}.json'.format(frame)
	# 	new_img = update_ui(fname_mw, fname_p, base_img)
	# 	new_img = cv.putText(new_img, str(frame), (1035, 172), font, 1.4, black_color, font_thickness, cv.LINE_AA)
	# 	cv.imshow(winname, new_img)
	# 	cv.moveWindow(winname, 1, 0)
	# 	cv.waitKey(350)
	# 	frame+=1
	# cv.waitKey()

