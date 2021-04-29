import sys
from mainWindow import *
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

suppress_qt_warnings()


def runEncrypto(args = None):
	if args is None:
		args = sys.argv[1:]

	mainWindow()



if __name__ == "__main__":
	runEncrypto()