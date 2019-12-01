# Kulunvalvonta-Tehtävä

Tehtävä on koulutyö Tampereen yliopistossa, jonka sai tehdä yksin tai kaverin kanssa. Tehtävä oli alunperin kaverini, johon tein malli vastauksen, jota hän käytti apunansa sen ratkaisemiseen.

# Tehtävänanto:

Eräässä kuvitteellisessa organisaatiossa toimivilla henkilöillä on kulkukortit, joille voidaan antaa kulkuoikeuksia organisaation tiloihin. Jokainen kulunvalvontajärjestelmään kuuluva ovi on yksilöity ovikoodilla, joka on mielivaltainen merkkijono. Ovikoodien lisäksi kulunvalvontajärjestelmässä on kulkualuekoodeja, jotka ovat myös mielivaltaisia merkkijonoja. Ovikoodit ja kulkualuekoodit ovat yksilöiviä, eli sama merkkijono ei voi toimia kahden eri asian koodina (oven ja kulkualueen).

Tiedot kaikista organisaation kulunvalvontajärjestelmään kuuluvista ovista ja kulkualueista on talletettu dict-tyyppiseen muuttujaan nimeltä DOORCODES, joka löytyy määriteltynä ohjelmakoodipohjan alusta. Kyseisessä muuttujassa on avaimina kaikien organisaation ovien ovikoodit. Avainta vastaavana arvona on lista kulkualuekoodeista, joilla on oikeus kulkea ko. ovesta. Laillinen ovikoodi on siis merkkijono, joka löytyy avaimena ko. dictistä ja laillinen kulkualuekoodi merkkijono, joka löytyy alkiona jostakin ko. dictiin arvoiksi talletetuista listoista.

Henkilöjen kulkukorteille lisätään pääsykoodeja, jotka voivat olla joko ovikoodeja tai kulkualuekoodeja.

Esimerkki 1: Henkilöllä, jonka työhuone on TE113, voisi olla kulkukortilleen ladattuna vaikkapa pääsykoodit TIE, TE113 ja G, joista viimeinen voisi tarkoittaa vaikkapa organisaation yleisten tilojen kulkualuetta (general). Kortille ladatuista pääsykoodeista TIE ja G ovat kulkualuekoodeja ja TE113 ovikoodi. Tämän voi päätellä siitä, että TE113 on yksi muuttujan DOORCODES sisältämistä avaimista, mutta TIE ja G eivät esiinny avaimina.

Esimerkki 2: DOORCODES-dictissä avainta "TC210" vastaavana arvona on lista ["TIE","TST"] Tämä tarkoittaa, että ovesta TC210 pääsee kulkemaan, jos kulkukortille on ladattuna jokin seuraavista pääsykoodeista: TC210 (joka siis on ko. oven ovikoodi), TIE tai TST (jotka molemmat ovat kulkualuekoodeja).

Toteutetaan valmiina annettua ohjelmakoodia hyödyntäen ohjelma, joka lukee käynnistyttyään työhakemistosta tiedoston nimeltä accessinfo.txt. Kyseinen tiedosto sisältää listan organisaation kulkukorteista ja niille talletetuista tiedoista. Jos ja kun tiedostot on luettu onnistuneesti, ohjelma esittää käyttäjälle yksinkertaisen komentotulkkikäyttöliittymän, jonka avulla kulkukorttitietoja voidaan käsitellä.

# Tehtävän toteutukselle asetetut erityisvaatimukset

Valmiissa tiedostopohjassa on toteutettu luokka Accesscard sekä komentotulkkikäyttöliittymä. Luokka Accesscard mallintaa yksittäistä kulkukorttia. Organisaation kulkukorttien tiedot tulee tallettaa kyseistä luokkaa hyödyntäen niin, että Accesscard-olioita tallennetaan sopivaan Python-tietorakenteeseen. Valmiissa tiedostopohjassa luokalle on myös määritelty metodeita, jotka ovat toteuttamatta. Määritellyt metodit tulee toteuttaa ja niitä tulee käyttää tehtävänannon komentojen toteuttamisessa. Valmiina määriteltyjen metodien parametrejä ei saa muuttaa. Eli niitä ei saa lisätä tai poistaa eikä uudelleen nimetä, koska palautusautomaatti olettaa niiden olevan samat kuin tiedostopohjassa.

