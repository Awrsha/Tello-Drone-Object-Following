import numpy as np

from djitellopy import tello

import cv2

me = tello.Tello()

me.connect()

print(me.get_battery())

me.streamon()

#me.takeoff()

cap = cv2.VideoCapture(1)

hsvVals = [0,0,188,179,33,245]

sensors = 3

threshold = 0.2

width, height = 480, 360

senstivity = 3  # if number is high less sensitive

weights = [-25, -15, 0, 15, 25]

fSpeed = 15

curve = 0

def thresholding(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([hsvVals[0], hsvVals[1], hsvVals[2]])

    upper = np.array([hsvVals[3], hsvVals[4], hsvVals[5]])

    mask = cv2.inRange(hsv, lower, upper)

    return mask

def getContours(imgThres, img):

    cx = 0

    contours, hieracrhy = cv2.findContours(imgThres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:

        biggest = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(biggest)

        cx = x + w // 2

        cy = y + h // 2

        cv2.drawContours(img, biggest, -1, (255, 0, 255), 7)

        cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    return cx

def getSensorOutput(imgThres, sensors):

    imgs = np.hsplit(imgThres, sensors)

    totalPixels = (img.shape[1] // sensors) * img.shape[0]

    senOut = []

    for x, im in enumerate(imgs):

        pixelCount = cv2.countNonZero(im)

        if pixelCount > threshold * totalPixels:

            senOut.append(1)

        else:

            senOut.append(0)

        # cv2.imshow(str(x), im)

    # print(senOut)

    return senOut

def sendCommands(senOut, cx):

    global curve

    ## TRANSLATION

    lr = (cx - width // 2) // senstivity

    lr = int(np.clip(lr, -10, 10))

    if 2 > lr > -2: lr = 0

    ## Rotation

    if   senOut == [1, 0, 0]: curve = weights[0]

    elif senOut == [1, 1, 0]: curve = weights[1]

    elif senOut == [0, 1, 0]: curve = weights[2]

    elif senOut == [0, 1, 1]: curve = weights[3]

    elif senOut == [0, 0, 1]: curve = weights[4]

    elif senOut == [0, 0, 0]: curve = weights[2]

    elif senOut == [1, 1, 1]: curve = weights[2]

    elif senOut == [1, 0, 1]: curve = weights[2]

    me.send_rc_control(lr, fSpeed, 0, curve)

while True:

    #_, img = cap.read()

    img = me.get_frame_read().frame

    img = cv2.resize(img, (width, height))

    img = cv2.flip(img, 0)

    imgThres = thresholding(img)

    cx = getContours(imgThres, img)  ## For Translation

    senOut = getSensorOutput(imgThres, sensors)  ## Rotation

    sendCommands(senOut, cx)

    cv2.imshow("Output", img)

    cv2.imshow("Path", imgThres)

    cv2.waitKey(1)

# Color Picker

from djitellopy import tello

import cv2

import numpy as np

frameWidth = 480

frameHeight = 360

me = tello.Tello()

me.connect()

print(me.get_battery())

me.streamon()

def empty(a):

    pass

cv2.namedWindow("HSV")

cv2.resizeWindow("HSV", 640, 240)

cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)

cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)

cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)

cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)

cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)

cv2.createTrackbar("VALUE Max","HSV", 255, 255, empty)

#cap = cv2.VideoCapture(1)

frameCounter = 0

while True:

    img = me.get_frame_read().frame

    #_, img = cap.read()

    img = cv2.resize(img, (frameWidth, frameHeight))

    img = cv2.flip(img,0)

    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "HSV")

    h_max = cv2.getTrackbarPos("HUE Max", "HSV")

    s_min = cv2.getTrackbarPos("SAT Min","HSV")

    s_max = cv2.getTrackbarPos("SAT Max", "HSV")

    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")

    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

    lower = np.array([h_min, s_min, v_min])

    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(imgHsv, lower, upper)

    result = cv2.bitwise_and(img, img, mask=mask)

    print(f'[{h_min},{s_min},{v_min},{h_max},{s_max},{v_max}]')

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    hStack = np.hstack([img, mask, result])

    cv2.imshow('Horizontal Stacking', hStack)

    if cv2.waitKey(1) and 0xFF == ord('q'):

        break

# cap.release()
# 
# cv2.destroyAllWindows()