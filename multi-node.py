import cv2 as cv
import numpy as np
import tkinter as tk

def visualizer():
    # create window
    screen_width = 2000
    screen_height = 1100
    img = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)

    position_x = 1600  # x-coordinate of the line
    box_width = 2  # width of the line
    white_color = 255, 255, 255  # white color

    # draw rectangle to separate screen
    img = cv.rectangle(img, (0, 0), (position_x, screen_width), white_color, -1)

    # parameters of rectangle for data box
    rec_width = 200
    rec_height = 75
    font = cv.FONT_HERSHEY_SIMPLEX

    # text and data box for "Node 1 Range"
    img = cv.rectangle(img, (1700, 150), (1700 + rec_width, 150 + rec_height), white_color, -1)
    img = cv.putText(img, "Node 1 Range", (1700, 140), font, 0.9, white_color, 4, cv.LINE_AA)

    # text and data box for "Node 1 Angle"
    img = cv.rectangle(img, (1700, 425), (1700 + rec_width, 425 + rec_height), white_color, -1)
    img = cv.putText(img, "Node 1 Angle", (1700, 415), font, 0.9, white_color, 4, cv.LINE_AA)

    # text and data box for "Node 2 Range"
    img = cv.rectangle(img, (1700, 675), (1700 + rec_width, 675 + rec_height), white_color, -1)
    img = cv.putText(img, "Node 2 Range", (1700, 665), font, 0.9, white_color, 4, cv.LINE_AA)

    # text and data box for "Node 2 Angle"
    img = cv.rectangle(img, (1700, 950), (1700 + rec_width, 950 + rec_height), white_color, -1)
    img = cv.putText(img, "Node 2 Angle", (1700, 940), font, 0.9, white_color, 4, cv.LINE_AA)

    # Boxes representing the nodes
    node_height = 100
    node_width = 100
    black_color = 0, 0, 0

    # Node 1
    img = cv.rectangle(img, (50, 450), (50 + node_height, 450 + node_width), black_color, -1)
    img = cv.putText(img, "1", (90, 510), font, 1, white_color, 4, cv.LINE_AA)

    # Node 2
    img = cv.rectangle(img, (750, 950), (750 + node_height, 950 + node_width), black_color, -1)
    img = cv.putText(img, "2", (790, 1010), font, 1, white_color, 4, cv.LINE_AA)

    # Scale tick mark parameters
    num_ticks = 11
    tick_length = 10

    # vertical line adjacent to node 1
    line1_start = (150, 50)
    line1_end = (150, 950)
    img = cv.line(img, line1_start, line1_end, black_color, 2)
    # tick marks
    # Calculate the interval between tick marks
    interval1 = (line1_end[1] - line1_start[1]) // (num_ticks - 1)

    # Draw tick marks perpendicular to the line
    for i in range(num_ticks):
        tick_position = (line1_start[0], line1_start[1] + i * interval1)
        cv.line(img, (tick_position[0] - tick_length, tick_position[1]),
            (tick_position[0] + tick_length, tick_position[1]), black_color, 2)


    # vertical line adjacent to node 2
    line2_start = (1450, 50)
    line2_end = (1450, 950)
    img = cv.line(img, line2_start, line2_end, black_color, 2)
    # tick marks
    # Calculate the interval between tick marks
    interval2 = (line2_end[1] - line2_start[1]) // (num_ticks - 1)

    # Draw tick marks perpendicular to the line
    for i in range(num_ticks):
        tick_position = (line2_start[0], line2_start[1] + i * interval2)
        cv.line(img, (tick_position[0] - tick_length, tick_position[1]),
            (tick_position[0] + tick_length, tick_position[1]), black_color, 2)

    # bottom horizontal line
    line3_start = (150, 950)
    line3_end = (1450, 950)
    img = cv.line(img, line3_start, line3_end, black_color, 2)
    # Calculate the interval between tick marks
    interval3 = (line3_end[0] - line3_start[0]) // (num_ticks - 1)

    # Draw tick marks perpendicular to the line
    for i in range(num_ticks):
        tick_position = (line3_start[0] + i * interval3, line3_start[1])
        cv.line(img, (tick_position[0], tick_position[1] - tick_length),
                 (tick_position[0], tick_position[1] + tick_length), black_color, 2)

    # top horizontal line
    line4_start = (150, 50)
    line4_end = (1450, 50)
    img = cv.line(img, line4_start, line4_end, black_color, 2)
    # Calculate the interval between tick marks
    interval4 = (line4_end[0] - line4_start[0]) // (num_ticks - 1)

    # Draw tick marks perpendicular to the line
    for i in range(num_ticks):
        tick_position = (line4_start[0] + i * interval4, line4_start[1])
        cv.line(img, (tick_position[0], tick_position[1] - tick_length),
                 (tick_position[0], tick_position[1] + tick_length), black_color, 2)

    # label the scale
    img = cv.putText(img, "Distance", (750, 30), font, 0.9, black_color, 4, cv.LINE_AA)

    # legend
    img = cv.putText(img, "1m intervals", (25, 1050), font, 0.8, black_color, 4, cv.LINE_AA)

    # Circle for each for triangulation
    red_color = 0, 0, 255
    # Must extract dimensions from node range circles
    node1Circle = (100, 500, 430)  # more code needed to find radius of circle from data (last number)
    node2Circle = (800, 1000, 600)  # more code needed to find radius of circle from data (last number)

    # Node 1
    img = cv.circle(img, (node1Circle[0], node1Circle[1]), node1Circle[2], red_color, 2)
    # Node 2
    img = cv.circle(img, (node2Circle[0], node2Circle[1]), node2Circle[2], red_color, 2)
    cv.imshow("Multi-Node UI", img)
    cv.waitKey(0)

if __name__ == "__main__":
    visualizer()