Se, että valmiina annetussa ohjelmakoodipohjassa on määriteltynä valmiiksi joitain metodeita ja funktiota, ei tarkoita, että ohjelman funktiojako olisi täydellinen juuri tällaisena. Tarpeen vaatiessa ja halutessasi panostaa ohjelmointityyliin voit myös itse määritellä lisää funktioita ja metodeja. Myös muita luokkia saa halutessaan määritellä.

Myöskään valmiina annetun komentotulkin toimintaa ei saa muuttaa, koska palautusautomaatti olettaa ohjelman toimivan tiedostopohjan mukaisesti.

Koodipohjassa olevia valmiita kommentteja saa ja pitääkin muokata. Osa kommenteista on keskeneräisiä ja osa liittyy tehtävänantoon eikä itse ohjelman toimintaan. Valmiissa työssä olevien kommenttien on siis oltava oleellisia ohjelman kannalta.

# Syötetiedosto

Ohjelman lukema syötetiedosto on aina nimeltään accessinfo.txt. Tätä ei siis kysytä käyttäjältä.

Syötetiedosto on nk. CSV-tiedosto: sen rivit muodostuvat osatiedoista, jotka on eroteltu toisistaan jollain sovitulla merkillä. Tässä tehtävässä erotinmerkkeinä toimivat puolipiste ja pilkku.

Syötetiedoston rivit ovat muodoltaa seuraavia:

tunniste;nimi;lista pääsykoodeja
jossa lista pääsykoodeja sisältää pilkuin toisistaan eroteltuja merkkijonoja, jotka ovat pääsykoodeja. Kaikki muunlaiset rivit ovat virheellisiä.
Esimerkiksi seuraava tiedosto olisi kelvollinen syötetiedosto toteutettavalle ohjelmalle:

987654;Ella Electronicsresearcher;ELT,G,SM112
123456;Ted Technologystudent;G
999;Cliff Cleaner;G
KK-23;Fiona Fired Employee;
777;Thelma Teacher;TIE,OPET,TE113
888;Pricilla Professor;TIE,TC114,TC210,TE102
007;Research Team X;SM112,TE117,X
Esimerkki 1: yksinkertainen virheetön syötetiedosto.

Tunniste ja nimi ovat mielivaltaisia merkkijonoja (eivät kuitenkaan sisällä merkkejä ";" ja ","). Tunniste yksilöi kulkukortin, eli organisaatiossa ei voi olla useita kulkukortteja samalla tunnisteella. tunniste, nimi tai yksikään kulkualuekoodi ei saa olla tyhjä merkkijonoja.
Lista kulkualuekoodeja voi olla tyhjä. Tämä tarkoittaa sitä, että kyseisellä kulkukortilla ei pääse minnekään. Ehkä kortti on kadonnut tai varastettu ja sen oikeudet on poistettu.

Tiedostoa ei voi olettaa "sievennetyksi" pääsykoodien suhteen, eli tiedostossa kulkukortilla voi olla päällekkäisiä pääsykoodeja, esimerkiksi kulkualuekoodi TIE ja ovikoodi TC114 (näistähän TC114 on turha, koska TIE kattaa myös sen).

# Accesscard-luokka

Kuten edellä määriteltiin, luokka Accesscard mallintaa yksittäistä kulkukorttia ja siis sisältää sen tiedot, jotka on luettu syötetiedostosta. Luokkarajapinnassa on valmiiksi määriteltynä metodeja, esimerkiksi pääsykoodin lisääminen kulkukortille ja tietystä ovesta pääsyn tarkastaminen. Esimerkki yksittäisen kulkukorttiolion toiminnasta Python-konsolissa:

