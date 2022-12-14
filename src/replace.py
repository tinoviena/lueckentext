import src.articles as articles

replacement_text = "___"

def replace(text :str, para_i :int) -> str:
    pieces = text.split()
    new_text = ""
    replacements = []
    for i, p in enumerate(pieces):
        if p.lower() in articles.all():
            replacements.append((p,len(new_text) - len(replacement_text)-1))
#            new_text += f' [:{str(len(replacements)).rjust(2, "0")}:]' #" " + replacement_text
            
            new_text += f' <span contenteditable="true" id="{para_i}:{str(len(replacements)).rjust(2, "0")}" class="luecke">{replacement_text}</span>'
        else:
            new_text += " " + p

    return (new_text.strip(), replacements)

