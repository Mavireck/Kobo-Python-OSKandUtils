import KIP
import osk
import json
from _fbink import ffi, lib as FBInk
from PIL import Image, ImageDraw, ImageFont


fbink_cfg = ffi.new("FBInkConfig *")
fbink_cfg.is_centered = True
fbink_cfg.is_halfway = True

# Open the FB...
fbfd = FBInk.fbink_open()
FBInk.fbink_init(fbfd, fbink_cfg)


touchPath = "/dev/input/event1"
t = KIP.inputObject(touchPath, 1080, 1440)
if t==None:
	print("error")
FBInk.fbink_print(fbfd, b"Test ! Have Fun...", fbink_cfg)
FBInk.fbink_cls(fbfd, fbink_cfg)



with open('./sample-keymap-en_us.json') as json_file:
	km = json.load(json_file)
	vk = osk.virtKeyboard(km, 1080, 1440)

	# Generate an image of the OSK
	vkPNG = "./osk-en_us.png"
	vk.createIMG(vkPNG)
	# Print the image to the screen. Its position on screen should match that stored
	# in the keyboard object
	FBInk.fbink_print_image(fbfd, vkPNG, int(vk.StartCoords["X"]), int(vk.StartCoords["Y"]), fbink_cfg)
	runeStr = ""
	upperCase = False
	fbink_cfg.row = 0


	fbink_cfg.is_centered = False
	fbink_cfg.is_halfway = False


while True:

	(x, y,err) = t.getInput()
	if err != None:
		continue
	k = vk.getPressedKey(x, y)
	if k == None :
		continue
	if not k["isKey"]:
		continue
	if k["keyType"] == osk.KTstandardChar:
		if upperCase:
			key = str(k["keyCode"]).upper()
		else:
			key = str(k["keyCode"]).lower()
		runeStr = runeStr + key
		FBInk.fbink_print(fbfd, str(runeStr), fbink_cfg)
	elif k["keyType"] == osk.KTbackspace:
		if len(runeStr) > 0:
			# removing last element and drawing and empty space instead
			runeStr = runeStr[:-1] 
			FBInk.fbink_print(fbfd, str(runeStr) + " ", fbink_cfg)
	elif k["keyType"] == osk.KTcapsLock:
		if upperCase:
			upperCase = False
		else:
			upperCase = True
	elif k["keyType"] == osk.KTcarriageReturn:
		runeStr = ""
		fbink_cfg.row += 1
	else:
		continue