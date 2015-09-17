#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Me-page redovisning, texts from each course moment.
As cgi.

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


# Here comes the content of the webpage
content = """
Min Redovisnings-sida
==============================================================================


Kmom01:
------------------------------------------------------------------------------


Hoppsan!

Riktigt himla rolig start av detta. LINUX på PC och relativt bra fungerande verktyg
både på Firefox(FireSSH)
 och Chroome(Secure Shell)
 Putty osså..

 Bra också att LINUX kommer in som en upside.
 cygwin riktigt plus......
 OCH dbwebb riktigt bra för att få rätt struktur
 sedan har jag plockat med FileZilla, bekvämt då den är bekant.

 Permissins är mycket enklare i LINUX än i
 Windows10(
 https://www.youtube.com/watch?v=FFZsXI9sq34
 http://www.7tutorials.com/take-ownership-and-change-permissions-files-and-folders
 )

 Har inte fått html att fungera i cgi ännu exempel tack...
 Dessutom översikter med minskad entropi skulle göra det snabbare att förstå
 hur det hänger ihop.
 Hur skapar man bara en "fil" som lägger in redivisningstext i både .py och .cgi??

 Frågorna:


Vilken utvecklingsmiljö använder du?
Windows10 på Dell LATIDUDE E5530 16GB RAM, 200GB SSD + 3TB onside (googledrive osså men inte för detta)
Är du bekant med Python sedan tidigare?
NOPE konstigt nog . . .
Är du bekant med programmering och problemlösning sedan tidigare?
JA! Men inte speciellt duktig programmerat i slutet på 70-talet
. . något har hänt . . och det händer hela tiden....
Är du bekant med terminalen och Unix-kommandon sedan tidigare? Svaret blir nej . . men har "provat på"
Gick det bra att komma i gång med kursmomentet, var det lagom, för litet, för stort? Lagom lätt
men som jag skrev entropin och översikten kunde vara tydligare.
Vilken del av kursmaterialet (böcker, artiklar, videor, etc) uppskattade du mest?
Bäst är mos video (andra videos är inte fel heller, tvärtom) tipset:
sakta in när det blir nytt och krytt osv.. . . gärna fler om du orkar.
Böcker är böcker roligt att ha några (når kakburken bättre) men
man läser inte så mycket chatten och surfen ger snabba besked...
Dessutom finns ju så gott som alla böcker fritt som pdf nu (fylla disken typ)
Artiklar blir alla små och lite större siter som har tips ömsom vin ömsom vatten.

MEN mos-video´s bäst för lärandet . . .


vid publish:
DONE to validate and publish course results.
Saved a log of the output: less -R '/home/erikwi2000/.dbwebb-publish.log'
Your files are now published on:
 http://www.student.bth.se/~erikwi2000/dbwebb-kurser/python/me
MEN är och borde vara:
 http://www.student.bth.se/~bjvi13/dbwebb-kurser/python/me

 felet?????

Kmom02:
------------------------------------------------------------------------------

Här skriver du redovisningstext för kursmoment 02.

TBD


"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
