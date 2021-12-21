import os
import discord
import requests
import json
import random
import math
import time
import pathlib
from replit import db
from alive_pls import keep_alive

def timsolonbe(tong, hieu):
  return ((tong+hieu)/2,(tong-hieu)/2)

def giaithua(n):
  n = int(n)
  if (n == 0): return (1)
  if (n < 0): return -1
  tich = 1
  for i in range(1,n+1):
    tich *= i
  return (tich)

def gtbt(s):
  return eval(s)

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def hexToBinary(n):
    return bin(int(n,16)).replace("0b", "")

def decimalToHex(n):
    return hex(n).replace("0x", "")

def binToHex(n):
    n = int(n,2)
    return hex(n).replace("0x", "")

def binaryToDecimal(n):
    return int(n,2)

def anyToDecimal(n,b):
  return int(n,b);

# https://www.codespeedy.com/inter-convert-decimal-and-any-base-using-python/
def dec_to_base(num,base):  #Maximum base - 36
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters
        num //= base

    base_num = base_num[::-1]  #To reverse the string
    return base_num

invalid_msg = ['Invalid input','Sir, why you do that?','I believe that there is no cake here', 'Some thing went so wrong','Check your input pls','Put trash in the recycle bin pls','404 not found .-.','1+1 = 3 ?!','Do you brain divided by zero?','What is discord???','Can you do it yourself? I am lazy.','||[REDACTED]||','The Earth is flat ?!?!?!!','Yeet!','Banana?','Do you want some cookie?','Hot potato! You have been tagged.','Boo!','Spooky spooky skeleton...','Maybe some good old /helpme will help you']


