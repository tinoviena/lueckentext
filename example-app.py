import time
from browser import document, html, ajax
import sys
import json
import CONFIG

#api_new_quiz_url = "http://127.0.0.1:5000/quiz/"
#api_base_url = "http://127.0.0.1:5000"

class Quiz:
   def __init__(self, testee_name, q:dict={}, display_name="Anonymous"):
      self.api_new_quiz_url = f"http://{CONFIG.http_api_ip}:{CONFIG.http_api_port}/quiz/"
      self.api_base_url = f"http://{CONFIG.http_api_ip}:{CONFIG.http_api_port}"
      self.q = q
      self.testee_name = testee_name
      self.log_element = document["log_output"]
      sys.stderr.write("element: {0}".format(self.log_element))
      nb = 0
      app_root_element = document["app"]
      app_element = html.DIV(f" {display_name} ", id="app_"+testee_name, Class="app")
      app_element <= html.BUTTON("Hier klicken für das nächste Wort", id="send_button_"+testee_name).bind("click", self.change)
      app_element <= html.DIV("", id="question_"+testee_name, Class="frage") 
      app_element <= html.DIV(" .... ", id="lösung_"+testee_name, Class="lösung")
      app_root_element <= app_element
      document["send_button_"+testee_name].bind("click", self.change)
   
   def clear_log(self, ev):
      self.log_element.clear()
      self.log_element <= html.BUTTON("Clear").bind("click", self.clear_log)
   #log_element <= html.BUTTON("Clear").bind("click", clear_log)

   def change(self, event):
      self.log(f'pressed {event.target.id}')
      name = self.testee_name

      ajax_url = self.api_new_quiz_url+name
      self.log(f'Calling Ajax {ajax_url}')
      ajax.get(ajax_url,
               blocking=False,
               timeout=7,
               oncomplete=self.display_word)

   def lösung_click_handler(self, event):
      api_get_word_url = self.api_base_url + self.q["word"]
      self.log(f'Calling Ajax {api_get_word_url}')
      ajax.get(api_get_word_url,
               blocking=False,
               timeout=7,
               oncomplete=self.display_word_lösung)

   def display_word_lösung(self, data):
      document["lösung_"+self.testee_name].clear()
      self.log(f"display word lösung: {data.text}")
      j = json.loads(data.text)
      ds = f'{j["infinitiv"]}, {j["imperfekt"]}, {j["perfekt_hilfsverb"]} {j["perfekt_partizip"]}'
      document["lösung_"+self.testee_name] <= html.DIV(ds, Class='lösung_text')

   def known_click_handler(self, event):
      ajax.post(self.api_base_url + self.q["known"],
               blocking=False,
               headers={ "Content-Type": "application/json" },
               data="j",
               timeout=7,
               oncomplete=self.display_known_response)

   def not_known_click_handler(self, event):
      ajax.post(self.api_base_url + self.q["not_known"],
               blocking=False,
               headers={ "Content-Type": "application/json" },
               data="n",
               timeout=7,
               oncomplete=self.display_known_response)

   def display_known_response(self, data):
      stats = json.loads(data.text)
      wort = list(stats.keys())[0]
      gewusst = stats[wort]["known"]
      nicht_gewusst = stats[wort]["not_known"]
      display_text = html.DIV(Class="display_stats")
      display_text <= html.UL()
      display_text <= html.LI(f"Gewusst: {gewusst} mal")
      display_text <= html.LI(f"Nicht gewusst: {nicht_gewusst} mal")
      display_text <= html.LI(f"Last used: {stats[wort]['last_used']}.")
            
      document["lösung_"+self.testee_name] <= html.P() + display_text

   def new_word_click_handler(self, event):
      api_get_new_word_url = self.api_base_url + self.q["add_word"]
      self.log(f"calling new word url {api_get_new_word_url}")
      ajax.get(api_get_new_word_url,
               blocking=False,
               timeout=7,
               oncomplete=self.display_word_lösung)

   def list_words_click_handler(self, event):
      self.log(f"q={self.q}")
      api_stats_url = self.api_base_url + self.q["stats"]
      ajax.get(api_stats_url,
               blocking=False,
               timeout=7,
               oncomplete=self.display_stats)

   def display_stats(self, data):
      document["lösung_"+self.testee_name] <= html.P() + data.text + html.P()

   def display_word(self, ev):
      self.log(ev.text)
      self.q = json.loads(ev.text)
      document["question_"+self.testee_name].clear()
#      row_div = html.DIV(Class="row")
#      row_div <= html.DIV("links", Class="column") + html.DIV(f'{self.q["question"]["question"]}', Class="column text") + html.DIV("rechts", Class="column")
      document["question_"+self.testee_name] <= html.DIV(f'{self.q["question"]["question"]}', Class="text")
      document["question_"+self.testee_name] <= html.BUTTON("Lösung", id="lösung_btn", Class="frage button").bind("click", self.lösung_click_handler)
      document["question_"+self.testee_name] <= html.BUTTON("Gewusst", id="known_btn", Class="frage button").bind("click", self.known_click_handler)
      document["question_"+self.testee_name] <= html.BUTTON("Nicht Gewusst", id="not_known_btn", Class="frage button").bind("click", self.not_known_click_handler)
      document["question_"+self.testee_name] <= html.BUTTON("Neues Wort", id="add_word_btn", Class="frage button").bind("click", self.new_word_click_handler)
      document["question_"+self.testee_name] <= html.BUTTON("Alle Wörter", id="list_words_btn", Class="frage button").bind("click", self.list_words_click_handler)
   
   def log(self, msg):
      document["log_output"] <= html.P() + msg
   

sebastian = Quiz("s", {"test": True}, display_name="Sebastian") # "Sebastian"
#sebastian()
angelo = Quiz("a", {}, display_name="Angelo")
