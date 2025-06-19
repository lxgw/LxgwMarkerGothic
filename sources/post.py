import glob
from pathlib import Path
from fontTools.ttLib import TTFont
import os

try:
	os.mkdir("fonts/gf/",)
except:
	pass

for file in Path("fonts").glob("**/*.ttf"):
	font = TTFont(str(file))
	if font["gasp"].gaspRange != {65535: 0x000A}:
		font["gasp"].gaspRange = {65535: 0x000A}

	try:
		del font["prep"]
	except KeyError:
		pass

	font.save(file)

	font["OS/2"].sTypoAscender = 982
	font["OS/2"].sTypoDescender = -198
	font["OS/2"].sTypoLineGap = 0
	font["hhea"].ascender = 982
	font["hhea"].descender = -198
	font["hhea"].lineGap = 0
	font["OS/2"].usWinAscent = 1160
	font["OS/2"].usWinDescent = 288
	font["OS/2"].fsSelection = 0x00c0

	font.save(str(file).replace('/ttf/',"/gf/"))