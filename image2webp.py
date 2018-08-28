#! /usr/bin/env python3

from PIL import Image
from glob import glob
import os
"""
说明：仅提供核心基础思想和脚本，自己可以改善为自动识别 Android 工程全部转换。

1. 将该脚本放置在自己 Android png 目录下;
2. 运行命令 python3 image2webp.py;
3. 在该目录下的 output 目录下生成当前文件夹下所有 png 图片对应的 webp 图片;
"""

def image2webp(inputFile, outputFile):
    try:
        image = Image.open(inputFile)
        if image.mode != 'RGBA' and image.mode != 'RGB':
            image = image.convert('RGBA')

        image.save(outputFile, 'WEBP')
        print(inputFile + ' has converted to ' + outputFile)
    except Exception as e:
        print('Error: ' + inputFile + ' converte failed to ' + outputFile)

matchFileList = glob('*.png')
if len(matchFileList) <= 0:
    print("There are no *.png file in this directory (you can run this script in your *png directory)!")
    exit(-1)

outputDir = os.getcwd() + "/output"
for pngFile in matchFileList:
    fileName = pngFile[0:pngFile.index('.')]
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    image2webp(pngFile, outputDir + "/" + fileName + ".webp")

print("Converted done! all webp file in the output directory!")
