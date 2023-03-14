import discord
import aiohttp
import async_timeout
import asyncio
import os
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from discord.ext import commands
import uuid
import pytesseract as pt
import numpy as np
import numpy as np
from urllib.request import Request, urlopen
import cv2
import time

tokenr = open("token.token", "r")
token = tokenr.read()

# Setting Prefix
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '', intents=intents) # Command Prefix


# When Bot is ready!
@client.event
async def on_ready():
    print("Bot's Ready!")

# OCR Command
@client.command()
async def ocr(ctx, *, message : str):
    
    """
    # Starting Command Message [FOR TESTING]
    inittime = time.time()
    strinittime = str(inittime)
    print("Starting " + strinittime)
    """
    
    url = message
        
    # Read image from URL
    req = Request(
        url = url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    wp = urlopen(req)
    arr = np.asarray(bytearray(wp.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1) # 'Load it as it is'
    
    # Remove alpha channel
    a,b,g,r = cv2.split(img)
    img = cv2.merge((r,g,b))

    # EDSR Super Resolution Upscaling
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    path = "EDSR_x4.pb"
    sr.readModel(path)
    sr.setModel("edsr",4)
    result = sr.upsample(img)

    # Resized image
    img = cv2.resize(result,dsize=None,fx=4,fy=4)

    # Convert to grayscale and apply Gaussian filtering
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    gray = cv2.bitwise_not(img_bin)

    # Specify structure shape and kernel size.
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.erode(gray, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)

    # Upscale and blur image
    img = cv2.pyrUp(img)

    # Print extracted text
    out_below = pt.image_to_string(img)
                    
    # Send Response
    await ctx.send('```' + out_below + '```')
    print(out_below)
    
    # Ending Command Message [FOR TESTING]
    """
    endtime = time.time()
    strendtime = str(endtime)
    print("Finished " + strendtime)
    
    timetaken = endtime - inittime
    strtimetaken = str(timetaken)
    print(strtimetaken)
    await ctx.send('That took ' + strtimetaken + " seconds to complete!")
    """
                    
# Run
client.run(token)
token.close()