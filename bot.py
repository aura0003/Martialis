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


tokenr = open("token.token", "r")
token = tokenr.read()

# Setting Prefix
client = commands.Bot(command_prefix = '') # Command Prefix

# When Bot is ready!
@client.event
async def on_ready():
    print("Bot's Ready!")

# OCR Command
@client.command()
async def ocr(ctx, *, message : str):
    
    url = message
        
     # Read image from which text needs to be extracted
    req = Request(
        url=message, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    wp = urlopen(req)
    arr = np.asarray(bytearray(wp.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1) # 'Load it as it is'

    # Convert to grayscale and apply Gaussian filtering
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    gray = cv2.bitwise_not(img_bin)

    # Specify structure shape and kernel size.
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.erode(gray, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)

    # Print extracted text
    out_below = pt.image_to_string(img)
                    
    # Send Image
    await ctx.send(out_below)

                    
# Run
client.run(token)
token.close()