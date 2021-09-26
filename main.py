
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image,ImageOps,ImageFont,ImageDraw
import textwrap
import requests
import csv
from flask import jsonify
from defstuff import *
import uvicorn
import aiohttp
import os
import random
import json
from io import BytesIO
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")    
templates = Jinja2Templates(directory="templates")

async def WebCounter(page):
    print("h")

@app.get("/", response_class=HTMLResponse)
async def uij(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/wanted')
async def wanted(avatar:str=None):
    if not avatar==None:
        
        response = requests.get(avatar)
        image = Image.open(BytesIO(response.content))
        image.save("avatar.png")
        pfp=Image.open("avatar.png")
        pfp=pfp.resize((177,177))
        wanted=Image.open("image/wanted.jpg")
        wanted.paste(pfp,(120,212))
        wanted.save("trash_photo/wanted2.jpg")
        return FileResponse("trash_photo/wanted2.jpg")
@app.get('/trash')
async def trash(avatar:str=None):
      
        
    if not avatar==None:
        await WebCounter('trash')
        response = requests.get(avatar)
        image = Image.open(BytesIO(response.content))
        image.save("avatar.png")
        pfp=Image.open("avatar.png")
        pfp=pfp.resize((170,170))
        trash=Image.open("image/trash.png")
        trash.paste(pfp,(140,145),pfp.convert("RGBA"))
        trash.save("trash_photo/trashpic.png")
        return FileResponse("trash_photo/trashpic.png", )



@app.get('/greyscale')
async def grey_scale(avatar:str=None):

    if not avatar==None:
        await WebCounter('greyscale')
        
        response = requests.get(avatar)
        image = Image.open(BytesIO(response.content))
        pfp = image.convert("L")
        pfp.save("trash_photo/greyscale.png")
        return FileResponse("trash_photo/greyscale.png")

@app.get('/alert')
async def alert(text:str=None):
    if not text==None:
        await WebCounter('alert')

        alert=Image.open("image/alert.jpg")
        font=ImageFont.truetype("image/arial.ttf",32)
        draw=ImageDraw.Draw(alert)
        draw.text((55,566),text,(0,0,0),font=font)
        alert.save("trash_photo/alert.png")
        return FileResponse("trash_photo/alert.png",)



@app.get('/json/quote')
async def qoutes():

    await WebCounter('quote')
    with open("api-things/qoutes.json",encoding="utf-8") as json_file:
      data = json.load(json_file)
      Rdata=random.choice(data["quotes"])

    return Rdata
@app.get('/hitler')
async def hiter(avatar:str=None):
    if not avatar==None:
        await WebCounter('hitler')
        
        response = requests.get(avatar)
        image = Image.open(BytesIO(response.content))
        image.save("avatar.png")
        pfp=Image.open("avatar.png")
        pfp=pfp.resize((160,160))
        trash=Image.open("image/hitler.png")
        trash.paste(pfp,(29,32),pfp.convert("RGBA"))
        trash.save("trash_photo/hitlerpic.png")
        return FileResponse("trash_photo/hitlerpic.png",)



@app.get('/billy')
async def billy(text:str=None):
    if not text==None:
        await WebCounter('billy')
        
        alert=Image.open("image/billy.png")
        font=ImageFont.truetype("image/arial.ttf",20)
        draw=ImageDraw.Draw(alert)
        draw.text((26,291),text,(0,0,0),font=font)
        alert.save("trash_photo/billy2.png")
        return FileResponse("trash_photo/billy2.png")

                                                                                                            

@app.get('/god_temp')
async def god_temp(text:str=None):
    
    if not text==None:


        alert=Image.open("image/god-meme-template.jpg")
        font=ImageFont.truetype("image/arial.ttf",32)
        draw=ImageDraw.Draw(alert)
        draw.text((93,350),text,(0,0,0),font=font)
        alert.save("trash_photo/god_temp.png")
        return FileResponse("trash_photo/god_temp.png",)

@app.get('/biden')
async def biden(text:str=None):
    if not text==None:
        alert=Image.open("image/biden.png")
        font=ImageFont.truetype("image/arial.ttf",32)
        draw=ImageDraw.Draw(alert)
        draw.text((30,110),text,(0,0,0),font=font)
        alert.save("trash_photo/biden.png")
        return FileResponse("trash_photo/biden.png")

@app.get('/pacman/text')
async def pacman(text:str=None):
    if not text==None:
        lines = textwrap.wrap(text, width=10)


        image=Image.open("image/blankimage.png")
        width, height = image.size
        
        font=ImageFont.truetype("api-things/CrackMan.tff",120)
        draw=ImageDraw.Draw(image)

        y_text = 50
        for line in lines:
          width, height = font.getsize(line)
      

          draw.text(((992 - width) / 2, y_text), line,(0,0,0), font=font)
          #draw.text((26,265),line,(0,0,0),font=font)
          y_text += height
        #draw.text((26,265),text,(0,0,0),font=font)
        image.save("trash_photo/pacmantext.png")
        return FileResponse("trash_photo/pacmantext.png", )

@app.get("/image/otter",)
async def otters_img():
  imgList = os.listdir("otter")
  seal = random.choice(imgList)
  return FileResponse(f"otter/{seal}")

@app.get("/image/dog",)
async def dog_img():
  
  imgList = os.listdir("dogs")
  seal = random.choice(imgList)
  return FileResponse(f"dogs/{seal}")


@app.get('/json/dogs', )
async def Dfact():
    with open("api-things/dfact.json") as json_file:
      data = json.load(json_file)
      Rdata=random.choice(data)
    return Rdata 



@app.get('/jail')
async def jail(avatar:str=None):

    if not avatar==None:
        await WebCounter('jail')
        
        response = requests.get(avatar)
        image = Image.open(BytesIO(response.content))
        pfp = image.convert("L")
        pfp=pfp.resize((512,512))
        jail=Image.open("image/jail.png")
        pfp.paste(jail,(-10,-10),jail.convert("RGBA"))
        pfp.save("trash_photo/trsh.png")
    
        return FileResponse("trash_photo/trsh.png")


@app.get('/invert')
async def invert(avatar:str=None):
    if not avatar==None:
        await WebCounter('invert')
        
        response = requests.get(avatar)
        image = Image.open(BytesIO(response.content))
        image.save("invert.png")
        pfp = Image.open("invert.png").convert("RGB")
        pfp = ImageOps.invert(pfp)
        pfp.save("trash_photo/invert.png")
        return FileResponse("trash_photo/invert.png")
        #pfp = pfp.open('profile.png')


@app.get('/slap')
async def slap(avatar1:str=None,avatar2:str=None):
  if not avatar1==None:
        await WebCounter('slap')
        
        response=requests.get(avatar1)
        image=Image.open(BytesIO(response.content))
        image.save("avatar.png")
        if not avatar2==None:
     
          response2=requests.get(avatar2)
          image2=Image.open(BytesIO(response2.content))
          image2.save("avatar2.png")
          image=Image.open("avatar.png")
          slap=Image.open("image/slap.png")
          image2=image2.resize((86,86))
          image=image.resize((86,86))
          slap.paste(image,(24,29),image)
          slap.save("trash_photo/slapimg.png")
  return FileResponse("trash_photo/slapimg.png")



@app.get('/premuim/chatbot')
async def chatbot(code:str=None,text:str=None):
  
  with open('apikey.csv', mode='r') as keyfile:
    csv_reader = csv.reader(keyfile, delimiter=',')
    apikey_exists = 0
    for row in csv_reader:
      if row[1]==code:
        apikey_exists=1
        break

  if apikey_exists==1:
    if not text==None:
      
      async with aiohttp.ClientSession() as cs:
        async with cs.get(f'http://api.brainshop.ai/get?bid=158326&key=wcISHu2N1pgIf5Kh&uid=[uid]&msg={text}') as r:
          data = await r.json()
          return {"text":data['cnt']}
          
  else:
    return "Invalid Api Key! Go get one!"
@app.get('/mocktext')
async def mocktext(text:str=None):
    results = []
    if not text==None:
        return {"text":spongemocklower(text)}
@app.get('/reddit')
async def reddit(subreddit:str=None,type:str=None):
      if not subreddit==None:
        if not type==None:
         amogus=type
        else:
          amogus='random'
        
        await WebCounter('reddit')
       
        async with aiohttp.ClientSession() as cs:
          async with cs.get(f"https://www.reddit.com/r/{subreddit}/{amogus}.json") as r:
            
            data = await r.json()
        if amogus=='random':
          name = data[0]['data']['children'][0]['data']['title']
          url = data[0]['data']['children'][0]['data']['url']
          comments = data[0]['data']['children'][0]['data']['num_comments']
          author = data[0]['data']['children'][0]['data']['author']

          is_nsfw = data[0]['data']['children'][0]['data']['over_18']
              
          up = data[0]['data']['children'][0]['data']['score']
          link = data[0]['data']['children'][0]['data']['permalink']
          award=data[0]['data']['children'][0]['data']['total_awards_received']
        else:
          sussy=random.randint(1,26)
          name = data['data']['children'][sussy]['data']['title']
          url = data['data']['children'][sussy]['data']['url']
          comments = data['data']['children'][sussy]['data']['num_comments']
          author = data['data']['children'][sussy]['data']['author']

          is_nsfw = data['data']['children'][sussy]['data']['over_18']
              
          up = data['data']['children'][sussy]['data']['score']
          link = data['data']['children'][sussy]['data']['permalink']
          award=data['data']['children'][sussy]['data']['total_awards_received']          
        return {
        'name':name,
        'url':f"https://reddit.com{link}",
        'comments':comments,
        'upvote':up,
        'is_nsfw':is_nsfw,
        'author':author,
        'awards':award,
        }



@app.get('/rainbow')
async def rainbow_overlay(avatar:str=None):
    if not avatar==None:
    
        response = requests.get(avatar)
        image = Image.open(BytesIO(response.content))
        #if image.tile[0][0] == "gif":
        image=image.convert('RGB')
        pixels=image.load()
        width,height=image.size
        
        for i in range(width):
          for j in range(height):
            n=10
            k=int(j/n)
            pix=pixels[i,j]
            #pix=image.getpixel((i,j))


            r=pix[0]
            g=pix[1]
            b=pix[2]

            if k%3==1:
              nr=r
              ng=0.1*g
              nb=0.1*b
            elif k%3==2:
              nr=0.1*r
              ng=g
              nb=0.1*b
            else:
              nr=0.1*r
              ng=0.1*g
              nb=b
            pixels[i,j]=(int(nr),int(ng),int(nb))
        image.save("trash_photo/profile.png")


        return FileResponse("trash_photo/profile.png")
        #pfp = pfp.open('profile.png')




uvicorn.run(app,host="0.0.0.0",port="8080")
