from PIL import Image

for i in range(79, 80):
	img = Image.open("WechatIMG" + str(i) +".jpeg")
	img2 = img.crop((220, 200, 800, 700))
	img2.save("damping0.0_"+str(i - 70)+".jpg")
