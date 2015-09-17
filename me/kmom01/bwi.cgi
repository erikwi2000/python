#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Execute as cgi-skript and send a correct HTTP header.
Send result as plain text.
"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()


# Send the HTTP header
print("Content-Type: text/plain;charset=utf-8")
#print("Content-Type: text/html;charset=utf-8")
print("")


# Store my ascii image in a separat variabel as a raw string
meImage = r"""

          _______     
         /_______\    
         |   OO  |
         |  OOOO |
         |  ---- |
         |_______| 
         0=======0

"""


# Here comes the content of the webpage 
content = """
Min Me-sida
==============================================================================

Hej, 

Jag heter Björn Viklund. X

{image} 

Detta är min me-sida i kursen. Denna sidan innehåller en presentation av mig
själv. 
Börjande för många år sedan studera ja innan datorerna fanns tror jag . .
jag hade iaf ingen.
Landade via grundskola--gymnasium till KTH och fastnade där i 14år.
I den tiden fanns datorer, räknare (HP), och en del hjälpmedel.

Vi matade datorerna med tjockt papper som vi petade hål i.
Två \"körningar\" per dag fick vi . . .

1975 ungefär så hade en institution en dator med 
3MB disk och där 16 användare sansades..

Och vartefter så ökade prestanda och minne . . 
På min PC är det 3TB sidodisk och 240GB intern SSD samt 16GB RAM..

Dessutom har formatet garderob blivit en modell större kokbok.

Har också jobbat i södra delen av landet på Sony och varit med om 
definition av Xperia Z-serien . . 16GB eMMC och minneskort upp till 128GB 
lite variationer dock beroende på modell.....

Privat har det bara gått utför . . började norr om Östersund 
men sedan gick det bara utför och hamnade i Lund till slut

Har fyra barn som jag inte vet riktigt vad dom gör . . precis som förut . . 
vissa saker pratas det inte om . . MEN det tar sig . .
Ett barnbarn som inte heller pratar så mycket . .
ensambarn får så mycket ord lagda i sin mun så språket är:
-- AaaA
eller
-- EEEeeeE

MEN småsaker som \"ställ tillbaka gerjen du tog\" 
(man kommer ju inte igår var man lagt saker längre)
klarar han av så han förstår riktigt bra egentligen . . .

På nätet finns jag här och där . . 

Hobby.

Ja 2013 blev de webbprogrammering tyvärr så sk-t det sig pga 
rörighet i boendet
så då blev det renovering av hus 2014....
renovering inte klar ännu men boende fixat 
så nu gäller webb o programmering igen

Ja plus flera andra saker osså: Golf, Dans, Friluft...
..MEN man hinner inte allt..... 


Vi syns och hörs i forum och chatt!

"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content.format(image=meImage))
