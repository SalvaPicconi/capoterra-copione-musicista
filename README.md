# CAPOTERRA — Copione musicista (29 agosto 2026)

Pagina separata per il musicista, ricavata dal file consegnato dall'attrice.
Contiene quattro letture e soltanto le indicazioni MUSICA/STOP MUSICA presenti
nel documento, senza accordi o istruzioni musicali aggiunte.

La pagina conserva selezione delle letture, scorrimento automatico regolabile,
corpo testo variabile, modalità palco, schermo intero e wake lock.

- Pagina autonoma, nessuna dipendenza esterna: `index.html`
- Pubblicata via GitHub Pages
- `noindex, nofollow`: la pagina è raggiungibile solo da chi ha il link

Il file `scripts/build_musicista_page.py` documenta la trasformazione effettuata
partendo dal layout della pagina live originale.

## Modifiche

Modificare `index.html`, poi:

```
git add -A && git commit -m "aggiorna copione" && git push
```

La pubblicazione si aggiorna in circa un minuto.
