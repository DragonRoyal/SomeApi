from PIL import Image,ImageOps,ImageFont,ImageDraw
import flask
import textwrap
from random import randrange
import requests

import json
from io import BytesIO
from flask import *
from defstuff import *
import os
app = flask.Flask(__name__)
def Schema():
  return "a"
def valueError():
  return render_template("valueError.html")

with open("api-things/dfact.json") as json_file:
    data = json.load(json_file)
    dataLength = len(data)

@app.route('/example')
def example():
   return '{"name":"Bob"}'
@app.route("/")
def main():
  return render_template("index.html")
@app.route("/user/question")
def cooluser():
  return render_template("userquestion.html")
@app.route("/user/page")
def userpage():
  return render_template("userscreen.html")
 
  
@app.route("/otter/image",)
def otters_img():
  imgList = os.listdir("/image/otter")
  seal = random.choice(imgList)
  return send_file(f"/image/otter/{seal}.jpg", mimetype='image/jpg')





@app.route('/dogs/fact', methods=['GET'])
def api_number():
  results = []
  try:
    if 'number' in flask.request.args:
        number = int(flask.request.args['number'])
        for _ in range(number):
            results.append(data[randrange(dataLength)])
    elif 'index' in flask.request.args:
        requestIndex = int(flask.request.args['index'])
        if requestIndex >= 0 and requestIndex < dataLength:
            results.append(data[requestIndex])
  except ValueError:
    return valueError()

        
    return flask.jsonify(results)
