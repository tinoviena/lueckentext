import src.get_text as get_text
import src.replace as replace
import logging
import json
import base64
import persistence
import urllib.parse
from flask import Flask, render_template, send_from_directory, request, redirect

log = logging.getLogger("app.py")
log.setLevel(level=logging.INFO)

app = Flask(__name__)

@app.route("/test")
def test():
   return "Hello"
@app.route("/web/<path:path>")
def web(path):
  return send_from_directory("web", path)

@app.route("/")
def index():
  html = html_header() + html_body_start()
#  html += '<div id="select_space" class="select_text">Name für den Bereich eingeben: <input id="select_space_input">\n'
#  html += '<button id="select_space_ok_button" class="ok_button">OK</button></div>'
  html += '''
  <p>Diese Webseite macht aus einem deutschen Text einen Lückentext, indem es bestimmtem alle Artikel entfernt. Zur Kontrolle kann man einen beliebigen Artikel in die Lücken einfügen.
  </p>
  <p>Als Ausgangstext kann man den Titel eines deutschsprachigen Wikipediaartikels eingeben, in welchem dann alle bestimmten ARtikel durch Lücken ersetzt werden.
  </p>
  <p>Wähle zunächst einen Namen für deine Benutzung aus. Den Wikipediaartikel kannst du dir auch der nächsten Seite aussuchen, zum Beispiel "Schlaumeier" oder "Lucky Luke".
  </p>
  '''
  html += '''
   <form action="/space" method="get" class="select_text"">
   <div class="select_text">
      <label for="space_id">Name für den Bereich eingeben: </label>
      <input type="text" name="space_id" id="space_id_input" required>
      <input type="submit" value="Los!">
   </div>
   </form>
  '''
  return html

@app.route("/space")
def index_space():
  space_id = request.args.get('space_id')
  return redirect("/spaces/"+space_id, 302)

@app.route("/spaces/<path:space_id>")
def space(space_id):
  article_title = 'Montag'
  html = html_header() + html_body_start()
  html_luecken = wikipedia(article_title)
  html += '<p>Gib hier den Titel eines Artikels aus <a href="https://de.wikipedia.org" target="_blank">de.wikipedia.org</a> ein, zum Beispiel "Montag" oder "Anakin Skywalker" oder den eines <a href="https://de.wikipedia.org/wiki/Spezial:Zuf%C3%A4llige_Seite">zufälligen Artikels</a>.'
  html += '<p><span id="check_result" class="stats animate__backInLeft">Korrekt: 0 inkorrekt: 0 total: 0</span>'
  html += '<div id="select_text" class="select_text">wikipedia artikel <input id="select_text_input" placeholder="Titel eines Wikipedia-Artikels">'
  html += '<button id="ok_button" class="ok_button animate__backInLeftf">OK</button><button id="check_button" class="check_button">Check</button>'
  #html += 'Korrekt: 0, inkorrekt: 0, total: 0'
  html += '</div>'
  html += '<div id="lueckentext" class="lueckentext"></div>'
  html += output_area()
  html += add_script()
  html += "</div></body></html>"    
  return html # render_template("index.html", paras = lupas)

@app.route("/spaces/<path:space>/log", methods = ['POST'])
def space_log(space):
   print("space_log")
   logitem = json.loads(request.get_data())
   logitem["space"] = space

   persistence.save(logitem)
   return "OK"

@app.route("/wikipedia/<path:article_title>")
def wikipedia(article_title):
  article_title = urllib.parse.quote(article_title)
  (html_luecken, replaced) = lueckentext(article_title)
  html_luecken += add_data(article_title, replaced)
  return html_luecken

def lueckentext(article_title :str) -> str:
  ret_html = ""

  ps = get_text.from_wikipedia(article_title)

  log.debug(f'Found {len(ps)} paragraphs')
  replaced = {}
  for i, p in enumerate(ps):
      if (log.level == logging.DEBUG):
        msg = p.text[:80].replace("\n","")
        log.debug(f'{i} ::: {msg}')
      (lueckentext, luecken) = replace.replace(p.text, i)
      if len(luecken):
         replaced[i] = luecken
         log.debug(lueckentext)
         ret_html += f'<p class="">\n{lueckentext}</p>\n'
  return (ret_html, replaced)

def html_header():
  r='''<!DOCTYPE html>
  <html lang="de">
  <title>Lückentexte</title>
  <head>
      <link href="/web/styles.css" rel="stylesheet">
      <link  id="favicon" rel="icon" href="https://cdn.glitch.global/f745eda5-f86f-4ad3-9af0-529f17db8f24/favicon.ico?v=1649580481045" />
      <script src="https://cdn.jsdelivr.net/gh/brython-dev/brython@master/www/src/brython.js"></script>
      <script src="https://cdn.jsdelivr.net/gh/brython-dev/brython@master/www/src/brython_stdlib.js"></script>
      <link href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" rel="stylesheet">
  </head>
  '''
  return r

def html_body_start():
  r ='''
  <body onload="brython()" class="app">
  <div id="all" class="all">
  '''
  return r

def output_area():
  r = '<div id="output" class="output"></div>'
  return r

def add_script():
    r = '''\n  <script type="text/python" src="/web/webapp.py">
    </script>\n
      '''
    return r
    
def add_data(article_title, json_obj):
    r = ''
    json_obj['article_title']=article_title
    message = json.dumps(json_obj)
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    r += f'\n<data id="data" value="{base64_message}">\n'
    return r

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=6000)