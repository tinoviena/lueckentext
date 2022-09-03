from browser import document, html, ajax
import json
import base64
from datetime import datetime
import functools

DEBUG = False
'''id of the span, which is currently in focus, i.e. editable'''
CURRENT_FOCUS = 0
ARTICLE_TITLE = ''

def log(msg):
#   document <= html.P()
#   document <= str(msg)
   pass

def get_data():
    base64_message = document.select('data')[0].value

    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    data = json.loads(message)
    global ARTICLE_TITLE 
    ARTICLE_TITLE = data["article_title"]
    del data["article_title"]
    return data

def compare(ev):
    given_answers = []
    spans = document.select('span.luecke')
    given_answers   = [x.text for x in spans]
    correct_answers = []
    correct_answers = functools.reduce(lambda x,y : x+y, get_data().values())
    correct_answers = list(map(lambda x : x[0], correct_answers))
    if DEBUG:
        document <= html.P()
        document <= str(len(given_answers)) 
        document <= html.P() + given_answers # list(map(lambda x : f'{x.text} ', spans))
        document <= html.P() + str(len(correct_answers)) 
        document <= html.P() + correct_answers #list(map(lambda x : f'{x[0]} ', get_data()["0"]))

    checks = []
    correct_count = 0
    incorrect_count = 0
    for i, s in enumerate(spans):
        #document <= html.P() + f'{a.strip()} == {correct_answers[i].strip()}'
        a = s.text
        checks.append(a.strip() == correct_answers[i].strip())
        if a.strip() == correct_answers[i].strip():
            s.className = "luecke correct"
            correct_count += 1
        else:
            s.className = "luecke incorrect"
            incorrect_count += 1
    document.select('#output')[0].text = f"Korrekt: {correct_count}, inkorrekt: {incorrect_count}, total: {correct_count+incorrect_count}"
    document.select('#check_result')[0].text = f'Korrekt: {correct_count} inkorrekt: {incorrect_count} total: {correct_count+incorrect_count}'
    global ARTICLE_TITLE
    log_record = {
       'correct': correct_count,
       'incorrect': incorrect_count,
       'total': correct_count+incorrect_count,
       'article_title': ARTICLE_TITLE,
       'datetime': str(datetime.now())
    }
    log(log_record)
    ajax.post(document.URL+"/log", mode="json", data=json.dumps(log_record))
    #document.select('#check_result')[0].className += ' w3-animate-opacity'
    if DEBUG:
        document <= html.P()
        document <= str(checks)

def clear_span(ev):
    ev.target.text = ev.target.text
    ev.target.className = "focus luecke"

def unclear_span(ev):
    ev.target.text = ev.target.text.replace("_","")
    ev.target.className = "luecke" #ev.target.className.replace("focus","")

    if ev.target.text == "":
        ev.target.text = "___"
    check_span(ev)

def check_span(ev):
    position = ev.target.id.split(":") # sth like 0:01, 4:13, ...
    para = position[0]
    luecke = int(position[1]) # starts with 0
    duple = get_data()[para][luecke-1][0]
    solution = str(duple)

    if (ev.target.text == solution):
        ev.target.className = "luecke correct"
    else:
        ev.target.className = "luecke incorrect"
    compare(ev)

def get_article_from_input(ev):
   input_text = document.select('#select_text_input')[0]
   #document.select('#output')[0] <= input_text.value
   ajax.get(f"/wikipedia/{input_text.value}", oncomplete=show_article)

def get_article(ev):
   ajax.get("/wikipedia/Reise_um_die_Erde_in_80_Tagen", oncomplete=show_article)

def show_article(req):
   global CURRENT_FOCUS
   CURRENT_FOCUS = 0
   luete = document.select('#lueckentext')[0]
   luete.html = req.text
   luecken = document.select('span.luecke')
   for s in luecken: # spans with class 'luecke'
   #    s.bind("click", clear_span) 
      s.bind("focus", clear_span) 
   #    s.bind("input", clear_span) 
      s.bind("blur", unclear_span) 
   document.select('#check_result')[0].text = f'Korrekt: {0} inkorrekt: {0} total: {len(luecken)}'
   document.select('span.luecke')[0].focus()