>>> DOORCODES = {"TC114":["TIE"], "TE113":[]}
>>> card = Accesscard("777","Thelma Teacher")
>>> card.info()
777, Thelma Teacher, access:
>>> card.check_access("TC114")
False
>>> card.check_access("TE113")
False
>>> card.add_access("TIE")
>>> card.check_access("TC114")
True
>>> card.add_access("TE113")
>>> card.check_access("TE113")
True
>>> card.info()
777, Thelma Teacher, access: TE113, TIE
>>>
Esimerkki 2: kulkukorttiolion toiminta, huomaa, että määriteltynä pitää olla DOORCODES-niminen dict.

Huomaa erityisesti rivien kolme ja neljä toiminta: info-metodin kutsu tulostaa, ei palauta merkkijonoa. Python-konsolissa rivi neljä lukisi '777, Thelma Teacher, access:' sisältäen hipsut, jos metodi olisi palauttanut merkkijonon. Kun hipsuja ei ole, on metodi tulostanut jotakin.

# Käyttöliittymä

Käynnistyttyään ohjelma yrittää lukea syötetiedoston sisällön sopivaan Python-rakenteeseen. Jos lukemisessa ei tapahtunut virheitä, ohjelma tulostaa kehotteen ja suorittaa käyttäjän antamia komentoja:

command>  
Toisaalta, mikäli tiedoston lukeminen epäonnistui mistä tahansa syystä, ohjelma tulostaa virheilmoituksen ja suoritus päättyy:

Error: file cannot be read.
Käyttäjän komentoja lukeva käyttöliittymä on toteutettu valmiina annetussa tiedostopohjassa, eikä sen toimintaa siksi määritellä tässä. Jos käyttäjä syöttää määrittelemättömän komennon tai määritellylle komennolle väärän määrän parametreja, tulostuu valmiina komentotulkissa toteutettu virheilmoitus.

# Komennot

Seuraavassa listataan käyttöliittymän tunnistamat komennot ja määritellään niiden toiminnallisuus. Esimerkkitulosteissa oletetaan, että ohjelmalla on käytössään edellä esitetty syötetiedosto.

komento: info
Tulostaa näytölle tiedot kulkukortista, jolla on kysytty tunniste. Tulostusasun voi päätellä seuraavasta esimerkistä:
command> info 777
777, Thelma Teacher, access: OPET, TE113, TIE
command> info 888
888, Pricilla Professor, access: TIE
command> info abc
Error: unknown id.
command> info 123
Error: unknown id.
command>  
Esimerkki 3: info-komennon käyttäytymismalleja.

Kaikki kortin sisältämät pääsykoodit tulostetaan aakkosjärjestyksessä samaan listaan riippumatta siitä, ovatko ne ovikoodeja vai kulkualuekoodeja.

"Turhia" ovikoodeja ei tulosteta. Tämä tarkoittaa, että jos ovikoodi TC114 kuuluu kulkualueeseen TIE, ja kulkukortilla on oikeudet molempiin näistä, niin ovikoodia TC114 ei tulosteta. (Ks. myös komento add.)

Ainoa info-komentoon liittyvä virheilmoitus, joka ohjelmoijan on huomioitava, on se, että haettavaa tunnistetta ei ole ole olemassa. Virheilmoituksen tulostusasu pääteltävissä edeltä.
komento: list
Tulostaa näytölle kaikkien organisaation kulkukorttien tiedot tunnisteen mukaisessa aakkosjärjestyksessä. Kortin tietojen tulostusasu on sama kuin info-komennossa. Esimerkki komennon toiminnasta:
command> list
007, Research Team X, access: SM112, TE117, X
123456, Ted Technologystudent, access: G
777, Thelma Teacher, access: OPET, TE113, TIE
888, Pricilla Professor, access: TIE
987654, Ella Electronicsresearcher, access: ELT, G, SM112
999, Cliff Cleaner, access: G
KK-23, Fiona Fired Employee, access:
command>  
Esimerkki 4: list-komennon tulostus esimerkin 1 mukaisella syötetiedostolla.

