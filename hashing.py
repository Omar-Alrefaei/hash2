import hashlib
print ("=========================================================")
print ("Hashing cheacker [1] , Hash length [2] , Hash type [3] " )
print ("MD5 Encrypt [4] ")
print ("=========================================================")

choose = input ("please choose option : " )
if choose == '1' :
      hash1 = input (" Enter Hash1 : " )
      hash2 = input  (" Enter Hash2 : " )
      if hash1 == hash2 :
           print (" The Hash is clean ")
      else :
           print (" The Hash is virus ")
if choose == '2' :
      length = input ("Enter your Hash : " )
      print ("The Hash length is : " , len(length) )      

if choose == '3' :
      type = input ("Enter your Hash : " )
      length = len(type)
      if length == 32 :
           print (" Your Hash is [MD5] ")
      if length == 40 :
           print (" Your Hash is [SHA1] ")
      if length == 64 :
           print (" Your Hash is [SHA256] ")
      else  :
          print (" Wrong Hash ")
if choose == '4' :
      word = input ("Enter Your Text : ")
      md5 = hashlib.md5(word.encode())
      print (md5.hexdigest())    
      


