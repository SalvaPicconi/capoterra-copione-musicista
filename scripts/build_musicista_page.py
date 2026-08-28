"""Ricostruisce il solo testo del copione musicista dal file dell'attrice.

Documenta la trasformazione fatta la prima volta, partendo dal layout della
pagina live. Da allora la pagina ha guadagnato un secondo strato, che questo
script non conosce: le annotazioni musicali scritte a mano sul copione
cartaceo, la fascia dei riferimenti e i relativi stili. Rieseguirlo
riscriverebbe <main> perdendo quelle annotazioni, quindi si ferma da solo se
la pagina le contiene gia'.
"""

from __future__ import annotations

from html import escape
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

if 'id="hud"' in INDEX.read_text(encoding="utf-8"):
    sys.exit(
        "index.html contiene gia' le annotazioni del musicista: questo script "
        "le cancellerebbe. Modifica index.html a mano."
    )


def p(text: str, dialogue: bool = False) -> str:
    class_name = "narrative dialogue" if dialogue else "narrative"
    return f'<p class="{class_name}">{escape(text)}</p>'


def cue(text: str, cue_id: str, stop: bool = False) -> str:
    class_name = "cue stop" if stop else "cue"
    return f'<aside class="{class_name}" id="{cue_id}" tabindex="0"><strong>{escape(text)}</strong></aside>'


def reading(number: int, title: str, content: list[str]) -> str:
    roman = ["I", "II", "III", "IV"][number - 1]
    return (
        f'<section class="reading source-content" id="lettura-{number}" data-reading="{number}">'
        f'<p class="reading-marker">{roman} LETTURA</p><h2>{escape(title)}</h2>'
        + "".join(content)
        + '<div class="breath" aria-hidden="true"></div></section>'
    )