def move_focus(ev):
   global CURRENT_FOCUS
   lues = document.select('span.luecke')
   if DEBUG:
      document <= html.P()
      document <= f"trying to move focus to {CURRENT_FOCUS}"
   if (len(lues)):
      CURRENT_FOCUS = (CURRENT_FOCUS + 1) % len(lues)
      lues[CURRENT_FOCUS].focus()
'''
XX['ATTRIBUTE_NODE ', 'CDATA_SECTION_NODE ', 'COMMENT_NODE ', 'DOCUMENT_FRAGMENT_NODE ', 'DOCUMENT_NODE ', 'DOCUMENT_POSITION_CONTAINED_BY ', 'DOCUMENT_POSITION_CONTAINS ', 'DOCUMENT_POSITION_DISCONNECTED ', 'DOCUMENT_POSITION_FOLLOWING ', 'DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC ', 'DOCUMENT_POSITION_PRECEDING ', 'DOCUMENT_TYPE_NODE ', 'ELEMENT_NODE ', 'ENTITY_NODE ', 'ENTITY_REFERENCE_NODE ', 'NOTATION_NODE ', 'PROCESSING_INSTRUCTION_NODE ', 'TEXT_NODE ', 'accessKey ', 'accessKeyLabel ', 'addEventListener ', 'after ', 'animate ', 'append ', 'appendChild ', 'assignedSlot ', 'attachInternals ', 'attachShadow ', 'attributes ', 'baseURI ', 'before ', 'blur ', 'childElementCount ', 'childNodes ', 'children ', 'classList ', 'className ', 'click ', 'clientHeight ', 'clientLeft ', 'clientTop ', 'clientWidth ', 'cloneNode ', 'closest ', 'compareDocumentPosition ', 'contains ', 'contentEditable ', 'dataset ', 'dir ', 'dispatchEvent ', 'draggable ', 'enterKeyHint ', 'firstChild ', 'firstElementChild ', 'focus ', 'getAnimations ', 'getAttribute ', 'getAttributeNS ', 'getAttributeNames ', 'getAttributeNode ', 'getAttributeNodeNS ', 'getBoundingClientRect ', 'getClientRects ', 'getElementsByClassName ', 'getElementsByTagName ', 'getElementsByTagNameNS ', 'getRootNode ', 'hasAttribute ', 'hasAttributeNS ', 'hasAttributes ', 'hasChildNodes ', 'hasPointerCapture ', 'hidden ', 'id ', 'innerHTML ', 'innerText ', 'inputMode ', 'insertAdjacentElement ', 'insertAdjacentHTML ', 'insertAdjacentText ', 'insertBefore ', 'isConnected ', 'isContentEditable ', 'isDefaultNamespace ', 'isEqualNode ', 'isSameNode ', 'lang ', 'lastChild ', 'lastElementChild ', 'localName ', 'lookupNamespaceURI ', 'lookupPrefix ', 'matches ', 'mozMatchesSelector ', 'mozRequestFullScreen ', 'namespaceURI ', 'nextElementSibling ', 'nextSibling ', 'nodeName ', 'nodeType ', 'nodeValue ', 'nonce ', 'normalize ', 'offsetHeight ', 'offsetLeft ', 'offsetParent ', 'offsetTop ', 'offsetWidth ', 'onabort ', 'onanimationcancel ', 'onanimationend ', 'onanimationiteration ', 'onanimationstart ', 'onauxclick ', 'onbeforeinput ', 'onblur ', 'oncanplay ', 'oncanplaythrough ', 'onchange ', 'onclick ', 'onclose ', 'oncontextmenu ', 'oncopy ', 'oncuechange ', 'oncut ', 'ondblclick ', 'ondrag ', 'ondragend ', 'ondragenter ', 'ondragexit ', 'ondragleave ', 'ondragover ', 'ondragstart ', 'ondrop ', 'ondurationchange ', 'onemptied ', 'onended ', 'onerror ', 'onfocus ', 'onformdata ', 'onfullscreenchange ', 'onfullscreenerror ', 'ongotpointercapture ', 'oninput ', 'oninvalid ', 'onkeydown ', 'onkeypress ', 'onkeyup ', 'onload ', 'onloadeddata ', 'onloadedmetadata ', 'onloadend ', 'onloadstart ', 'onlostpointercapture ', 'onmousedown ', 'onmouseenter ', 'onmouseleave ', 'onmousemove ', 'onmouseout ', 'onmouseover ', 'onmouseup ', 'onmozfullscreenchange ', 'onmozfullscreenerror ', 'onpaste ', 'onpause ', 'onplay ', 'onplaying ', 'onpointercancel ', 'onpointerdown ', 'onpointerenter ', 'onpointerleave ', 'onpointermove ', 'onpointerout ', 'onpointerover ', 'onpointerup ', 'onprogress ', 'onratechange ', 'onreset ', 'onresize ', 'onscroll ', 'onsecuritypolicyviolation ', 'onseeked ', 'onseeking ', 'onselect ', 'onselectionchange ', 'onselectstart ', 'onslotchange ', 'onstalled ', 'onsubmit ', 'onsuspend ', 'ontimeupdate ', 'ontoggle ', 'ontransitioncancel ', 'ontransitionend ', 'ontransitionrun ', 'ontransitionstart ', 'onvolumechange ', 'onwaiting ', 'onwebkitanimationend ', 'onwebkitanimationiteration ', 'onwebkitanimationstart ', 'onwebkittransitionend ', 'onwheel ', 'outerHTML ', 'outerText ', 'ownerDocument ', 'parentElement ', 'parentNode ', 'part ', 'prefix ', 'prepend ', 'previousElementSibling ', 'previousSibling ', 'querySelector ', 'querySelectorAll ', 'releaseCapture ', 'releasePointerCapture ', 'remove ', 'removeAttribute ', 'removeAttributeNS ', 'removeAttributeNode ', 'removeChild ', 'removeEventListener ', 'replaceChild ', 'replaceChildren ', 'replaceWith ', 'requestFullscreen ', 'requestPointerLock ', 'scroll ', 'scrollBy ', 'scrollHeight ', 'scrollIntoView ', 'scrollLeft ', 'scrollLeftMax ', 'scrollTo ', 'scrollTop ', 'scrollTopMax ', 'scrollWidth ', 'setAttribute ', 'setAttributeNS ', 'setAttributeNode ', 'setAttributeNodeNS ', 'setCapture ', 'setPointerCapture ', 'shadowRoot ', 'slot ', 'spellcheck ', 'style ', 'tabIndex ', 'tagName ', 'textContent ', 'title ', 'toggleAttribute ', 'webkitMatchesSelector ']XX
'''
#document <= "Data: "+ str(get_data())

for s in document.select('span.luecke'): # spans with class 'luecke'
#    s.bind("click", clear_span) 
    s.bind("focus", clear_span) 
#    s.bind("input", clear_span) 
    s.bind("blur", unclear_span) 

document <= html.P()
check_btn = html.BUTTON("Check")
check_btn.bind("click", compare)

document <= html.P()
artikel_btn = html.BUTTON("Test-Artikel")
artikel_btn.bind("click", get_article)

document <= html.P()
input_btn = document.select("#ok_button")[0] # html.BUTTON("OK")
input_btn.bind("click", get_article_from_input)
input_btn.bind("keypress", get_article_from_input)

check_btn = document.select("#check_button")[0] 
check_btn.bind("click", compare)

""" document <= html.P()
move_btn = html.BUTTON("Next")
move_btn.bind("click", move_focus)
document <= move_btn"""

document.select("#check_result")[0].bind("click", move_focus) 

#document <= check_btn
document <= artikel_btn
#document <= input_btn

