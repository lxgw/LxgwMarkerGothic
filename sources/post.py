import glob
from pathlib import Path
from fontTools.ttLib import TTFont

for file in Path("fonts").glob("**/*.ttf"):
	font = TTFont(str(file))
	if font["gasp"].gaspRange != {65535: 0x000A}:
		font["gasp"].gaspRange = {65535: 0x000A}

	font.save(file)