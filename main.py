from PIL import Image,ImageOps,ImageFont,ImageDraw
from oauth import Oauth
import csv
import quart
import textwrap
from random import *
import requests
import secrets
import json
import urllib.parse as urlparse
from urllib.parse import parse_qs
from io import BytesIO
from quart import *
from defstuff import *
import os
app = Quart(__name__)
async def Schema():
  return "a"
async def valueError():
  return await render_template("valueError.html")


with open("api-things/qoutes.json") as json_file:
    data = json.load(json_file)
    dataLength = len(data)




@app.route("/")
async def main():
  return await render_template("index.html")
@app.route("/user/question")
async def cooluser():
  return await render_template("userquestion.html")
@app.route("/user/page")
async def userpage():
  return await render_template("userscreen.html")
 
@app.route("/theme")
async def themes():
  return await render_template("theme.html")


@app.route("/otter/image",)
async def otters_img():
  imgList = os.listdir("/image/otter")
  seal = random.choice(imgList)
  return await send_file(f"/image/otter/{seal}.jpg", mimetype='image/jpg')


@app.route("/register")
async def api_key_register():
  pass
@app.route("/register/discord",methods=['get'])
async def discord_url():
  discord_url_link='https://discord.com/api/oauth2/authorize?client_id=873068029024534538&redirect_uri=https%3A%2F%2Fsomeapi.xyz%2Fregister%2Fdiscord&response_type=code&scope=email%20identify%20guilds'

  url = "https://discord.com/api/users/@me"
  access_token = Oauth.get_access_token(str(quart.request.args['code']))
  
  headers = {"Authorization": f"Bearer {access_token}"}
  gen_key=secrets.token_hex(20)
  user_object = requests.get(url = url, headers = headers).json()
  print("user objetc",user_object)
  userid=user_object["id"]
  with open('apikey.csv', mode='r') as keyfile:
    csv_reader = csv.reader(keyfile, delimiter=',')
    userid_exists = 0
    for row in csv_reader:
      if row[0]==userid:
        print(f"user id:{userid} already exists ")
        userid_exists=1
        return "Only 1 api key per User, You already have one"
        #break
        
  if userid_exists==0:
    with open('apikey.csv', mode='a') as keyfile:
      key_writer = csv.writer(keyfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      key_writer.writerow([userid, gen_key,])
    
  return f"sucessful your api key is {genkey}"



@app.route('/json/dogs', methods=['GET'])
async def Dfact():     
    with open("api-things/dfact.json") as json_file:
      data = json.load(json_file)
      Rdata=random.choice(data)
    return quart.jsonify(Rdata)


@app.route('/json/qoute', methods=['GET'])
async def qoutes():     
    with open("api-things/qoutes.json") as json_file:
      data = json.load(json_file)
      Rdata=random.choice(data["quotes"])

    return quart.jsonify(Rdata)
@app.route('/greyscale',methods=['GET'])
async def grey_scale():
  try:
    if 'avatar' in quart.request.args:
        Lavatar = str(quart.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        pfp = image.convert("L")
        pfp.save("trash_photo/greyscale.png")
        return await send_file("trash_photo/greyscale.png", mimetype='image/png')
        #pfp = pfp.open('profile.png')
    else:
      return await page_not_found(404)
  except ValueError:
     return await Schema()

@app.route('/wanted',methods=['GET'])
async def wanted():
    if 'avatar' in quart.request.args:
        Lavatar = str(quart.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        image.save("avatar.png")
        pfp=Image.open("avatar.png")
        pfp=pfp.resize((177,177))
        wanted=Image.open("image/wanted.jpg")
        wanted.paste(pfp,(120,212))
        wanted.save("trash_photo/wanted2.jpg")
        return await send_file("trash_photo/wanted2.jpg", mimetype='image/jpg')
 

    else:
      return await page_not_found(404)


@app.route('/trash',methods=['GET'])
async def trash():
      if 'avatar' in quart.request.args:
        Lavatar = str(quart.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        image.save("avatar.png")
        pfp=Image.open("avatar.png")
        pfp=pfp.resize((170,170))
        trash=Image.open("image/trash.png")
        trash.paste(pfp,(140,145),pfp.convert("RGBA"))
        trash.save("trash_photo/trashpic.png")
        return await send_file("trash_photo/trashpic.png", mimetype='image/png')
 

      else:
        return await page_not_found(404)



@app.route('/invert',methods=['GET'])
async def invert():
    if 'avatar' in quart.request.args:
        Lavatar = str(quart.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        image.save("invert.png")
        pfp = Image.open("invert.png").convert("RGB")
        pfp = ImageOps.invert(pfp)
        pfp.save("trash_photo/invert.png")
        return await send_file("trash_photo/invert.png", mimetype='image/png')
        #pfp = pfp.open('profile.png')
    else:
      return await page_not_found(404)
@app.route('/youtube',methods=['GET'])
async def youtube():
    if 'avatar' in quart.request.args:
        Lavatar = str(quart.request.args['avatar'])
        response=requests.get(Lavatar)
        image=Image.open(BytesIO(response.content))
        image.save("avatar.png")
        if 'title' in quart.request.args:
          title=str(quart.request.args['title'])
          if 'text' in quart.request.args:
            text = str(quart.request.args['text'])

            youtube=Image.open("image/youtube-comment.png")

            image=Image.open("avatar.png")
            image = mask_circle_transparent(image, 0)
            image=image.resize((86,86))
            youtube.paste(image,(24,29),image)
            youtube.save("trash_photo/youtube.png")
            return await send_file("trash_photo/youtube.png", mimetype='image/png')
            


 

    else:
      return await page_not_found(404)
@app.route('/slap',methods=['GET'])
async def slap():
  if 'avatar1' in quart.request.args:
        Lavatar = str(quart.request.args['avatar1'])
        response=requests.get(Lavatar)
        image=Image.open(BytesIO(response.content))
        image.save("avatar.png")
        if 'avatar2' in quart.request.args:
          Lavatar2 = str(quart.request.args['avatar2'])
          response2=requests.get(Lavatar2)
          image2=Image.open(BytesIO(response2.content))
          image2.save("avatar2.png")
          image=Image.open("avatar.png")
          slap=Image.open("image/slap.png")
          image2=image2.resize((86,86))
          image=image.resize((86,86))
          slap.paste(image,(24,29),image)
          slap.save("trash_photo/slapimg.png")
  return await send_file("trash_photo/slapimg.png", mimetype='image/png')

@app.route('/alert',methods=['GET'])
async def alert():
    if 'text' in quart.request.args:
        text = str(quart.request.args['text'])


        alert=Image.open("image/alert.jpg")
        font=ImageFont.truetype("image/arial.ttf",32)
        draw=ImageDraw.Draw(alert)
        draw.text((55,566),text,(0,0,0),font=font)
        alert.save("trash_photo/alert.png")
        return await send_file("trash_photo/alert.png", mimetype='image/png')
 

    else:
      return await page_not_found(404)
@app.route('/billy',methods=['GET'])
async def billy():
    if 'text' in quart.request.args:
        text = str(quart.request.args['text'])
        alert=Image.open("image/billy.png")
        font=ImageFont.truetype("image/arial.ttf",20)
        draw=ImageDraw.Draw(alert)
        draw.text((26,291),text,(0,0,0),font=font)
        alert.save("trash_photo/billy2.png")
        return await send_file("trash_photo/billy2.png", mimetype='image/png')
 

    else:
      return await page_not_found(404)


@app.route('/god_temp',methods=['GET'])
async def god_temp():
    if 'text' in quart.request.args:
        text = str(quart.request.args['text'])


        alert=Image.open("image/god-meme-template.jpg")
        font=ImageFont.truetype("image/arial.ttf",32)
        draw=ImageDraw.Draw(alert)
        draw.text((93,350),text,(0,0,0),font=font)
        alert.save("trash_photo/god_temp.png")
        return await send_file("trash_photo/god_temp.png", mimetype='image/png')
 

    else:
      return await page_not_found(404)

@app.route('/biden',methods=['GET'])
async def biden():
    if 'text' in quart.request.args:
        text = str(quart.request.args['text'])


        alert=Image.open("image/biden.png")
        font=ImageFont.truetype("image/arial.ttf",32)
        draw=ImageDraw.Draw(alert)
        draw.text((30,110),text,(0,0,0),font=font)
        alert.save("trash_photo/biden.png")
        return await send_file("trash_photo/biden.png", mimetype='image/png')
 

    else:
      return await page_not_found(404)



@app.route('/pacman/text',methods=['GET'])
async def pacman():
    if 'text' in quart.request.args:
        text = str(quart.request.args['text'])
        print(len(text),text[10],text[0])
        lines = textwrap.wrap(text, width=10)
        

        image=Image.open("image/blankimage.png")
        width, height = image.size
        print(width,height)
        font=ImageFont.truetype("api-things/CrackMan.tff",120)
        draw=ImageDraw.Draw(image)

        y_text = 50
        for line in lines:
          width, height = font.getsize(line)
          print(width,height,y_text)
          
          print(line)
          draw.text(((992 - width) / 2, y_text), line,(0,0,0), font=font)
          #draw.text((26,265),line,(0,0,0),font=font)
          y_text += height
        #draw.text((26,265),text,(0,0,0),font=font)
        image.save("trash_photo/pacmantext.png")
        return await send_file("trash_photo/pacmantext.png", mimetype='image/png')
 

    else:
      return await page_not_found(404)


@app.route('/mocktext', methods=['GET'])
async def mocktext():
    results = []
    if 'text' in quart.request.args:
        text = str(quart.request.args['text'])

        
        
    else:
        return await page_not_found(404)
        
    return quart.jsonify(text=spongemocklower(text))


@app.route('/wasted',methods=['GET'])
async def wasted():
    if 'avatar' in quart.request.args:
        Lavatar = str(quart.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        
        pfp=ImageOps.grayscale(image).convert("RGBA")
        wasted=Image.open("image/wasted.png")
       
        wasted=wasted.resize((320,400))
        pfp=pfp.resize((248,248))
        #pfp=pfp.resize((512,512))
        pfp.paste(wasted, (-35, -70), wasted.convert("RGBA"))
        pfp.save("trash_photo/wasted2.gif")
        return await send_file("trash_photo/wasted2.gif", mimetype='image/gif')
        #pfp = pfp.open('profile.png')
    else:
      return await page_not_found(404)

@app.route('/rainbow',methods=['GET'])
async def rainbow_overlay():
    if 'avatar' in quart.request.args:
        Lavatar = str(quart.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        #if image.tile[0][0] == "gif":


        image=image.convert('RGB') 
        pixels=image.load()
        width,height=image.size 
        print(image.format,image.mode,image.palette,image.info)
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
            
        
        return await send_file("trash_photo/profile.png", mimetype='image/png')
        #pfp = pfp.open('profile.png')
    else:
      return await page_not_found(404)



@app.errorhandler(404)
async def page_not_found(e):
    return await render_template("404.html")

#@app.errorhandler()


@app.route('/doc')
async def docpage():
    return await render_template("docpage.html")


@app.route('/policy-thing')
async def policythings():
    return await render_template("TOS.html")



@app.route('/credits')
async def creduts():
    return await render_template("credits.html")


 

app.run(host="0.0.0.0",port=80,debug=True)