@app.route('/greyscale',methods=['GET'])
def grey_scale():
  try:
    if 'avatar' in flask.request.args:
        Lavatar = str(flask.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        pfp = image.convert("L")
        pfp.save("trash_photo/greyscale.png")
        return send_file("trash_photo/greyscale.png", mimetype='image/png')
        #pfp = pfp.open('profile.png')
    else:
      return page_not_found(404)
  except:
    return Schema()
@app.route('/wanted',methods=['GET'])
def wanted():
    if 'avatar' in flask.request.args:
        Lavatar = str(flask.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        image.save("avatar.png")
        pfp=Image.open("avatar.png")
        pfp=pfp.resize((177,177))
        wanted=Image.open("image/wanted.jpg")
        wanted.paste(pfp,(120,212))
        wanted.save("trash_photo/wanted2.jpg")
        return send_file("trash_photo/wanted2.jpg", mimetype='image/jpg')
 

    else:
      return page_not_found(404)


@app.route('/trash',methods=['GET'])
def trash():
      if 'avatar' in flask.request.args:
        Lavatar = str(flask.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        image.save("avatar.png")
        pfp=Image.open("avatar.png")
        pfp=pfp.resize((170,170))
        trash=Image.open("image/trash.png")
        trash.paste(pfp,(140,145),pfp.convert("RGBA"))
        trash.save("trash_photo/trashpic.png")
        return send_file("trash_photo/trashpic.png", mimetype='image/png')
 

      else:
        return page_not_found(404)



@app.route('/invert',methods=['GET'])
def invert():
    if 'avatar' in flask.request.args:
        Lavatar = str(flask.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        image.save("invert.png")
        pfp = Image.open("invert.png").convert("RGB")
        pfp = ImageOps.invert(pfp)
        pfp.save("trash_photo/invert.png")
        return send_file("trash_photo/invert.png", mimetype='image/png')
        #pfp = pfp.open('profile.png')
    else:
      return page_not_found(404)
@app.route('/youtube',methods=['GET'])
def youtube():
    if 'avatar' in flask.request.args:
        Lavatar = str(flask.request.args['avatar'])
        response=requests.get(Lavatar)
        image=Image.open(BytesIO(response.content))
        image.save("avatar.png")
        if 'title' in flask.request.args:
          title=str(flask.request.args['title'])
          if 'text' in flask.request.args:
            text = str(flask.request.args['text'])

            youtube=Image.open("image/youtube-comment.png")

            image=Image.open("avatar.png")
            image = mask_circle_transparent(image, 0)
            image=image.resize((86,86))
            youtube.paste(image,(24,29),image)
            youtube.save("trash_photo/youtube.png")
            return send_file("trash_photo/youtube.png", mimetype='image/png')
            


 

    else:
      return page_not_found(404)


@app.route('/alert',methods=['GET'])
def alert():
    if 'text' in flask.request.args:
        text = str(flask.request.args['text'])


        alert=Image.open("image/alert.jpg")
        font=ImageFont.truetype("image/arial.ttf",32)
        draw=ImageDraw.Draw(alert)
        draw.text((55,566),text,(0,0,0),font=font)
        alert.save("trash_photo/alert.png")
        return send_file("trash_photo/alert.png", mimetype='image/png')
 

    else:
      return page_not_found(404)
@app.route('/billy',methods=['GET'])
def billy():
    if 'text' in flask.request.args:
        text = str(flask.request.args['text'])
        alert=Image.open("image/billy.png")
        font=ImageFont.truetype("image/arial.ttf",20)
        draw=ImageDraw.Draw(alert)
        draw.text((26,291),text,(0,0,0),font=font)
        alert.save("trash_photo/billy2.png")
        return send_file("trash_photo/billy2.png", mimetype='image/png')
 

    else:
      return page_not_found(404)


@app.route('/god_temp',methods=['GET'])
def god_temp():
    if 'text' in flask.request.args:
        text = str(flask.request.args['text'])


        alert=Image.open("image/god-meme-template.jpg")
        font=ImageFont.truetype("image/arial.ttf",32)
        draw=ImageDraw.Draw(alert)
        draw.text((93,350),text,(0,0,0),font=font)
        alert.save("trash_photo/god_temp.png")
        return send_file("trash_photo/god_temp.png", mimetype='image/png')
 

    else:
      return page_not_found(404)

@app.route('/biden',methods=['GET'])
def biden():
    if 'text' in flask.request.args:
        text = str(flask.request.args['text'])


        alert=Image.open("image/biden.png")
        font=ImageFont.truetype("image/arial.ttf",32)
        draw=ImageDraw.Draw(alert)
        draw.text((30,110),text,(0,0,0),font=font)
        alert.save("trash_photo/biden.png")
        return send_file("trash_photo/biden.png", mimetype='image/png')
 

    else:
      return page_not_found(404)



@app.route('/pacman/text',methods=['GET'])
def pacman():
    if 'text' in flask.request.args:
        text = str(flask.request.args['text'])
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
        return send_file("trash_photo/pacmantext.png", mimetype='image/png')
 

    else:
      return page_not_found(404)


@app.route('/mocktext', methods=['GET'])
def mocktext():
    results = []
    if 'text' in flask.request.args:
        text = str(flask.request.args['text'])

        
        
    else:
        return page_not_found(404)
        
    return flask.jsonify(text=spongemocklower(text))


@app.route('/wasted',methods=['GET'])
def wasted():
    if 'avatar' in flask.request.args:
        Lavatar = str(flask.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        
        pfp=ImageOps.grayscale(image).convert("RGBA")
        wasted=Image.open("image/wasted.png")
       
        wasted=wasted.resize((320,400))
        pfp=pfp.resize((248,248))
        #pfp=pfp.resize((512,512))
        pfp.paste(wasted, (-35, -70), wasted.convert("RGBA"))
        pfp.save("trash_photo/wasted2.gif")
        return send_file("trash_photo/wasted2.gif", mimetype='image/gif')
        #pfp = pfp.open('profile.png')
    else:
      return page_not_found(404)

@app.route('/rainbow',methods=['GET'])
def rainbow_overlay():
    if 'avatar' in flask.request.args:
        Lavatar = str(flask.request.args['avatar'])
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
            
        
        return send_file("trash_photo/profile.png", mimetype='image/png')
        #pfp = pfp.open('profile.png')
    else:
      return page_not_found(404)



@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

#@app.errorhandler()


@app.route('/doc')
def docpage():
    return render_template("docpage.html")


@app.route('/policy-thing')
def policythings():
    return render_template("TOS.html")



@app.route('/credits')
def creduts():
    return render_template("credits.html")



app.run(host="0.0.0.0",port=80,debug=True)