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
print("Content-Type: text/html;charset=utf-8")
print("")


# Here comes the content of the webpage
content = """
<h1>Min Redovisnings-sida, <i>bjvi13 alt. erikwi2000</i></h1>


<h2><u>Kmom01:</u></h2>



<p>Hoppsan!<p>

<p>Riktigt himla rolig start av detta.</p>
<br>LINUX på PC och relativt bra fungerande verktyg
både på Firefox(FireSSH)
 och Chroome(Secure Shell)
 <br>Putty osså..

 <p>Bra också att LINUX kommer in som en upside.
 <br><i>cygwin riktigt plus</i>......
 <br><b>OCH</b> dbwebb riktigt bra för att få rätt struktur
 <br>sedan har jag plockat med FileZilla, bekvämt då den är bekant.

 <p>Permissions är mycket enklare i LINUX än i
 <br>
 <br>Windows10(
 <br>https://www.youtube.com/watch?v=FFZsXI9sq34
 <br>http://www.7tutorials.com/take-ownership-and-change-permissions-files-and-folders
 <br>)

<p> Har <s>inte</s> fått html att fungera i cgi <s>än</s>nu <s>exempel tack...</s>
 <p>Dessutom översikter med minskad entropi skulle göra det snabbare att förstå
 hur det hänger ihop.
 <br>Hur skapar man bara en "fil" som lägger in redivisningstext i både .py och .cgi??
 <br> finns inte??

 <h3>Frågorna:</h3>


<p><i>Vilken utvecklingsmiljö använder du?</i>
<br>Windows10 på Dell LATITUDE E5530 16GB RAM, 200GB SSD + 3TB onside (googledrive osså men inte för detta)
<p><i>Är du bekant med Python sedan tidigare?</i>
<br>NOPE konstigt nog . . .
<p><i>Är du bekant med programmering och problemlösning sedan tidigare?</i>
<br>JA! Men inte speciellt duktig programmerat i slutet på 70-talet
. . något har hänt . . och det händer hela tiden....
<p><i>Är du bekant med terminalen och Unix-kommandon sedan tidigare?</i>
<br>Svaret blir nej . . men har "provat på"
<p><i>Gick det bra att komma i gång med kursmomentet, var det lagom, för litet, för stort?</i>
<br>Lagom lätt
men som jag skrev entropin och översikten kunde vara tydligare.
<p><i>Vilken del av kursmaterialet (böcker, artiklar, videor, etc) uppskattade du mest?</i>
<br>Bäst är mos video (andra videos är inte fel heller, tvärtom) tipset:
<br>- sakta in när det blir nytt och krytt osv.. . .
<br>- gärna fler videos om du orkar.
<br>Böcker är böcker roligt att ha några (når kakburken bättre) men
man läser inte så mycket chatten och surfen ger snabba besked...
<br>Dessutom finns ju så gott som alla böcker fritt som pdf nu (fylla disken typ)
<br>Artiklar blir alla små och lite större siter som har tips ömsom vin ömsom vatten.

<p><b>MEN mos-video´s bäst för lärandet . . .</b>

<p>
<br>vid publish:
<br>DONE to validate and publish course results.
<br>Saved a log of the output: less -R '/home/erikwi2000/.dbwebb-publish.log'
<br>Your files are now published on:
<br>http://www.student.bth.se/~erikwi2000/dbwebb-kurser/python/me
<br>MEN är och borde vara:
 <br> http://www.student.bth.se/~bjvi13/dbwebb-kurser/python/me

 <br>felet?????

<h2><u>Kmom02:</u></h2>
------------------------------------------------------------------------------
<p>Fortfarande imponerad av den ordning som skapats via dbwebb och att det
 fungerar med uppdatering . . riktigt bra faktiskt . . .

 <p>Ska nog rita en bild/karta över de tre platserna samt kommandon däremellan

 <p>Hoppas att denna metodik/pedagogik finns på de andra kurserna . .

 <p>Nu känns det bättre också eftersom jag startade "i förväg" med att läs python etc...
 <br>Kanske ett litet tips där att tipsa studenterna om lite sommarläsning . .
 <br>eftersom böcker, videos etc finns tillgängligt är det ju bara att surfa kunt och4
 plocka.......

 <h3>till frågorna:</h3>
<p><i>Hur känns syntaxen i Python? Är det enkelt att se programmets struktur och vad det gör?</i>
<br>Syntaxen är som i de flesta moderna program . . det händer ganska mycket
även med bara ett fåtal kodrader . och den är effektiv och logisk . .<br>de självklara behöver man
inte skriva det tar intrepretatorn hand om...
<p><i>Hur går det med valideringen av uppgifterna? Är du överens med pylint om eventuella
 felmeddelanden vid valideringen?</i>
 <br>Briljant verktyg att snurra runt i koden med. <br>Överens?? <br>Pylint har ju rätt men ibland gör ja
 samma fel ideligen till exempel : där de ska vara, något mellanslag för mycket etc.
 men det känns som barnsjukdomarna kommer att gå över . .
<p><i>Hur gick det att utföra uppgifterna, var de enkla eller svåra?</i>
<br>Bra uppgifter lagom nivå . . <br>inte att det inte skulle kunna vara svårare men då
tappar vi gnuggandet på dessa småsaker som är så viktiga...
<br>Men pylint hittar onödiga variabler t.ex...<br> känns lite bekant med php, och C++ osv
förmodligen en bra starta up kurs för de andra med php och databaser lite svårare.....



<h2><u>Kmom03:</u></h2>
------------------------------------------------------------------------------


<br>
<br>Fortfarande imponerad av dbwebb och den smidiga strukturen inte alltför svårt
att använda.

<br>länkar:
<br> http://www.student.bth.se/~bjvi13/dbwebb-kurser/python/me/kmom03
<br> http://www.student.bth.se/~bjvi13/dbwebb-kurser/python/me/redovisning.cgi
<br><b>Saknar strukturen typ:</b>
<ol>
<li>Huvudsak I</li>
<li>Huvudsak II</li>
<ul>
<li>Bisak 1</li>
<ol>
<li>Riktig nitti gritty små, små sak</i>
</ol>
<li>Bisak 2</li>
<li>Bisak 3</li>
</ul>
<li>Huvudsak III</li>
</ol>

<p>Konstigt nog så missade jag uppgiften i kmom01 förmodligen så blandade jag med övningarna.<p>
<ul>

<h3>till frågorna:</h3>
<li><i>Har du programmerat med filhantering tidigare,
känns det lätt eller svårt?</i></li>
<li><b>Jo visst har filhantering gjorts förr men
detta är ganska raktfram och visst är behörigheter mycket enklare i LINUX</b></li>
<li><i>Vad tycker du om video som läromedel, tycker du att de tillför något som läromedel?</i></li>
<li><b>Riktigt bra . . jag märker att genomgångarna inte täcker hela kapitlen MEN
om det är presentation av "The vital few" (vilket det är) så är det OK
dock har vissa föreläsare bråttom typ: hastigt och lustigt . . .</li></b>
<li><i>Du har gjort din första modul i Python, känns strukturen bra?</i></li>
<li><b>Joo det känns som ett bra steg för oss som kommer från gamla tider:
<br>Fortran, maskinkod osv Det var en härlig tid då vi plockade
 maskinkod från kompilerad Fortran och effektiviserade (realtidsapplikationer)</b></li></>
<li><i>Vad tyckte du om de olika uppgifterna?
 Hur tänkte du när du utförde dem? Var de utmanande eller lätta?</i></li>
<li><b>Svar1: Joo det gick varmt stundtals.
<br>Svar2: Blandat <br>vissa gånger fattade jag inte up-front
<br>andra gånger var det riktigt lätt
<br> MEN att googla ger massor med bra info och
Dessutom nya verktyg och litteratur....</li></b>
</ul>


<h2><u>Kmom04:</u></h2>
------------------------------------------------------------------------------
<br>Länkar:
<br>
<br>http://www.student.bth.se/~bjvi13/dbwebb-kurser/python/me/kmom04
<br>http://www.student.bth.se/~bjvi13/dbwebb-kurser/python/me/redovisning.cgi

<p>Fortfarande imponerad av dbwebb och den
<br>smidiga strukturen inte alltför svårt
att använda.
<br> Saknar fortfarande strukturerna i kursinfo,
<br>missar av någon anledning
genom att springa iväg <br>och sedan inte riktigt gå tillbaka
i samma spår utan hoppar till ett annat spår.
<br>Tydligare snitsling kanske?
<br> Bra är dock detta nötande över kod/syntax
. . man lär sig så småningom att
<ul>
<li>det skall vara mellanslag på rätt ställe</li>
<li>det skall vara kolon där det ska vara</li>
<li>rätt indent!  blir bara oreda annars</li>
<li>det skall vara</li>
<li></li>
<li></li>
<li></li>
</ul>

<p> Detta avsnitt tog tid . .
vet inte om jag förstod upplägget
 men valde i alla fall en väg som
 <br>inte hamna tillbaka på huvudmenyn utan blev
 kvar hos Marvin med gjorde
 inte så mycket vid fel kommandon utan då till huvudmenyn...
<p> Och som oftast först lägga timmar på något för att
sedan hitta "bra o ha" som t. ex. läsa/skriva/strip/join underbart.
<br> Hadedock trubbel med att en
 CR dök upp ibland så jag strippade alla vagnreturer (tror jag)



 <h3>till frågorna:</h3>
<ul>
<li><i>Var det svårt att bekanta sig med datastrukturen för listor eller flöt det på bra?
</i></li>
<li><b>Jo visst är listor kända men de verktyg som finns i python är
smidigare än det jag haft sedan förunt</b></li>
<li><i>Har du jobbat med listor, eller arrayer, i andra
 programmeringsspråk — <br>kan du isåfall jämföra Python
 listor mot andra programmeringsspråk?
</i></li>
<li><b>Som ovan sagt bättre verktyg,
fler verktyg <br>och ändå så har jag bara skrapat på ytan.
<br>Jag upplever ofta att det finns verktyg som jag oftast <br>förut byggde
eller jobbade runt.</li></b>
<li><i>Hur gick det att utföra uppgifterna, <br>
vilken tog mest tid och vilken var mest lärorik när det gäller listor?
</i></li>
<li><b>Tog tid dels för att jag tog omvägar dela för att
jag inte tog vara på alla tipsen . .
<br>Om pedagogiken är för att skapa aha-upplevelser så
blev det små sådana i dessa verktyg för strukturerna..
<br>osså en lite större där jag upptäckte att funktionen Marvin
alldeles utmärkt kunde starta om....
<br>I gamla tider gjorde vi sådant genom hopp, och som nu funktioner.
<br> Som jag sa den filen rörande läsa/skriva/ändra/osv<br>
som finns i git är guld värd . . .</li></b>
</ul>

<h2><u>Kmom05:</u></h2>
------------------------------------------------------------------------------




TBD
<h2><u>Kmom06:</u></h2>
------------------------------------------------------------------------------


TBD
<h2><u>Kmom010:</u></h2>
------------------------------------------------------------------------------


TBD





"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
