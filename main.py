import cv2
import numpy as np
from HandTrack import handDetector

# Constants for thickness and colors

BRUSH_THICKNESS = 15
ERASER_THICKNESS = 50

# Colors and tools

colors = [
    (255, 0, 255), (255, 0, 0), (0, 255, 0), (0, 255, 255), (255, 165, 0),
    (128, 0, 128), (0, 128, 128), (128, 128, 0), (75, 0, 130), (255, 192, 203)
]

color_names = ["Pink", "Blue", "Green", "Yellow", "Orange", "Purple",
"Teal", "Olive", "Indigo", "Light Pink"]

tools = ["Brush", "Eraser", "Rectangle", "Circle", "Triangle", "Line",
"Oval"]

# Initialize canvas variables

xp, yp = None, None

imgCanvas = np.zeros((720, 1280, 3), np.uint8)

# Function to draw an enhanced navigation bar

def draw_navbar(img):

    cv2.rectangle(img, (0, 0), (1280, 125), (30, 30, 30), -1)  # Navbar background

    # Draw tool buttons
    for i, tool in enumerate(tools):
        cv2.rectangle(img, (20 + i * 150, 20), (150 + i * 150, 105), (200, 200, 200), -1)
        cv2.putText(img, tool, (40 + i * 150, 75),
cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    # Draw color buttons
    for i, color in enumerate(colors):
        cv2.rectangle(img, (1050 + i * 45, 20), (1090 + i * 45, 105), color, -1)

# Initialize shape state

def reset_shape_state():

    global selected_shape, shape_start, resizing_shape

    selected_shape = None
    shape_start = None
    resizing_shape = False

# Initialize webcam

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detector instance

detector = handDetector(detectionCon=0.85)

# Current tool state

current_tool = "Brush"
selected_color = (255, 0, 255)
selected_shape = None
shape_start = None
resizing_shape = False
shape_finalized = False

while True:

    # Capture frame
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # Flip for mirror effect
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    draw_navbar(img)  # Draw the navigation bar

    if len(lmList) != 0:

        x1, y1 = lmList[8][1:]  # Tip of index finger

        # Check if the user selects a tool in the navbar with two fingers
        fingers = detector.fingersUp()

        if fingers[1] and fingers[2] and not any(fingers[3:]):

            if y1 < 125:  # Navbar area

                for i, tool in enumerate(tools):
                    if 20 + i * 150 < x1 < 150 + i * 150:
                        current_tool = tool
                        reset_shape_state()
                        xp, yp = None, None  # Reset last point for brush

                for i, color in enumerate(colors):
                    if 1050 + i * 45 < x1 < 1090 + i * 45:
                        selected_color = colors[i]
                        xp, yp = None, None  # Reset last point for brush

        # Drawing or resizing with one finger
        elif fingers[1] and not any(fingers[2:]):

            if current_tool == "Brush":
                cv2.circle(img, (x1, y1), 15, selected_color, cv2.FILLED)

                if xp is None or yp is None:
                    xp, yp = x1, y1

                cv2.line(img, (xp, yp), (x1, y1), selected_color,
BRUSH_THICKNESS)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), selected_color,
BRUSH_THICKNESS)

                xp, yp = x1, y1

            elif current_tool == "Eraser":
                cv2.circle(img, (x1, y1), 15, (0, 0, 0), cv2.FILLED)

                if xp is None or yp is None:
                    xp, yp = x1, y1

                cv2.line(img, (xp, yp), (x1, y1), (0, 0, 0),
ERASER_THICKNESS)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), (0, 0, 0),
ERASER_THICKNESS)

                xp, yp = x1, y1

            elif current_tool in ["Rectangle", "Circle", "Triangle", "Line",
"Oval"]:

                if shape_start is None:
                    shape_start = (x1, y1)
                    shape_finalized = False

                else:
                    tempCanvas = imgCanvas.copy()

                    if current_tool == "Rectangle":
                        cv2.rectangle(tempCanvas, shape_start, (x1, y1),
selected_color, 2)

                    elif current_tool == "Circle":
                        radius = int(((x1 - shape_start[0]) ** 2 + (y1 -
shape_start[1]) ** 2) ** 0.5)
                        cv2.circle(tempCanvas, shape_start, radius,
selected_color, 2)

                    elif current_tool == "Triangle":
                        pt1 = shape_start
                        pt2 = (x1, y1)
                        pt3 = (shape_start[0], y1)
                        pts = np.array([pt1, pt2, pt3], np.int32)
                        cv2.polylines(tempCanvas, [pts], isClosed=True,
color=selected_color, thickness=2)

                    elif current_tool == "Line":
                        cv2.line(tempCanvas, shape_start, (x1, y1),
selected_color, 2)

                    elif current_tool == "Oval":
                        center = ((shape_start[0] + x1) // 2, (shape_start[1] + y1) //
2)
                        axes = (abs(x1 - shape_start[0]) // 2, abs(y1 -
shape_start[1]) // 2)
                        cv2.ellipse(tempCanvas, center, axes, 0, 0, 360,
selected_color, 2)

                    img = cv2.bitwise_or(img, tempCanvas)

        # Finalize shape on release
        elif fingers[1] and fingers[2] and not shape_finalized:

            if shape_start is not None:

                if current_tool == "Rectangle":
                    cv2.rectangle(imgCanvas, shape_start, (x1, y1),
selected_color, 2)

                elif current_tool == "Circle":
                    radius = int(((x1 - shape_start[0]) ** 2 + (y1 -
shape_start[1]) ** 2) ** 0.5)
                    cv2.circle(imgCanvas, shape_start, radius,
selected_color, 2)

                elif current_tool == "Triangle":
                    pt1 = shape_start
                    pt2 = (x1, y1)
                    pt3 = (shape_start[0], y1)
                    pts = np.array([pt1, pt2, pt3], np.int32)
                    cv2.polylines(imgCanvas, [pts], isClosed=True,
color=selected_color, thickness=2)

                elif current_tool == "Line":
                    cv2.line(imgCanvas, shape_start, (x1, y1),
selected_color, 2)

                elif current_tool == "Oval":
                    center = ((shape_start[0] + x1) // 2, (shape_start[1] + y1) //
2)
                    axes = (abs(x1 - shape_start[0]) // 2, abs(y1 -
shape_start[1]) // 2)
                    cv2.ellipse(imgCanvas, center, axes, 0, 0, 360,
selected_color, 2)

                reset_shape_state()
                shape_finalized = True

        else:
            xp, yp = None, None

    else:
        xp, yp = None, None

    # Merging canvas and webcam feed
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255,
cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # Display the image
    cv2.imshow("Canvas", imgCanvas)
    cv2.imshow("Air Canvas", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
