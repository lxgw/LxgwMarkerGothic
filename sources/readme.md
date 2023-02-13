请运行 `build.bat` 或 `build.sh` 以生成字体。需要安装 [`fontmake`](https://github.com/googlefonts/fontmake)：`pip3 install fontmake` 和 [`fontTools`](https://github.com/fonttools/fonttools)：`pip3 install fonttools`。

目前源文件使用 [UFO 3 ZIP 格式（`.ufoz`）](https://unifiedfontobject.org/versions/ufo3/)，碍于 `fontmake` 暂不支援 `.ufoz` 格式，因此运行 `extract_ufoz.py` 解压缩后使用其 `.ufo` 文件夹制作字体。



Please run `build.bat` or `build.sh`  to build font. [`fontmake`](https://github.com/googlefonts/fontmake) (`pip3 install fontmake`) and [`fontTools`](https://github.com/fonttools/fonttools)（`pip3 install fonttools`） are required.

The source files are provided in [UFO 3 ZIP format (`.ufoz`)](https://unifiedfontobject.org/versions/ufo3/). As `fontmake` does not support `.ufoz` files yet, the script will run `extract_ufoz.py` to extract the `.ufo` folders before running `fontmake` on the `.ufo` folders to build the fonts.