readings = [
    reading(
        1,
        "4. Risveglio",
        [
            cue("MUSICA ca. 30’’ – LA MUSICA CONTINUA SUL TESTO SUCCESSIVO", "cue-1-musica-30"),
            '<p class="ellipsis">…</p>',
            p('Appena apro gli occhi, il primo segnale che percepisco dal mondo esterno è il rumore dei macchinari a cui sono legato. Il “beep” ripetitivo, emesso a intervalli regolari di circa un secondo, detta il tempo al lento ritmo del mio risveglio.'),
            p('Sono ancora intontito. Tutto è ovattato intorno a me. Le luci, i colori, i suoni. Tutto appare sbiadito. Solo l’odore di disinfettante al fenolo sovrasta ogni mia altra percezione sensoriale e mi fa rinvenire nel qui e ora.'),
            p('La cannula che entra nella vena del mio braccio sinistro è attaccata alla flebo di fianco al mio letto.'),
            p('Sono sdraiato supino, avvolto in un camice bianco.'),
            p('- Si è appena svegliato, - sento la voce dell’infermiera che parla con il medico. Sono nella mia stanza, li vedo in fondo al mio letto, eppure la loro presenza mi sembra provenire da altri mondi.', True),
            cue("STOP MUSICA", "cue-1-stop-1", True),
            p('- Buongiorno signor Delpiano, - la voce del medico è calma e autoritaria allo stesso tempo. Mi danno il tempo di mettere a fuoco la situazione. Se mi fossi risvegliato dopo una serata alcolica, probabilmente sarei più lucido. La testa mi gira come se stessi smaltendo i postumi di una sbornia.', True),
            p('- Buongiorno dottore. Come è andata l’operazione al cuore?', True),
            p('- Non ha fatto alcuna operazione al cuore. È vittima di un incidente stradale. È stato investito da un’auto e ha avuto un trauma cranico. È rimasto in coma per...', True),
            p('Non lo lascio finire di parlare.'),
            p('- Dottore, probabilmente mi confonde con un altro paziente. Io sono stato operato al cuore.', True),
            p('Il chirurgo alza la mano destra con il palmo aperto davanti a me, come se volesse bloccare la mia voce con le dita.'),
            p('- Si calmi ora.', True),
            p('Io insisto:'),
            p('- Se mi apre il camice le faccio vedere la cicatrice sul petto.', True),
            p('- Non ha nessuna cicatrice.', True),
            p('Vorrei capirci qualcosa e provo a guardarmi lo sterno, ma, legato ai tubi e ancora dolorante, non riesco a piegare il collo.'),
            p('- Potreste portarmi uno specchio? Voglio vedere con i miei occhi.', True),
            p('Il chirurgo, molto paziente, fa arrivare uno specchio e me lo pone davanti agli occhi. Lo inclina in modo tale che io possa osservare il mio torace. Ha ragione, non c’è nessuna cicatrice. Nello specchio vedo il volto di una persona che ha subito un trauma, ma non c’è segno di bisturi.'),
            cue("MUSICA", "cue-1-musica-2"),
            p('Vado in crisi. Non trovo quel riferimento che cerco e che confermerebbe l’operazione che penso di avere affrontato. Eppure, sono sicuro di non averla sognata. Era tutto troppo nitido per essere un sogno. Direi addirittura più chiaro di quello che sto vivendo ora, in uno stato di confusione, di smarrimento.'),
            p('Vengo travolto da un’infinita onda di ansia e angoscia e inizio a urlare tutta la mia disperazione per ciò che sembra portarmi lontano dalle mie certezze'),
            cue("STOP MUSICA (NETTO)", "cue-1-stop-netto", True),
            p('- È ancora in stato confusionale, sedatelo, - ordina il medico all’infermiere.', True),
        ],
    ),
    reading(
        2,
        "11. Beata solitudine (1^ Parte)",
        [
            p('La necessità di essere solo trova una verifica qualche mese più tardi, durante uno dei miei ricoveri in ospedale. Nell’unità spinale di Fiorenzuola d’Adda condivido la camera con altri due giovani motociclisti, entrambi vittime di incidenti stradali. Uno è paralizzato dalla vita in giù, all’altro sono stati amputati un braccio e una gamba. Entrambi si trovano nella fase “calda” del post-trauma, quella fase in cui gli sguardi sono rivolti al passato appena trascorso, a ciò che si è fino all’istante in cui il dramma accade. Vedersi in una condizione assai diversa non è ancora possibile; si lotta con la paura e con il buio che sembra avere avvolto le proprie esistenze; si è disperatamente immersi nel dolore di una realtà che non era prevista a quella età: il corpo mutilato per sempre.'),
            p('Io occupo il letto centrale. Alla mia sinistra c’è il ragazzo amputato. È in sedia a rotelle, parla poco e ha lo sguardo che sembra andare oltre i muri dell’ospedale e perdersi chissà dove; non riceve mai visite. Nel suo trascorrere silenzioso il tempo mi colpiscono i suoi occhi. Sono fermi e intensi e parlano di ricerca, più che di resa; comunicano la forza costante di un guerriero che accoglie il momento doloroso senza perdere di vista un suo misterioso obiettivo. Io non sono ancora in grado di capire quale possa essere, ma i suoi silenziosi occhi magnetici mi attirano e mi appaiono come qualcosa di sconosciuto che forse vale la pena di scoprire.'),
            p('Non parla mai e lotta per ingoiare un cucchiaio di minestra, per prendere un libro o il telefonino, per trasferirsi dal letto alla sua sedia a rotelle, come per ogni piccolo, elementare gesto nel corso della giornata. Fa una grande fatica, ma ci prova sempre, facendosi forza grazie alla sua rabbia che trasuda di un grande amore per sé stesso.'),
            p('Alla mia destra c’è il ragazzo paraplegico. La sedia di fianco al suo letto viene occupata ogni giorno e per diverse ore dalla madre.'),
            p('La donna è servizievole. Lo imbocca, lo aiuta a vestirsi, a lavarsi... insomma, fa tutto quello che può per lui. Il ragazzo, travolto dal suo amore, mi appare ormai rassegnato al ruolo di comparsa passiva della sua esistenza. La madre, invece, al termine di ogni giornata, prima di lasciarlo si abbandona a un pianto di tristezza. In quel quotidiano saluto, come in tanti altri momenti della sua giornata, percepisco il rivivere un lutto da cui non ci si vuole distaccare.'),
            p('La sensazione che entrambi stiano formando un immenso abbraccio per tenere vivo e presente tutto ciò che è svanito nel trauma, sprofondando in un pianto continuo, è sconvolgente. Nessuno dei due sembra voler lasciare andare ciò che non esiste più, per attraversare quella selva oscura e sconosciuta in cui tanto, se non tutto, dovrà essere rivisto e rimodulato in virtù di una nuova condizione fisica.'),
            p('E così, io mi sento di fronte a un bivio da intraprendere:'),
            cue("MUSICA", "cue-2-musica"),
            p('mi proietto in entrambe le storie, mi ci immergo con ogni mia cellula, provando a raccogliere ogni sensazione che ciascuna delle due mi potrebbe dare. Ma, mentre osservo quella mamma - che in quel momento rappresenta la mia- immaginando al suo fianco anche il mio caro babbo, vengo scosso dalla potente e chiara percezione di una “strada” ad alto rischio. Anzi, sento che, se coinvolgessi i miei genitori nella mia storia, correrei due rischi.'),
            p('Il primo è che crollino in mille pezzi, che sprofondino nel buio e nel dolore, smarrendo qualcosa che dovrebbe rimanere indipendente da me: la loro voglia di sorridere alla vita.'),
            p('Il secondo, ed è questo ciò che più mi spaventa, è che io accetti la loro immagine di dolore, facendomi intrappolare e finendo per rinunciare alla “lotta” senza più reagire a quanto il destino mi ha proposto! Vedo, come in un film, che potrei scivolare nella parte di vittima che deve essere “accolta” e “accudita”, reclamando in modo perpetuo il loro aiuto; mi intravedo orrendamente avvolto in una condizione di resa passiva e tristemente rinunciataria.'),
            cue("… SOLO MUSICA ca. 20’’ POI STOP", "cue-2-solo-20", True),
            p('Un padre e una madre sono preziosi per darti un abbraccio. Ma c’è il rischio che quell’abbraccio diventi così affettuoso da soffocarti e impedirti di sperimentare in prima persona il mondo che dovrà appartenerti e che potrà consegnarti immense parti di te che ancora non conosci. Un amore cieco, come quello dei genitori, se da un lato può essere estremamente nutriente e protettivo, dall’altro, se mal dosato, può portare alla resa.'),
            p('Voglio evitare di sviluppare quella malsana tendenza di chiedere aiuto quando non ne ho realmente bisogno. E non vorrei mai vedere mio padre o mia madre piangere accanto al mio letto, tenendo stretta tra le mani del cuore l’immagine di me che corre con la bici o gioca a pallone. Poi, oltre alle mie, dovrei asciugare anche le loro lacrime.'),
            p('- È dura stare lontano, - mi dirà un giorno mia mamma, durante una nostra conversazione.', True),
            p('- Sarebbe ancora più duro starmi vicino, credimi mamma, - le risponderò io.', True),
        ],
    ),
    reading(
        3,
        "16. Tra Cuore e Follia",
        [
            cue("MUSICA ca. 30’’ – LA MUSICA CONTINUA SUL TESTO SUCCESSIVO", "cue-3-musica-30"),
            p('Mi dico che l’essere ancora qui, ancora vivo, è un dono che merita di essere accolto con riconoscenza e gratitudine. E se non posso fare quello che vorrei, allora posso almeno immaginarlo, “sentirlo” con la forza del Cuore, e provare a viverlo dentro di me.'),
            p('In piscina sfogo la mia rabbia e la mia frustrazione e poi, una volta ripulito da tutti i sentimenti e le emozioni nocive, mi chiedo: “Cosa voglio provare, ora? Cosa vorrei “sentire”, in questo momento?” Ogni giorno la mia replica è diversa.'),
            p('Può esserci il giorno che mi rispondo: - Voglio correre! - ad esempio. So che non è possibile, ma è qui che entra in gioco la follia.'),
            p('Attuo un esercizio di visualizzazione. Chiudo gli occhi e mi immagino in pantaloncini e maglietta, in una giornata di sole primaverile, su una strada della mia Sardegna che era uno dei miei percorsi preferiti quando mi allenavo, prima dell’incidente. Immagino le mie gambe muoversi, il mio respiro farsi più corto via via che il passo aumenta. Poi vedo il paesaggio che scorre al mio fianco e sento il vento in faccia, tra i capelli: una carezza che mi sfiora e che mi fa percepire come parte della magnificenza della Natura.'),
            p('Sono in vasca, immerso per metà nell’acqua, eppure sto correndo. E così, tutte le volte che voglio correre, immagino di farlo. O tutte le volte che voglio essere sdraiato sul bagnasciuga della mia spiaggia preferita in Sardegna, lo immagino.'),
            p('Il desiderio non lo senti nella Mente o nella Pancia. Lo senti nel Cuore. Il Cuore ricerca quel senso di libertà che provava ogni volta che infilavo le scarpette da running o che mi trovavo nella mia terra, sui monti, tra distese di cisto o lentischio.'),
            p('La Mente lo immagina, razionalmente, aggiungendo dettagli sensoriali che ben mi sono noti. Che sapore ha? Che emozione comporta? Cosa provo?'),
            p('E a quel punto la Pancia ascolta e si emoziona. Tutto il mio corpo è scosso dalla stessa vibrazione che provavo quando correvo o quando vivevo la Natura della mia Sardegna. La follia sta nel riprodurre in me quelle stesse frequenze, anche se sono altrove.'),
            p('Quando Cuore, Mente e Pancia lavorano insieme, creano un ponte capace di raggiungere, tra le infinite circostanze, la manifestazione di una sola possibilità, quella desiderata.'),
            p('Il Cuore può sentire dolore o gioia. Sintonizzalo sulla gioia. La Mente può sentire chiarezza o confusione. Ma se il Cuore la orienta alla gioia, sentirà solo chiarezza. La Pancia può sentire pesantezza o leggerezza, a seconda dei pensieri che ci passano per la Mente. Sentiamo “le farfalle” quando siamo innamorati e pensiamo alla persona amata, sentiamo “un pugno nello stomaco” quando siamo scossi dalla delusione o dal dolore, o pensiamo a un torto subito, a un piano naufragato. Tutti noi possiamo diventare energeticamente i creatori del nostro desiderio.'),
            cue("STOP MUSICA", "cue-3-stop", True),
            p('A me cosa serve immaginare di correre, se poi so bene che non avrei mai più potuto farlo? Serve a sentirmi vivo. Serve a farmi andare avanti, follemente, con coraggio. Serve a mantenere accesa la fiammella della speranza; mi aiuta a scoprire che ogni esperienza che in passato ho attraversato, e che mi ha fatto vibrare, aveva come unico scopo proprio quell’immensa e sottile vibrazione. E allora scelgo di arrivarci per un’altra via; l’immaginazione attiva.'),
            p('E a poco a poco scopro che il mio traguardo non è più correre, ma fare questa esperienza di... follia. La visualizzazione e la voce del mio Cuore diventano la mia forza. Accetto quello che sto vivendo, ringrazio l’universo per avermi destinato a questo viaggio e da questo momento inizio a dare tutto me stesso. Me la vivo. Me la gioco. So che ci sarà ancora tanto dolore, sofferenza, rabbia. Ma inizio anche a sentire il gusto e il sapore di quello che vivo. Divento il primo tifoso di me stesso. Mi dico “bravo” quando mi guardo indietro e vedo la strada che ho percorso. Inizio a sentire ogni giorno, sempre più, un profondo senso di gratitudine.'),
            p('E non importa se non vedo la meta. Se da una parte non avere un traguardo di guarigione può essere drammatico, dall’altra mi concede di prendermi tutto il tempo di cui ho bisogno. Mi rendo conto che il viaggiare è il mio traguardo. Non ho una meta, se non quella di continuare a sperimentare.'),
            p('Più mi impegno, più esercito la mia intenzione, più metto in gioco la mia forza di volontà, più “sento” che sto imparando su un piano superiore a quello materiale.'),
            p('Una persona normale si sveglia la mattina, si alza, si veste, va a lavorare. Per me compiere in autonomia il breve tragitto di un corridoio è una conquista.'),
            p('Devo metterci tutto me stesso per stare in piedi e muovere un piede dopo l’altro. Ma ora la vita è diventata molto più ricca. Mi sento come un bimbo che esplora il mondo a poco a poco e si stupisce per tutto. Do valore a cose che prima davo per scontate. E riesco a farlo perché rimango nel Cuore. Se continuassi a pensare solo con la Mente, mi direi semplicemente che sono uno sfigato, probabilmente impazzirei o sarei sbranato da pensieri oscuri che potrebbero condurmi verso un punto di non ritorno. La follia mi permette di trovare possibilità che prima non vedevo.'),
            p('Nei mesi che seguiranno riuscirò a guidare l’auto utilizzando la mia stampella per schiacciare la frizione. Troverò un modo per entrare allo stadio di Torino senza biglietto e assistere al concerto degli U2. Riuscirò a raggiungere sulla mia sedia a rotelle una spiaggia remota e protetta nella mia Sardegna, superando ostacoli e barriere che sarebbero stati impervi anche per una persona in salute.'),
            p('Da questo momento in poi la follia è ciò che mi permette di andare avanti e trasformarmi da dis-abile a div-abile (divinamente abile).'),
            cue("MUSICA ca. 60’’", "cue-3-musica-60"),
        ],
    ),
    reading(
        4,
        "51. Tutto il mare che ho nel cuore",
        [
            p('È mattino presto e la primavera del 2015 è alle porte. Sento che l’aria frizzante provoca qualcosa di eccitante in me. Mentre accompagno mia figlia alla scuola materna mi ritorna in mente il giorno in cui lei, innocente e sincera come solo i piccoli sanno essere, mi chiese: - Papà, ma tu sei felice del lavoro che fai?'),
            p('Ora, a distanza di pochi anni, sono pronto a consegnarle la risposta che in quel momento non potevo darle; la sua domanda era giunta come un sasso scagliato da una fionda e non mi aveva dato il tempo di costruire un pensiero autentico, per me e per lei.'),
            p('Senza esitazione ora le direi: - Sì, figlia mia, sono davvero felice. Amo il mio lavoro e sono immensamente grato per ciò che oggi sono e faccio. Ho salutato con gratitudine il cammino professionale percorso e ringraziato i miei genitori, tuoi nonni, per avermi dato la possibilità di studiare e laurearmi. Ma quel periodo si è concluso. Sono finalmente approdato in un nuovo “mondo”, e quasi faccio fatica a considerare lavoro ciò che oggi faccio.'),
            p('Quello che mi accadde tanti anni fa mi ha portato a scoprire un mondo sommerso che ogni essere umano possiede, fatto di risorse e strumenti che possono rimanere nascosti per tutta la vita. Avere sperimentato tanto dolore e tanta sofferenza mi ha lentamente condotto in una dimensione in cui niente è scontato e gratuito. È uno spazio interiore in cui ho compreso che dovevo dare nuova vita a ciò che mi era rimasto e attingere da me stesso quelle risorse che erano ancora presenti: la volontà, la perseveranza, l’immaginazione, la follia (quanto basta!), ma, soprattutto, la riconnessione con il mio cuore. A quel punto, giorno dopo giorno, ho scoperto che nulla era impossibile. E allora sì, figlia mia, ti dico ancora una volta che sono davvero felice di essere oggi un counselor al servizio di chi, come accadde a me, vive un momento di temporanea difficoltà, aiutandolo e sostenendolo per scoprire tutte le sue risorse e le sue abilità, per migliorare la sua qualità di vita e divenire padrone del suo destino e artefice di una grande trasformazione. Tutti noi dobbiamo attraversare momenti bui e difficili e tutti noi abbiamo la possibilità di immergerci in quell’oscurità e scoprire che nel nostro Cuore possediamo “un mare dentro” e che da esso potremo attingere tutte le risorse che ci serviranno per sconfiggere il buio per giungere a una luce bellissima.'),
            cue("MUSICA", "cue-4-musica"),
            p('Dopo avere salutato Mimì, come ogni mattina mi dirigo verso il mio studio, nel cuore del quartiere “Oltretorrente”, appena al di là della sponda ovest del fiume Parma che taglia in due la città. Giusto il tempo di prendere un caffè nel piccolo bar accanto allo studio ed eccomi ad accogliere il primo cliente della giornata.'),
            p('Ancora una volta sono pronto, con totale disponibilità, a esserci per chi suonerà il campanello del portoncino nero con la maniglia dorata, per ascoltarlo con accettazione incondizionata e senza giudizio, e accompagnarlo nel suo cammino, convinto che la sua storia, indipendentemente da ciò che avrà da raccontarmi, avrà un filo comune con tutte le altre (la mia compresa): la vita è un mistero e se cerchi troverai esattamente ciò di cui hai necessità per trasformarla in un’esperienza meravigliosa e irripetibile.'),
            cue("STOP MUSICA", "cue-4-stop", True),
            p('Perché ciascuno di noi è sempre in grado di cambiare il proprio destino.'),
        ],
    ),
]


