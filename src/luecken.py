import spacy
from spacy.matcher import Matcher

nlp = spacy.load("de_core_news_sm")
matcher = Matcher(nlp.vocab)

def get_präpositionen_lueckentext(text, para_no=0):
    doc = nlp(text)
    PRÄPOSITION_VOR_ARTIKEL = [{"POS": "ADP"}, {"POS": "DET"}]
    matcher.add("ADP_DET", [PRÄPOSITION_VOR_ARTIKEL])
    matches = matcher(doc)

    lue_text = ""
    replacements = {}
    j = 0
    for c, (match_id, start, end) in enumerate(matches):
        span_id = calc_id(c, para_no)

        while(doc[j].i != start+1):
            token = doc[j]
            lue_text += token.text+" "
            j += 1

        token = doc[j]

        lue_text = lue_text + f' <span contenteditable="true" id="{span_id}" class="luecke">{token.lemma_}</span> '
        replacements[f"{span_id}"] = {
            "location": token.i, 
            "lemma":    token.lemma_, 
            "new_text": token.lemma_,
            "orig_text": token.text,
            "replaced": True
            }
        j += 1
    
    #after the last match there might be some text left to appedn
    while (j<len(doc)):
        lue_text += doc[j].text+" "
        j += 1
#    print(f"{len(locs)} Präpositionen gefunden")
#        lue_text = " ".join(new_doc)
#    lue_text = " ".join( [replace_smart(x, i, para_no) for (i,x) in enumerate(new_doc)] )
    lue_text = lue_text.replace(" . ", ". ")
    lue_text = lue_text.replace(" : ", ": ")
    lue_text = lue_text.replace(" , ", ", ")
    

    return(lue_text, replacements)

def get_verben_lueckentext(text, para_no=0):
    doc = nlp(text) # this is where the magic happens!
    new_doc = {}
    lue_text = ""
    replacements = {}
    
    for i, token in enumerate(doc):
        span_id = calc_id(i, para_no)

        if token.pos_ == 'VERB' or token.pos_=='AUX':
            #print(f"VERB/AUX: {token.text:<10} -> {token.lemma_:<10} [{token.i}]")
            #locs[token.i] = token
            
            container = {
                "location": token.i, 
                "lemma":    token.lemma_, 
                "new_text": token.lemma_,
                "orig_text": token.text,
                "replaced": True,
                #"token": token
                }
            lue_text = lue_text + f' <span contenteditable="true" id="{span_id}" class="luecke">{token.lemma_}</span> '
            
            replacements[f"{span_id}"] = container
        else:
            #print(f"NORMAL  : {token.text:<10} -> {token.lemma_:<10} [{token.i}]")
            new_doc[span_id] = {
                "location": token.i, 
                "lemma":    token.lemma_, 
                "new_text": token.text,
                #"orig_text": token.text,
                #"replaced": False
                }
            lue_text += token.text+" "

#    lue_text = " ".join(map( lambda x : x["new_text"], new_doc))
    
    lue_text = lue_text.replace(" . ", ". ")
    lue_text = lue_text.replace(" : ", ": ")
    lue_text = lue_text.replace(" , ", ", ")
    

    return(lue_text, replacements)

def calc_id(i, j) -> str:
    return f'{str(j).rjust(2,"0")}:{str(i).rjust(3, "0")}'

def replace_smart(ele, ele_id):
    ret = None
    if(ele["replaced"] == True):
        ret = f' <span contenteditable="true" id="{ele_id}" class="luecke">{ele["new_text"]}</span>'
    else:
        ret = ele["orig_text"]
    return ret

if __name__ == '__main__':
    
    print(get_verben_lueckentext("Ich lebe. Du sollst sprechen. Sie lebt. Wir leben. Ihr lebt. Sie leben.")[0])
    print(get_verben_lueckentext("Ich lebte. Du wirst leben. Er lebte. Wir lebten. Ihr lebtet. Sie lebten.")[0])
    (t, ds) = get_verben_lueckentext("Ich lebte. Du wirst leben. Er lebte. Wir lebten. Ihr lebtet. Sie lebten.")
