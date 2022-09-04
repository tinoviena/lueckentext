from deta import Deta
from os import environ
import sys
from datetime import datetime
import hashlib

dpk = environ.get("deta_project_key")
if(dpk):
   deta = Deta(environ["deta_project_key"])
else:
   print("\n==========================================\n    ATTENTION!!         \n==========================================\nPlease set an environment variable\n called 'deta_project_key'\n containing the deta project key\n you can generate in your\n Deta dashboard https://web.deta.sh/.\n==========================================")
   sys.exit(100)

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