intro = (
    '<section class="intro source-content" id="inizio">'
    '<h1 class="document-title">CAPOTERRA</h1>'
    '<p class="event-line">COPIONE MUSICISTA · LETTURE EVENTO 29 AGO 2026</p>'
    '<aside class="guide"><p><strong>GUIDA RAPIDA</strong></p>'
    '<p>Il testo e le indicazioni musicali riproducono il file consegnato dall’attrice.</p>'
    '<p>Le indicazioni MUSICA e STOP MUSICA sono evidenziate lungo il copione.</p>'
    '<p>Usa il menu superiore per passare fra le quattro letture.</p></aside></section>'
)


html = INDEX.read_text(encoding="utf-8")
html = html.replace("<title>CAPOTERRA — Copione live</title>", "<title>CAPOTERRA — Copione musicista</title>")
html = html.replace("CAPOTERRA · LIVE", "CAPOTERRA · MUSICISTA")
html = re.sub(
    r'<select id="readingSelect" aria-label="Vai alla lettura">.*?</select>',
    '<select id="readingSelect" aria-label="Vai alla lettura">'
    '<option value="inizio">Inizio e guida</option>'
    '<option value="lettura-1">I · 4. Risveglio</option>'
    '<option value="lettura-2">II · 11. Beata solitudine (1^ Parte)</option>'
    '<option value="lettura-3">III · 16. Tra Cuore e Follia</option>'
    '<option value="lettura-4">IV · 51. Tutto il mare che ho nel cuore</option>'
    '</select>',
    html,
    count=1,
    flags=re.S,
)
html = re.sub(
    r'<p class="screen-note">.*?</p>',
    '<p class="screen-note">Copione musicista con le sole indicazioni presenti nel file dell’attrice. Premi “▶ Scorri” per l’avanzamento automatico e regola “Vel.” anche durante la lettura. Barra spaziatrice: avvio/pausa.</p>',
    html,
    count=1,
    flags=re.S,
)
html = re.sub(
    r'<main id="copione">.*?</main>',
    '<main id="copione">' + intro + "".join(readings) + '</main>',
    html,
    count=1,
    flags=re.S,
)
html = html.replace(
    '.cue:focus-visible {',
    '.cue.stop { background: var(--blue-bg); border-color: var(--blue); color: var(--blue); }\n.cue:focus-visible {',
)
html = html.replace("capoterra-size", "capoterra-musicista-size")
html = html.replace("capoterra-scroll-speed", "capoterra-musicista-scroll-speed")
html = html.replace("capoterra-stage", "capoterra-musicista-stage")
INDEX.write_text(html, encoding="utf-8")

