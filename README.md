# lückentext

Macht aus einem deutschen Text einen Lückentext, indem es bestimmtem alle Artikel entfernt. Zur Kontrolle kann man einen beliebigen Artikel in die Lücken einfügen.

Built in python3 on Flask.

Verwendet [deta.sh|deta.sh] als deployment platform, inklusive Deta Base. Dafür braucht man einen Project Key, den man mit einem gratis Account bekommt.

Man kann die Flask app auch problemlos lokal laufen lassen, allerdings benötigt der Zugriff auf deta base einen Internetzugang und den oben erwähnten Project Key.

## commands

```
pip install -r requirements.txt
```

Set deta project key as environment variable:
```
export deta_project_key=<the deta project key>
```

Start:
```
python main.py
```
oder, wenn python3 noch nicht die standard Pythonvesion is:

```
python3 server.py
```