Komentoon list ei liity mitään virhetilanteita, joista ohjelmoijan olisi tarpeen huolehtia. Ainoa mahdollinen virhetilanne on käsitelty valmiina annetussa käyttöliittymäkoodissa.
komento: access
Komento tulostaa seuraavassa muodossa tiedon siitä, onko tietyllä kulkukortilla oikeutta kulkea tietystä ovesta:
command> access 123456 TB103
Card 123456 ( Ted Technologystudent ) has no access to door TB103
command> access 987654 SM112
Card 987654 ( Ella Electronicsresearcher ) has access to door SM112
command> access 42 TB103
Error: unknown id.
command> access 123456 TB100
Error: unknown doorcode.
command> access 42 TB100
Error: unknown id.
command>  
Esimerkki 5: access-komennon käyttäytyminen.

Huomioitavat virhetilanteet, jotka käsitellään tässä järjestyksessä:

käyttäjä syöttää tunnisteen, jota vastaavaa kulkukorttia ei ole olemassa
käyttäjä syöttää ovikoodin, jota ei ole olemassa
Virheilmoitukset ovat pääteltävissä esimerkkiajosta.
komento: add
Komennon add avulla kulkukortille voidaan lisätä uusi pääsykoodi seuraavaan tapaan:
command> info 123456
123456, Ted Technologystudent, access: G
command> add 123456 TIE
command> info 123456
123456, Ted Technologystudent, access: G, TIE
command> add 123456 TB103
command> info 123456
123456, Ted Technologystudent, access: G, TB103, TIE
command> add 123456 TC114
command> info 123456
123456, Ted Technologystudent, access: G, TB103, TIE
command> add xyz TC114
Error: unknown id.
command> add 123456 xyz
Error: unknown accesscode.
command> add xyz xyz
Error: unknown id.
command>  
Esimerkki 6: add-komennon käyttäytymisesimerkkejä.

Pääsykoodia ei kuitenkaan lisätä kulkukortille, jos kortilla on jo lisättynä täsmälleen sama pääsykoodi. Mikäli lisättävä pääsykoodi on kulkualuekoodi ja kortilla on jo tallennettuna ovikoodeja, jotka tulevat "turhiksi" tämän kulkualuekoodin lisäämisen myötä, poistetaan nämä "turhat" ovikoodit kortin tiedoista. Konkreettisesti nämä tilanteet näkyvät seuraavassa esimerkissä:

command> info 777
777, Thelma Teacher, access: OPET, TE113, TIE
command> add 777 TC114
command> info 777
777, Thelma Teacher, access: OPET, TE113, TIE
command> add 777 TIE
command> info 777
777, Thelma Teacher, access: OPET, TE113, TIE
command>  
Esimerkki 7: Kulkualuetta ei lisätä, jos kortilla entuudestaan kulkuoikeudet.

Ohjelmointivinkki: Kannattaa miettiä, onko helpompi valikoida poistettavat "turhat" ovikoodit ja poistaa ne, vai poistaa kaikki ovikoodit ja lisätä sitten takaisin ne ovikoodit, joille kortilla ei poiston jälkeen enää olisi pääsyä.

Virheetön add-komento ei tulosta mitään riippumatta siitä, lisättiinkö pääsykoodi vai ei, vaan ohjelma ainoastaan palaa odottamaan uutta komentoa. Huomioitavat virhetilanteet, jotka käsitellään tässä järjestyksessä:

käyttäjä syöttää tunnisteen, jota vastaavaa kulkukorttia ei ole olemassa
käyttäjä syöttää pääsykoodin, jota ei ole olemassa
Virheilmoitukset ovat pääteltävissä esimerkkiajosta.
komento: merge
Komennon merge avulla kulkukortille voidaan lisätä kaikki kulkualueet, jotka toisella kulkukortilla on määriteltynä. Komentoa käytetään seuraavasti:
command> info 987654
987654, Ella Electronicsresearcher, access: ELT, G, SM112
command> info 007
007, Research Team X, access: SM112, TE117, X
command> merge 987654 007
command> info 987654
987654, Ella Electronicsresearcher, access: ELT, G, SM112, TE117, X
command> info 007
007, Research Team X, access: SM112, TE117, X
Esimerkki 8: merge-komennon käyttäytyminen.

