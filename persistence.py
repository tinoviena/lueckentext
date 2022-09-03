from deta import Deta
from os import environ
from datetime import datetime
import hashlib

deta = Deta(environ["deta_project_key"])
luecken_logs = deta.Base("luecken_logs")
cache = []

def save(any):
#   m = hashlib.sha256()
#   m.update(str(any).encode())
   del(any['datetime'])
   print("persistence.save before: "+str(any))
   key = str(hash(str(any)))
   if key in cache:
      print(f"found {key} in cache, pass")
   else:
      any["key"] = key #m.digest()
      any["timestamp"] = str(datetime.now())
      print("persistence.save after: "+str(any))
      try:
         luecken_logs.insert(any)
      except Exception as e:
         print(" Deta DB transation failed. "+str(e))
#         print(print(sys.exc_info()))
      cache.append(key)

