import glob
import zipfile
from pathlib import Path
import os, shutil

for ufo in Path("sources/").glob("*.ufoz"):
    with zipfile.ZipFile(ufo, 'r') as zip_ref:
        zip_ref.extractall("sources/temp")