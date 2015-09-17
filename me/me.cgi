#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Execute as cgi-skript and send a correct HTTP header.

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
#print("Content-type: image/gif")
print("")


# Store my ascii image in a separat variabel as a raw string
meImage = r"""
    - - - - - = = == ---------------
    xxooxx   oooo
    goooggghhhjjjkkk
    ee       ffff
    ggg        eee
        rrrrrrrrrrrrrr
    gggggggaaaaa
    ------------------
"""


# Here comes the content of the webpage

content = """
Min Me-sida
==============================================================================


{image}

Hej,

Jag heter Björn Viklund läser denna kurs
på halvtid tillsammans med en annan
kurs så det blev . . heltid . . plötsligen händer det!!.

Jag är född och har
tillbringat mina första ~20år i mellersta Sverige,
Norrlands inland mellan Östersund och  Storuman.
Tyvärr så gick det utför för mig efter tonåren . . hamnade i Stockholms
utkanter, KTH vid Östra Station i 20år.
Sedan jobbade jag mig lite norrut igen till Kista och Ericsson . .
MEN sedan barkade iväg så då hamnade jag i Lund
fanns ju bron iofs men klarade mig ifrån Danmark iaf.

Sedan kastades jag ut (åldersberoende) så nu är jag på
väg tillbaka igen, sitter just nu i Stockholm och gör detta...

Startade 2013(?) på BTH men det gick inget bra då det blev renovering
av huset här i Stockholm.
Så då började vi renovera huset i Norrland för att övervintra där
(renoveringen närmare ett år) trillade igenom då vi rev golv, bröt armen,
fick plötsligen en annan lägenhet och under en hel del pyssel
har jag flytta dit/hit då.

renoveringen i Norrland är lågintensiv nu och har startat igen på BTH.


http://www.student.bth.se/~bjvi13/dbwebb-kurser/python/me/me.cgi


Om jag skall nämna någon hobby, förutom webbprogrammering, så blir det renovering
 av sommartorbet till vinterstandard, igen.
 Lite trädgårdsskötsel också.....

Ska börja träna också, igen, då saker och ting lugnat sig lite.

Vi syns och hörs i forum och chatt!

kmom03 and still kicking! 

"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content.format(image=meImage))
