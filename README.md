# CAPOTERRA — Copione musicista (29 agosto 2026)

Pagina separata per il musicista, ricavata dal file consegnato dall'attrice.
Contiene quattro letture, le indicazioni MUSICA/STOP MUSICA presenti nel
documento e le annotazioni musicali scritte a mano sul copione cartaceo:
titoli dei brani, giri di accordi, attacchi.

La pagina conserva selezione delle letture, scorrimento automatico regolabile,
corpo testo variabile, modalità palco, schermo intero e wake lock.

- Pagina autonoma, nessuna dipendenza esterna: `index.html`
- Pubblicata via GitHub Pages
- `noindex, nofollow`: la pagina è raggiungibile solo da chi ha il link

## Riferimenti sempre in vista

Sotto la barra dei comandi resta agganciata una fascia che mostra
l'indicazione musicale in corso — brano, giro di accordi, attacco — e
anticipa quella successiva, così la pagina può scorrere senza perdere il
riferimento. Il tasto `♪` (o `M`) la mostra e la nasconde.

Il colore dice cosa fare: rosso si suona, oro si suona da soli, blu si tace.

Mentre lo scorrimento automatico è attivo, su schermo stretto i comandi di
regolazione si ritirano e restano pausa, velocità e la fascia.

## Stato del testo

Il testo è stato confrontato con le pagine 1, 2, 3, 5 e 6 del copione
cartaceo: coincide parola per parola, comprese tutte le indicazioni musicali.
La pagina 4 non è ancora stata fotografata; il suo contenuto è confermato in
trasparenza attraverso il foglio precedente, ma l'attacco della III lettura
(`MUSICA ca. 30''`) resta senza annotazioni a mano.

## Modifiche

Modificare `index.html`, poi:

```
git add -A && git commit -m "aggiorna copione" && git push
```

La pubblicazione si aggiorna in circa un minuto.

`scripts/build_musicista_page.py` documenta la sola estrazione iniziale del
testo dal file dell'attrice: non conosce le annotazioni musicali e si ferma
da solo se le trova nella pagina.