Eli edellisessä esimerkissä kortille, jonka tunniste on 987654 lisätään kaikki pääsykoodit, jotka tunnisteella 007 varustetulla kortilla on. Uudet kulkualueet lisätään samalla tavalla kuin add-komennollakin.
Virheetön komento ei tulosta mitään riippumatta siitä, lisättiinkö pääsykoodeja vai ei, vaan ohjelma ainoastaan palaa odottamaan uutta komentoa. Ainoa huomioitava virhetilanne on se, että käyttäjä syöttää tunnisteen, jota ei ole olemassa. Huomaa kuitenkin, että komennolle annetaan kaksi tunnistetta, jotka molemmat tulee tarkastaa. Virheilmoitus on jälleen sama kuin edellisissä komennoissa.

# Esimerkki ohjelman toiminnasta

Esimerkki ohjelman toiminnasta
Ohjelman toiminnallisuuden selkeyttämiseksi alla on esitetty vielä kokonainen suoritusesimerkki:

command> list
007, Research Team X, access: SM112, TE117, X
123456, Ted Technologystudent, access: G
777, Thelma Teacher, access: OPET, TE113, TIE
888, Pricilla Professor, access: TIE
987654, Ella Electronicsresearcher, access: ELT, G, SM112
999, Cliff Cleaner, access: G
KK-23, Fiona Fired Employee, access:
command> access 999 TC205
Card 999 ( Cliff Cleaner ) has no access to door TC205
command> add 999 TC205
command> access 999 TC205
Card 999 ( Cliff Cleaner ) has access to door TC205
command> add 999 TIE
command> access 999 TC203
Card 999 ( Cliff Cleaner ) has access to door TC203
command> access 999 TC114
Card 999 ( Cliff Cleaner ) has access to door TC114
command> access 999 TE102
Card 999 ( Cliff Cleaner ) has access to door TE102
command> info 999
999, Cliff Cleaner, access: G, TIE
command> access 999 TE111
Card 999 ( Cliff Cleaner ) has no access to door TE111
command> add 999 TE111
command> add 999 TE112
Error: unknown accesscode.
command> add 999 TE113
command> add 999 TE114
Error: unknown accesscode.
command> add 999 TE115
command> info 999
999, Cliff Cleaner, access: G, TE111, TE113, TE115, TIE
command> access 999 TE111
Card 999 ( Cliff Cleaner ) has access to door TE111
command> access 999 TE112
Error: unknown doorcode.
command> access 999 TE113
Card 999 ( Cliff Cleaner ) has access to door TE113
command> access 999 TE114
Error: unknown doorcode.
command> info 777
777, Thelma Teacher, access: OPET, TE113, TIE
command> merge 999 777
command> info 999
999, Cliff Cleaner, access: G, OPET, TE111, TE113, TE115, TIE
command> info 777
777, Thelma Teacher, access: OPET, TE113, TIE
command> merge 997 007
Error: unknown id.
command> merge 999 007
command> info 999
999, Cliff Cleaner, access: G, OPET, SM112, TE111, TE113, TE115, TE117, TIE, X
command> access 999 secret_corridor_from_building_T_to_building_F
Card 999 ( Cliff Cleaner ) has access to door secret_corridor_from_building_T_to_building_F
command> list
007, Research Team X, access: SM112, TE117, X
123456, Ted Technologystudent, access: G
777, Thelma Teacher, access: OPET, TE113, TIE
888, Pricilla Professor, access: TIE
987654, Ella Electronicsresearcher, access: ELT, G, SM112
999, Cliff Cleaner, access: G, OPET, SM112, TE111, TE113, TE115, TE117, TIE, X
KK-23, Fiona Fired Employee, access:
command> quit
Bye!