client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} say hello to your server,o/".format(client))
    await client.change_presence(activity=discord.Game('/helpme'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    msg.strip()
    if msg.startswith('/sayhi'):
        await message.channel.send('Hello!')
        return

    if msg.startswith('/dem'):
        s = msg[5:]
        await message.channel.send(len(s))
        return

    if msg.startswith('/sqrt'):
        x = msg.split()[1]
        if (x.isnumeric()):
          await message.channel.send(math.sqrt(int(x)))
        else:
          await message.channel.send(random.choice(invalid_msg))
        return


    if msg.startswith('/pow'):
      x = msg.split()[1]
      y = msg.split()[2]
      if (x.isnumeric() & y.isnumeric()):
          await message.channel.send(int(int(x)**int(y)))
      else:
          await message.channel.send(random.choice(invalid_msg))
      return

    if msg.startswith('/tinh'):
      try:
        eval(msg[6:])
      except:
        await message.channel.send(random.choice(invalid_msg))
      else:
        await message.channel.send(eval(msg[6:]))
      return

    if msg.startswith('/divmod'):
      x = msg.split()[1]
      y = msg.split()[2]
      if (x.isnumeric() & y.isnumeric()):
          await message.channel.send(divmod(int(x),int(y)))
      else:
          await message.channel.send(random.choice(invalid_msg))
      return

    if msg.startswith('/randint'):
      x = msg.split()[1]
      y = msg.split()[2]
      if (x.isnumeric() & y.isnumeric()):
          await message.channel.send(random.randint(int(x),int(y)+1))
      else:
          await message.channel.send(random.choice(invalid_msg))
      return

    if msg.startswith('/timso'):
      x = msg.split()[1]
      y = msg.split()[2]
      if (x.isnumeric() & y.isnumeric()):
          await message.channel.send(timsolonbe(int(x),int(y)))
      else:
          await message.channel.send(random.choice(invalid_msg))
      return
      

    if msg.startswith('/giaithua'):
      x = msg.split()[1]
      if (x.isnumeric()):
          await message.channel.send(giaithua(msg.split()[1]))
      else:
          await message.channel.send(random.choice(invalid_msg))
      return

    if msg.startswith('/tong'):
      x = msg.split()[1]
      if (x.isnumeric()):
          x = int(x)
          await message.channel.send(int(x*(x+1)/2))
      else:
          await message.channel.send(random.choice(invalid_msg))
      return

    if msg.startswith('/bin'):
      x = msg.split()[1]
      if (x.isnumeric()):
          x = int(x)
          await message.channel.send(decimalToBinary(x))
      else:
          await message.channel.send(random.choice(invalid_msg))
      return
    if msg.startswith('/hex'):
      x = msg.split()[1]
      if (x.isnumeric()):
          x = int(x)
          await message.channel.send(decimalToHex(x))
      else:
          await message.channel.send(random.choice(invalid_msg))
      return

    if msg.startswith('/htob'):
      x = msg.split()[1]
      try:
        hexToBinary(x)
      except:
        await message.channel.send(random.choice(invalid_msg))
      else:
          await message.channel.send(hexToBinary(x))
      return

    if msg.startswith('/btoh'):
      x = msg.split()[1]
      try:
        binToHex(x)
      except:
        await message.channel.send(random.choice(invalid_msg))
      else:
          await message.channel.send(binToHex(x))
      return

    if msg.startswith('/dtob'):
      x = msg.split()[1]
      b = msg.split()[2]
      # x = int(x)
      # print(dec_to_base(x,b))
      try:
        x = int(x)
        b = int(b)
        dec_to_base(x,b)
      except:
        await message.channel.send(random.choice(invalid_msg))
      else:
        x = int(x)
        b = int(b)
        await message.channel.send(dec_to_base(x,b))
      return

    if msg.startswith('/btod'):
      x = msg.split()[1]
      b = msg.split()[2]
      try:
        b = int(b)
        anyToDecimal(x,b)
      except:
        await message.channel.send(random.choice(invalid_msg))
      else:
        b = int(b)
        await message.channel.send(anyToDecimal(x,b))
      return
    
    if msg.startswith('/dec'):
      x = msg.split()[1]
      try:
        binaryToDecimal(x)
      except:
        await message.channel.send(random.choice(invalid_msg))
      else:
          await message.channel.send(binaryToDecimal(x))
      return

# """
#     if (msg.startswith("?goi_thang_anh")):
#       await message.delete()   
#       await message.channel.send("<@633542840768528405>")
#       print(client.user.name)
#       return 
    

#     hmm = os.environ['hmmm']
#     if (msg.startswith(hmm)):
#       await message.delete()   
#       await message.channel.send("<@791642641875468308>")
#       print(client.user.name)
#       return 
# """
    if msg.startswith('/timeis'):
      localtime = time.localtime()
      result = time.strftime("%I:%M:%S %p", localtime)
      await message.channel.send(result)
      return
    if msg.startswith('/create'):
      name = msg.split()[1]
      content = msg[(len(name) + 1 + 7 + 1):]
      if (name in db.keys()):
        await message.channel.send("Câu lệnh đã tồn tại. Xin vui lòng chọn tên khác.")
        return
      if (name[0] != '?'):
        await message.channel.send("Câu lệnh không hợp lệ, vui lòng thử lại.")
      else:
        db[name] = content
        await message.channel.send("Câu lệnh " + name + " đã tạo thành công!")
      return

    if msg.startswith('/del'):
      name = msg.split()[1]
      if (name in db.keys()):
        del db[name]
        await message.channel.send("Đã xoá câu lệnh " + name + " !")
      else:
        await message.channel.send("Không tìm thấy câu lệnh!")
      return

    if msg.startswith('/list'):
      kt = 0
      s = "```"
      for name in db.keys():
        if (name[0] == '?'):
          s += name
          s += "\n"
          kt += 1
      s += "```"
      if kt == 0:
        await message.channel.send("Không tìm thấy câu lệnh nào hết!")
      else:
        await message.channel.send("Danh sách các câu lệnh(" + str(kt) + "câu lệnh):")
        # f = open("list.txt","w");
        # f.write(s)
        await message.channel.send(s)
      return

    if msg.startswith("?"):
      msg = msg.split()[0];
      if (msg in db.keys()):
         await message.channel.send(db[msg]);
      return

    # if msg.startswith('/tkb'):
    #   await message.channel.send('Here you go!')
    #   await message.channel.send(file = discord.file('tkb.png'))

    if msg.startswith('/helpme'):
      await message.channel.send(file=discord.File('help.txt'))
      return
    
keep_alive()
TOKEN = os.environ['botToken']
client.run(TOKEN)



