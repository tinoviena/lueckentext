import get_text
import replace
import logging

#logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("app.py")
log.setLevel(level=logging.DEBUG)

ps = get_text.from_80_Tage_wiki()

log.debug(f'Found {len(ps)} paragraphs')

for i, p in enumerate(ps):
    t=p.text[:80].replace("\n","")
    log.debug(f'{i} ::: {t}')
    (lt, ls) = replace.replace(p.text)
    log.debug(lt)

    first = ls[3]
    log.debug(first)
    log.debug(first[1])
    log.debug(f'{lt[:first[1]]} :{first[0]}:{lt[first[1]+10:100]}')
    if i>1: break
    
