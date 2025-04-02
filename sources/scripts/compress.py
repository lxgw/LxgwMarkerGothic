import glob
from pathlib import Path
import os
import ufoLib2

if os.path.exists("sources/temp"):
    archive_list = Path("sources/temp/").glob("*.ufo")

    for file in archive_list:
        print ("Packaging - "+str(file).split("/")[2])
        ufo = ufoLib2.Font.open(file)
        ufo.save(str(file).replace("temp/","")+"z",structure="zip",overwrite=True)

else:
    print ("No temp folder found")