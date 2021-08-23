from PIL import Image,ImageOps,ImageFont,ImageDraw
from oauth import Oauth
import csv
import quart
import textwrap
from random import *
import smtplib,ssl,subprocess
import requests
import secrets
import json
import aiohttp
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


@app.route("/image/otter",)
async def otters_img():
  imgList = os.listdir("otter")
  seal = random.choice(imgList)
  return await send_file(f"otter/{seal}", mimetype='image/jpg')
@app.route("/image/dog",)
async def dog_img():
  
  imgList = os.listdir("dogs")
  seal = random.choice(imgList)
  return await send_file(f"dogs/{seal}", mimetype='image/png')


@app.route("/register")
async def api_key_register():
  pass

def WebCounter(page):
       
        with open('test6.csv', mode='w') as keyfile:
            test_writer = csv.writer(keyfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        
            with open('stats.csv', mode='r') as keyfile:
                csv_reader = csv.reader(keyfile, delimiter=',')

                match=0
                # if os.path.getsize("bw.csv") == 0:
                #   test_writer.writerow([ctx.guild.id,"off"])
                # else:
                for row in csv_reader:
                    if row[0] == page:
                        ctr=sum(map(int,row[1]),1)
                        test_writer.writerow([row[0],ctr])
                        match=1
              
                    else:
                      
                      test_writer.writerow([row[0],row[1]])
                    #test_writer.writerow(["me",101])

        if match==0:
           
            with open('test6.csv', mode='a') as keyfile:
                test_reader = csv.writer(keyfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                test_reader.writerow([page, 1])

        os.rename('test6.csv','stats.csv')
 

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
  email=user_object["email"]
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
  await send_email(email,gen_key)
  return f"sucessful your api key is {gen_key}, a email with your api key will also be sent shortly..."




@app.route('/json/dogs', methods=['GET'])
async def Dfact():
    with open("api-things/dfact.json") as json_file:
      data = json.load(json_file)
      Rdata=random.choice(data)
    return quart.jsonify(Rdata)


@app.route('/json/quote', methods=['GET'])
async def qoutes():

    WebCounter('quote')
    with open("api-things/qoutes.json") as json_file:
      data = json.load(json_file)
      Rdata=random.choice(data["quotes"])

    return quart.jsonify(Rdata)

@app.route('/greyscale',methods=['GET'])
async def grey_scale():
  try:
    
    if 'avatar' in quart.request.args:

        WebCounter('greyscale')
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
        WebCounter('wanted')
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
 
@app.route('/leaderboard',methods=['GET'])
async def leaderboard():
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
        WebCounter('trash')
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

@app.route('/hitler',methods=['GET'])
async def hiter():
      if 'avatar' in quart.request.args:
        WebCounter('hitler')
        Lavatar = str(quart.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        image.save("avatar.png")
        pfp=Image.open("avatar.png")
        pfp=pfp.resize((160,160))
        trash=Image.open("image/hitler.png")
        trash.paste(pfp,(29,32),pfp.convert("RGBA"))
        trash.save("trash_photo/hitlerpic.png")
        return await send_file("trash_photo/hitlerpic.png", mimetype='image/png')


      else:
        return await page_not_found(404)



@app.route('/invert',methods=['GET'])
async def invert():
    if 'avatar' in quart.request.args:
        WebCounter('invert')
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
        WebCounter('slap')
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
        WebCounter('alert')

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
        WebCounter('billy')
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

@app.route('/premuim/chatbot')
async def chatbot():
  api_key=str(quart.request.args['code'])
  with open('apikey.csv', mode='r') as keyfile:
    csv_reader = csv.reader(keyfile, delimiter=',')
    apikey_exists = 0
    for row in csv_reader:
      if row[1]==api_key:
        apikey_exists=1
        break

  if apikey_exists==1:
    if 'text' in quart.request.args:
      text = str(quart.request.args['text'])
      async with aiohttp.ClientSession() as cs:
        async with cs.get(f'http://api.brainshop.ai/get?bid=158326&key=wcISHu2N1pgIf5Kh&uid=[uid]&msg={text}') as r:
          data = await r.json()
          return quart.jsonify(text=data["cnt"])
  else:
    return "Invalid Api Key! Go get one!"






@app.route('/pacman/text',methods=['GET'])
async def pacman():
    if 'text' in quart.request.args:
        text = str(quart.request.args['text'])

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

async def send_email(reciver,apikey):
  port = 465  # For SSL
  smtp_server = "smtp.gmail.com"
  sender_email = "aarav.singhania50@gmail.com"  # Enter your address
  receiver_email = reciver  # Enter receiver address

  message = f"""\
  Subject: SomeApi Key

  Hello! Thanks for signing up with SomeApi!
  Your Api Key is {apikey}."""

  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, "savecup11")
      server.sendmail(sender_email, receiver_email, message)


@app.route('/doc')
async def docpage():
    return await render_template("docpage.html")


@app.route('/policy-thing')
async def policythings():
    return await render_template("TOS.html")



@app.route('/credits')
async def creduts():
    return await render_template("credits.html")




@app.route("/dooltest")
async def iscool():
    resp = await make_response("hello") #here you could use make_response(render_template(...)) too
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app.run(host="0.0.0.0",port=80,)