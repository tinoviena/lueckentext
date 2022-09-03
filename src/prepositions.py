#"Genetiv:"
genetiv = ["angesichts","anhand","anlässlich","anstatt","anstelle","aufgrund","außerhalb","beiderseits","bezüglich","diesseits","infolge","innerhalb","jenseits","längs","links","mithilfe","oberhalb","rechts","unterhalb","statt","südlich","trotz","ungeachtet","unweit","während","wegen","westlich"]
dativ   = ['aus', 'außer', 'bei', 'binnen', 'entgegen', 'entgegen', 'entsprechend', 'gegenüber', 'gemäß', 'mit', 'nach', 'nahe', 'samt', 'seit', 'zu', 'zufolge', 'zuliebe']
akkusativ = ['für', 'um', 'durch', 'entlang', 'gegen', 'ohne', 'wider']
dativ_akkusativ = ['an', 'auf', 'hinter', 'in', 'neben', 'über', 'unter', 'vor', 'zwischen']

alle = '''
A

à
ab
abseits
abzüglich
an
anfangs
angelegentlich (s. anlässlich)
angesichts
anhand
anlässlich
anstatt
anstelle (siehe: anstatt)
auf
aufgrund/auf Grund
aufseiten/auf Seiten
aus
ausgangs
außer
außerhalb
ausschließlich
ausweislich

B

bar
bei
beid(er)seits
betreffs
bezüglich
binnen
bis

D

dank
diesseits
durch

E

eingangs
eingedenk
einschließlich
entsprechend
entgegen
entlang
exklusive

F

fern
für

G

gegen
gegenüber
gemäß

H

hinsichtlich
hinter

I

in
in puncto
infolge
inklusive
inmitten
innerhalb

J

je
jenseits

K

kraft

L

längs(seits)
laut

M

mangels
mit
mithilfe/mit Hilfe
(mit)samt
mittels

N

nach
nahe
neben
nebst
nördlich
nordöstlich (s. nördlich)
nordwestlich (s. nördlich)

O

oberhalb
ohne
östlich

P

per
pro

R

rücksichtlich

S

(mit)samt
seit
seitens
seitlich
statt (siehe: anstatt)
südlich
südöstlich (s. südlich)
südwestlich (s. südlich)

T

trotz

U

über
um
um … willen
ungeachtet
unter
unterhalb
unweit

V

vis-à-vis
von
vonseiten/von Seiten (siehe: seitens)
vor
vorbehaltlich

W

während
wegen
westlich
wider

Z

zeit
zu
zufolge
zugunsten/zu Gunsten
zulasten /zu Lasten
zuliebe
zuungunsten (siehe: zugunsten/zu Gunsten)
zuzüglich
zwecks
zwischen
'''.replace(' ','').split('\n')

alle=list(filter(lambda x : len(x)>1, alle))
print(alle)
