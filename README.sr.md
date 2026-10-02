# Project Docs Workflow

**Sačuvajte upotrebljive odluke, planove i dokaze kroz različite Codex sesije.**

[English](README.md) · [Instalacija](#instalacija-u-codexu) · [Prva upotreba](#prva-upotreba) · [Radna disciplina](#disciplina-koja-omogućava-da-pristup-funkcioniše) · [Provera](docs/validation.md)

Codex skill za uspostavljanje i održavanje malog, usklađenog dokumentacionog toka. Pravila projekta, prihvaćene odluke, planirani poslovi i dokazi sesija dobijaju jasno mesto, a novo znanje se prenosi u održavanu dokumentaciju uz očuvanje otvorenog posla.

Koristan je kada projekat traje kroz više sesija, saradnika ili agenata i postaje sve teže ustanoviti **šta postoji, šta je odlučeno i šta je sledeće**.

**Korist:** jasan početak rada, jedan operativni plan i sledljiva predaja između sesija. **Obaveza:** odluke moraju biti izričite, značajan rad zabeležen, a prikupljeni zapisi obrađeni. Sama instalacija skilla ne održava dokumentaciju aktuelnom.

## Šta se menja u praksi

| Problem koji se ponavlja | Kako ga ovaj tok obrađuje |
|---|---|
| Nova sesija počinje nagađanjem koji dokument je aktuelan | Kratak pregled vodi do merodavnog izvora za svaku ulogu |
| Zadaci su u planu, više pregleda i nedovršenim razgovorima | Jedan aktivni plan određuje redosled, zavisnosti i kriterijume završetka |
| Predlog vremenom postaje pretpostavljena odluka o proizvodu | Predlozi, prihvaćene odluke i stvarno ponašanje ostaju prepoznatljivi |
| Uspešan lokalni test postaje „spremno za produkciju” | Svaka tvrdnja nosi nivo dokaza koji stvarno postoji |
| Stari zapisi se stalno čitaju ili potpuno odbacuju | Provereno znanje se prenosi, otvoreni posao dobija odredište, a originalni dokaz se arhivira |

Na primer, sesija otkrije da CSV izvoz gubi vodeće nule. Prihvaćeni ugovor i dalje zahteva očuvanje identifikatora. Dokumentaciona faza beleži odstupanje, prenosi popravku u otvorenu stavku plana i povezuje izvorni dokaz. Journal se zatim može arhivirati dok popravka ostaje izričito otvorena.

Tok podržava projekte koji se duže razvijaju. Malom prototipu mogu biti dovoljni kratak pregled, plan i zapisi sesija. Postojeći nazivi dokumenata i korisne konvencije se čuvaju. Nema obaveznog tehnološkog steka, fiksnog kataloga dokumenata ni novog servisa za upravljanje projektom.

## Instalacija u Codexu

**Lokalna kopija ovog repozitorijuma nije potrebna.** Otvorite Codex razgovor sa pristupom mreži i pošaljite ovu poruku:

```text
Koristi $skill-installer i instaliraj skill project-docs-workflow sa adrese:
https://github.com/goranvuc/project-docs-workflow/tree/main/skills/project-docs-workflow

Instaliraj ga za mog korisnika, tako da bude dostupan kroz moje lokalne
Codex projekte, i prikaži stvarni direktorijum instalacije.
```

Ovo je poruka Codexu, a ne komanda za terminal. Ugrađeni Skill Installer preuzima folder skilla, uključujući reference i šablone. Nije potrebno ručno kloniranje niti build paketa. Pogledajte [zvanično Codex uputstvo](https://learn.chatgpt.com/docs/build-skills).

Ugrađeni installer pregledan za ovu verziju podrazumevano koristi:

```text
$CODEX_HOME/skills/project-docs-workflow/
```

Kada `CODEX_HOME` nije podešen, to je `~/.codex/skills/project-docs-workflow/`; na Windowsu obično `%USERPROFILE%\.codex\skills\project-docs-workflow\`. Merodavna je stvarna putanja koju installer prikaže. Codex podržava i `.agents/skills` lokacije; uspešno instaliran skill ne treba premeštati između direktorijuma.

U sledećoj poruci proverite učitavanje bez izmena projekta:

```text
Upotrebi $project-docs-workflow. Opiši podržane postupke i potvrdi
putanju SKILL.md fajla koji si učitao. Nemoj menjati fajlove.
```

Ako Codex ne prepozna skill, ponovo pokrenite Codex i pokušajte opet. Ako sam `$skill-installer` nije dostupan, primenite ručnu instalaciju opisanu ispod. Instalacija čini skill dostupnim; njegova primena na repozitorijum traži zaseban zahtev.

<details>
<summary>Ručna instalacija i rešavanje problema</summary>

Preuzmite ZIP repozitorijuma sa GitHuba, raspakujte ga i kopirajte **ceo** direktorijum `skills/project-docs-workflow` u korisnički direktorijum skillova, na primer `~/.agents/skills/`. Konačna putanja mora biti `~/.agents/skills/project-docs-workflow/SKILL.md`.

Za instalaciju vezanu za jedan repozitorijum koristite `<repository>/.agents/skills/project-docs-workflow/`. Zadržite jednu aktivnu instaliranu kopiju u željenom obuhvatu; dupli nazivi mogu otežati izbor. Nemojte kopirati samo `SKILL.md` niti ceo repozitorijum smestiti u dodatni podfolder skilla.

Za ponovljivu instalaciju koristite objavljeni tag ili commit SHA u GitHub adresi umesto `main`. Lokalna instalacija ne instalira skill automatski na drugi računar ili udaljeni host.

</details>

### Ažuriranje instalirane kopije

Pregledani installer odbija prepisivanje postojećeg odredišta. Nije automatski updater, a promene na GitHubu ne ažuriraju instaliranu kopiju.

Zatražite da Codex uporedi instaliranu kopiju sa željenom GitHub revizijom, sačuva lokalna prilagođavanja i instalira novu verziju u privremeni direktorijum. Posle pregleda zamenite staru kopiju uz očuvan povratni backup **van direktorijuma koje Codex pretražuje za skillove**. Ponovo proverite učitavanje. Nemojte brisati prilagođenu instalaciju samo da biste zaobišli grešku „already exists”.

## Prva upotreba

Pri uključivanju u postojeći projekat počnite procenom:

```text
Upotrebi $project-docs-workflow za procenu dokumentacije ovog repozitorijuma.
Pronađi sukobe merodavnih izvora, duple planove i nedostajuće dokaze za nastavak rada.
Predloži najmanji skup korisnih promena. Nemoj menjati fajlove.
```

Za uspostavljanje toka u novom projektu:

```text
Upotrebi $project-docs-workflow da ovde uspostaviš minimalan dokumentacioni tok.
Prilagodi ga stvarnom projektu i neka lokalna uputstva za agente budu samostalno upotrebljiva.
```

Za prilagođavanje postojećeg repozitorijuma:

```text
Upotrebi $project-docs-workflow da prilagodiš postojeći dokumentacioni tok.
Sačuvaj prihvaćene odluke i korisne dokumente. Poveži postojeće fajlove sa ulogama
pre dodavanja novih i zadrži jedan operativni plan.
```

Za obradu prikupljenih dokaza sesija:

```text
Upotrebi $project-docs-workflow za dokumentacionu fazu nad aktivnim journalima.
Uskladi aktuelne dokaze i prihvaćene odluke, ažuriraj relevantne ugovore
i plan, pa arhiviraj samo zapise čiji sav bitan sadržaj ima provereno
odredište. Nezavršeni implementacioni posao ostaje otvoren.
```

Običan razvoj zatim prati lokalna uputstva repozitorijuma. Skill nije potrebno pozivati u svakom zahtevu za kodiranje. Izmena jednog pasusa ne zahteva punu dokumentacionu fazu.

## Kako su delovi povezani

| Uloga | Za šta je merodavna |
|---|---|
| Lokalni `AGENTS.md` | Redosled čitanja, granice rada i usvojeni životni ciklus dokumentacije |
| Kratak pregled / mapa | Kontekst projekta i navigacija |
| Aktivni plan | Prioriteti, zavisnosti, vlasničke odluke i dokazi završetka |
| Fokusni ugovori | Stvarno ponašanje, prihvaćena namera i poznata odstupanja |
| Aktivni journal | Ishodi značajnih sesija i znanje koje čeka prenos |
| Obrađena arhiva | Sačuvani dokazi sa izričitim odredištima |

Ovo su uloge, bez propisanog broja fajlova. Skill pomaže da se tok uspostavi ili primeni; lokalna projektna uputstva ostaju trajni autoritet tokom običnog rada. Prihvaćena pravila projekta imaju prednost u odnosu na generičke šablone.

```text
Značajan rad → zapis sesije → dokumentaciona faza → obrađena arhiva
                    │                │
                    └── povezane izmene plana
                                     └── ugovori + izričito otvoreni zadaci
```

Arhiva beleži da je znanje obrađeno. Implementacioni zadatak se zatvara tek kada su njegovi kriterijumi završetka potkrepljeni dokazima.

## Disciplina koja omogućava da pristup funkcioniše

Ovaj pristup zahteva nekoga ko donosi odluke i pregleda dokaze. Agent može organizovati informacije i primenjivati tok; odgovornost za projekat ostaje kod vlasnika i saradnika.

1. **Održavajte jedan operativni plan.** U njemu određujte prioritete i zatvarajte posao. Journali i pregledi rizika mogu povezivati zadatke, ali ne treba da postanu konkurentni planovi.
2. **Izričito beležite odluke.** Razlikujte predloge od prihvaćenih izbora. Kada se izbor promeni, zabeležite šta ga zamenjuje i na šta promena utiče.
3. **Beležite značajne sesije.** Sačuvajte ishode, provere, dokumentaciju koja čeka prenos i otvoreni posao. Izbegavajte transkript svake komande i nov zapis za svaku sitnu izmenu ili pitanje.
4. **Obradite zapise pre nego što postanu teret.** Tražite dokumentacionu fazu na korisnim prekretnicama ili kada aktivni zapisi otežavaju početak sledeće sesije. Ritam prilagodite projektu.
5. **Sačuvajte otvorene nalaze.** Pre arhiviranja svaki bitan sadržaj mora dobiti proverljivo odredište. Otvoreni posao mora ostati vidljiv kada njegov izvorni journal bude premešten.
6. **Precizno označavajte dokaze.** Implementirano, lokalno testirano, commitovano, pushovano, deployovano i provereno u živom okruženju različite su tvrdnje. Navedite neuspehe, preskočene provere i neizvesnost.
7. **Pregledajte značenje i linkove.** Strukturno ispravan dokument može sadržati netačnu tvrdnju ili izostavljen nalaz. Proverite prenos od izvora do odredišta.
8. **Poštujte obuhvat i odgovornosti.** Dokumentacioni rad ne odobrava automatski implementaciju svakog nalaza, objavljivanje repozitorijuma, deployment servisa ili promene živih podataka. Postojeće ovlašćenje važi; ne dodajte ponovljena odobrenja za rutinski rad.

Ako odluke ostaju samo u razgovorima, a obrada zapisa se stalno odlaže, dokumentacija će se razići sa stanjem projekta. Više šablona to neće rešiti. Dokumenti treba da budu dovoljno mali za čitanje, a preuzete obaveze dovoljno realne za održavanje.

## Obuhvat i ograničenja

- Skill procenjuje, uspostavlja/prilagođava, konsoliduje i proverava dokumentacione tokove u Codexu. Druge agentske platforme nisu provereni podržani cilj ove verzije.
- Ne radi u pozadini, ne zakazuje održavanje, ne sinhronizuje instalirane kopije i ne primenjuje se sam na svaki repozitorijum.
- Ne donosi univerzalni alat za proveru projektne dokumentacije. Koristi postojeće provere gde su dostupne, a u ostalim slučajevima zahteva ručni pregled strukture i značenja.
- Ne potvrđuje spremnost za produkciju, ispravnost, bezbednost ili pravnu usklađenost. Pogledajte zabeležen [obuhvat provere](docs/validation.md).
- Čuva postojeća projektna pravila ovlašćenja. Instalacija ne daje nikakva dodatna prava nad repozitorijumom, nalozima, deploymentom ili podacima.

## Paket i doprinosi

Paket za instalaciju je [`skills/project-docs-workflow/`](skills/project-docs-workflow/SKILL.md). Sadrži osnovna uputstva, dve fokusirane reference, četiri prilagodljiva šablona i Codex UI metapodatke. Javni README fajlovi i alati za proveru ovog repozitorijuma održavaju se uz paket i ne kopiraju se pri standardnoj instalaciji foldera skilla.

U lokalnoj kopiji izvornog repozitorijuma Python 3.10+ može pokrenuti strukturnu proveru bez dodatnih zavisnosti:

```text
python scripts/validate.py
```

Provera obuhvata strukturu paketa, obavezne metapodatke i relativne Markdown linkove/ankere izvan ograđenih primera koda. Ne proverava spoljne URL adrese niti kvalitet odluka agenta. Značajne promene toka zahtevaju i realistične probe ponašanja u izolovanim primerima. Pogledajte [uputstva za održavanje](AGENTS.md) i [dokaze provere](docs/validation.md).

Uz predlog izmene navedite konkretan problem toka, mali primer i uticaj na postojeće projekte. Održavajte engleski i srpski README usklađenim. Prednost imaju dokazane potrebe u odnosu na dodatna pravila za hipotetičke slučajeve.

## Licenca

[MIT](LICENSE). Paket možete koristiti, prilagođavati i dalje distribuirati prema uslovima licence. Projekat se održava nezavisno i nije zvaničan OpenAI proizvod.
