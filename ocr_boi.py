import numpy as nm
from time import sleep
import pytesseract
import cv2
from PIL import ImageGrab


def ScreenCap():
	health_list = []
	pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
	while(True):
		cap = ImageGrab.grab(bbox =(1040, 1370, 1350, 1400))#top x, top y, bottom x, bottom y
		cv2.imshow('window', cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY))
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break
		tesstr = pytesseract.image_to_string(cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY))
		tesstr = tesstr[:-2]
		try:
			tesstr = eval(tesstr)
			
			if tesstr <= 1:
				health_list.append(tesstr)
				if(tesstr < health_list[-2]):
					print("Health Loss")
		except:
			continue

ScreenCap()
