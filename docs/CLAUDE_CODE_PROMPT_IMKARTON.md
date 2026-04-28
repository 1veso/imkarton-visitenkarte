# CLAUDE CODE PROMPTS — IMKARTON LEGAL DOCS + COPY-POLISH

> **Hinweis Jay:** Imkarton ist deutlich einfacher als Importia weil:
> - Visitenkartenseite ohne Effekte/Animationen die entfernt werden müssen
> - Copy-Polish ist hier nur Adress-Update (Trendiva Lux raus, Importia UG rein)
> - Daher ein einziger zweiphasiger Prompt der beides macht
>
> **Voraussetzung:** Lege die fünf Markdown-Files (IMPRESSUM.md, DATENSCHUTZ.md, COOKIE_HINWEIS.md, VORHALT_AGB_B2C.md, VORHALT_AGB_B2B.md, VORHALT_Widerrufsbelehrung.md) in den Ordner `legal_docs/` im Imkarton-Repo, BEVOR du Phase 1 absendest.

---

## PHASE 1 — ANALYSE & VORSCHLAG

```
Du bist ein erfahrener Senior Frontend Developer mit Spezialisierung auf statische Websites und DSGVO-konforme Web-Implementierung. Du arbeitest am Imkarton Projekt — der öffentlichen Marketing-Präsenz der Importia UG (haftungsbeschränkt) unter dem Internetauftritt imkarton.de, kommuniziert als "Kuratierter Versandhandler".

KONTEXT
========

Das Repository enthält die aktuelle Visitenkartenseite von Imkarton, derzeit deployed auf imkarton.pages.dev (Cloudflare Pages). Die Site enthält aktuell zwei Probleme die behoben werden müssen:

PROBLEM 1: Falscher Betreiber im Kontaktblock
Aktuell steht im Footer/Kontaktblock:
- Betreiber: Trendiva Lux
- Anschrift: Musterstraße 00, 00000 Musterstadt
- E-Mail: hello@imkarton.de

Das ist falsch. Der echte rechtliche Betreiber ist die Importia UG (haftungsbeschränkt), Weierstraße 10, 52349 Düren. Die korrekte E-Mail ist info@imkarton.de.

PROBLEM 2: Fehlende Legal Docs als Subpages
Die Site hat aktuell zwei Anker-Links #impressum und #datenschutz im Footer, die ins Leere führen. Es müssen zwei rechtskonforme Subpages eingebaut werden, plus Footer-Links die darauf zeigen.

QUELLDATEIEN
=============

Die Markdown-Quelldateien liegen bereits im Ordner legal_docs/ im Repo:

LIVE-DOKUMENTE (müssen als HTML-Subpages live geschaltet werden):
1. legal_docs/IMPRESSUM.md → wird zu /impressum.html
2. legal_docs/DATENSCHUTZ.md → wird zu /datenschutz.html

INTERNE DOKUMENTE (nicht live, nur intern):
3. legal_docs/COOKIE_HINWEIS.md (interne Beratungsempfehlung)
4. legal_docs/VORHALT_AGB_B2C.md (Vorhalt für künftiges B2C-Geschäft)
5. legal_docs/VORHALT_AGB_B2B.md (Vorhalt für künftiges B2B-Geschäft)
6. legal_docs/VORHALT_Widerrufsbelehrung.md (Vorhalt für künftiges B2C-Geschäft)

DEINE AUFGABE — PHASE 1 (NUR ANALYSE)
======================================

In dieser Phase implementierst du noch NICHTS. Du analysierst nur und lieferst einen Vorschlag.

Führe folgende Schritte aus:

1. STRUKTUR-SCAN
   - Liste die komplette Verzeichnisstruktur des Repos auf
   - Bestätige dass legal_docs/ existiert mit den richtigen .md Files
   - Identifiziere den Tech-Stack (Vanilla HTML/CSS/JS oder Framework)
   - Identifiziere wo CSS/Styling lebt
   - Identifiziere den Footer/Kontaktblock der index.html mit Zeilenangaben
   - Identifiziere alle Stellen mit "Trendiva Lux", "Musterstraße", "Musterstadt", "hello@imkarton.de"

2. DESIGN-SYSTEM EXTRAHIEREN
   - Schriftarten und ihre Verwendung
   - Farbpalette (CSS Custom Properties)
   - Layout-Konventionen (max-width, padding)
   - Erkennbare Stilelemente

3. IMPLEMENTATION-VORSCHLAG
   
   a) Subpage-Struktur:
      Beide Subpages sollen das gleiche Header/Footer-Design wie die Hauptseite haben, aber den Hauptinhalt durch einen Lese-Container mit max-width 720px ersetzen. Lese-Typografie mit line-height 1.65, klare Hierarchie zwischen H1/H2/H3.
   
   b) Markdown-zu-HTML-Konvertierung:
      Lies die .md Files und konvertiere zu semantischem HTML:
      - # → <h1>
      - ## → <h2>
      - ### → <h3>
      - #### → <h4>
      - **fett** → <strong>
      - GROSSGESCHRIEBENE Klauseln (z.B. WIDERSPRUCHSRECHT in DSE) als <p class="emphasize"> mit dezenter visueller Hervorhebung (Border-Left), NICHT als CSS text-transform, Originaltext bleibt großgeschrieben für Screen-Reader-Korrektheit
      - Listen → <ul> oder <ol>
      - Trennlinien --- → <hr>
      - Hinweise in [eckigen Klammern] bleiben als sichtbare Platzhaltertexte für den Mandanten
   
   c) Copy-Polish in index.html:
      Drei konkrete Änderungen:
      
      AKTUELL → NEU:
      - Betreiber: "Trendiva Lux" → "Importia UG (haftungsbeschränkt)"
      - Beschreibungszeile: "Handelsunternehmen für kuratierte Konsumgüter" → "Betreiber des Internetauftritts imkarton.de"
      - Anschrift "Musterstraße 00 / 00000 Musterstadt" → "Weierstraße 10 / 52349 Düren"
      - E-Mail "hello@imkarton.de" → "info@imkarton.de"
   
   d) Footer-Links:
      Aktuell sind im Footer zwei Anker-Links #impressum und #datenschutz. Diese müssen werden zu echten URLs:
      - #impressum → impressum.html
      - #datenschutz → datenschutz.html
      
      Falls zusätzlich eine Footer-Bar existiert (separates Element unten auf der Seite), beide Links auch dort einbauen für Compliance-Sicherheit (§ 5 DDG: Impressum muss in 2 Klicks von jeder Seite erreichbar sein).
   
   e) SEO/Meta:
      <title>: "Impressum — Imkarton" und "Datenschutz — Imkarton"
      <meta description>: kurzer Satz pro Page
      <meta robots>: index,follow
      canonical Tag pro Subpage
   
   f) Sitemap & robots.txt:
      Falls nicht vorhanden, erstellen:
      - sitemap.xml mit /, /impressum.html, /datenschutz.html
      - robots.txt mit Allow für Root, Disallow für /legal_docs/
   
   g) Vorhalt-Dokumente:
      Bleiben in legal_docs/ liegen, werden NICHT als HTML-Subpages gerendert.
      legal_docs/README.md erstellen die Live vs. Vorhalt klarstellt.

WICHTIGE EINSCHRÄNKUNGEN
=========================

- Du implementierst in dieser Phase NICHTS
- Das aktuelle Design der Hauptseite muss erhalten bleiben — nichts darf danach anders aussehen außer den drei Copy-Updates
- Keine externen Schriftarten nachladen falls die Site keine nutzt
- Kein JavaScript hinzufügen falls die Hauptseite keines hat
- Bei Google Fonts auf der Hauptseite: in Phase 1 als DSGVO-Risiko flaggen (LG München I, 3 O 17493/20), aber nicht selbst beheben

OUTPUT-FORMAT
=============

# 1. STRUKTUR-SCAN
[Verzeichnisbaum, gefundene Files, Tech-Stack]

# 2. DESIGN-SYSTEM
[Schriften, Farben, Stilelemente]

# 3. IDENTIFIZIERTE PROBLEM-STELLEN
[Alle Vorkommen von "Trendiva Lux", Musterstraße etc. mit Zeilenangaben]

# 4. IMPLEMENTATION-VORSCHLAG
## 4a) Subpage-Struktur
## 4b) Markdown-Konvertierung
## 4c) Copy-Polish in index.html
## 4d) Footer-Links
## 4e) SEO/Meta
## 4f) Sitemap & robots.txt
## 4g) Vorhalt-Dokumente

# 5. RISIKEN & EDGE-CASES

# 6. FREIGABE-FRAGE AN MICH
[Welche Entscheidungen brauchst du]

Beginne jetzt mit der Analyse.
```

---

## PHASE 2 — IMPLEMENTATION (NACH FREIGABE VON PHASE 1)

```
Sehr gut, dein Vorschlag aus Phase 1 ist freigegeben mit folgenden Anpassungen:

[FALLS KEINE ANPASSUNGEN: "Keine Anpassungen, setze deinen Vorschlag aus Phase 1 unverändert um."]

[FALLS ANPASSUNGEN: konkret auflisten]

DEINE AUFGABE — PHASE 2 (VOLLSTÄNDIGE IMPLEMENTATION)
======================================================

Setze jetzt alles in einem zusammenhängenden Edit-Pass um.

1. KOMPLETTE FILE-REPLACEMENTS / FILE-CREATIONS
   - Jede neue Datei (impressum.html, datenschutz.html) als KOMPLETTEN, lauffähigen Inhalt
   - Geänderte index.html als KOMPLETTE neue Datei
   - Keine Diffs, keine "..." Auslassungen
   - Ich kopiere die Files 1:1 ins Repo

2. SUBPAGES EDITORIAL-KONSISTENT
   Jede Subpage hat dieselbe Header/Footer-Struktur wie die Hauptseite, aber den Hauptinhalt durch einen Lese-Container ersetzen:
   
   - max-width: 720px
   - margin: 0 auto
   - padding: 80px 24px 120px (mobile: 48px 16px 80px)
   - line-height: 1.65
   - h1 etwas kleiner als Hero-h1 der Hauptseite
   - h2: 1.6rem, margin-top: 3rem
   - h3: 1.2rem, margin-top: 2rem
   - p: margin-bottom: 1rem
   - strong: font-weight 600
   - a: gleicher Style wie auf Hauptseite
   - .emphasize Klasse für GROSSGESCHRIEBENE Klauseln (Border-Left, dezenter Hintergrund, kein text-transform)
   - .stand Klasse für "Stand: April 2026" Footer der Subpage

3. MARKDOWN-KONVERTIERUNG
   Lies legal_docs/IMPRESSUM.md → konvertiere zu impressum.html
   Lies legal_docs/DATENSCHUTZ.md → konvertiere zu datenschutz.html
   
   - Hierarchie der Überschriften beibehalten
   - GROSSGESCHRIEBENE Klauseln (DSE 5.7) als <p class="emphasize"> mit Originaltext, nicht als text-transform
   - Listen sauber strukturieren
   - Keine Inhalts-Auslassungen
   - [Platzhalter in eckigen Klammern] sichtbar lassen für Mandant
   - Trennlinien --- als <hr>
   - "Stand: April 2026" als <p class="stand">

4. COPY-POLISH IN INDEX.HTML
   
   Drei konkrete Änderungen:
   
   a) Betreiber-Name:
      AKTUELL: "Trendiva Lux"
      NEU: "Importia UG (haftungsbeschränkt)"
   
   b) Beschreibungszeile darunter:
      AKTUELL: "Handelsunternehmen für kuratierte Konsumgüter"
      NEU: "Betreiber des Internetauftritts imkarton.de"
   
   c) Anschrift:
      AKTUELL: "Musterstraße 00 / 00000 Musterstadt"
      NEU: "Weierstraße 10 / 52349 Düren"
   
   d) E-Mail:
      AKTUELL: "hello@imkarton.de"
      NEU: "info@imkarton.de"
   
   e) Footer-Links:
      AKTUELL: <a href="#impressum"> und <a href="#datenschutz">
      NEU: <a href="impressum.html"> und <a href="datenschutz.html">
   
   Sonst NICHTS in index.html anfassen. Design, Layout, Typografie, alles andere bleibt unverändert.

5. SEO PRO SUBPAGE
   - <title>: "Impressum — Imkarton" und "Datenschutz — Imkarton"
   - <meta description> kurz, max 155 Zeichen
   - <meta robots>: index,follow
   - <link rel="canonical"> auf https://imkarton.pages.dev/impressum.html bzw. /datenschutz.html

6. SITEMAP.XML & ROBOTS.TXT
   sitemap.xml im Root mit drei URLs (Domain entsprechend imkarton.pages.dev)
   robots.txt mit Disallow: /legal_docs/

7. LEGAL_DOCS/README.md
   Erstelle die README.md mit einer Klarstellung welche Files Live sind und welche Vorhalt.

8. NACH IMPLEMENTATION
   
   A) Liste alle erstellten und geänderten Files
   B) Test-Checklist für mich:
      1. impressum.html im Browser öffnen → kein Layout-Bruch
      2. datenschutz.html im Browser öffnen → kein Layout-Bruch
      3. Footer-Links auf der Hauptseite → führen zu den Subpages
      4. Subpages-Footer-Links → führen zurück zur Hauptseite oder anderen Subpage
      5. Mobile-View (390px) → kein Layout-Bruch
      6. Console keine Fehler
      7. Im Kontaktblock der index.html steht: Importia UG (haftungsbeschränkt), Weierstraße 10, 52349 Düren, info@imkarton.de
   C) Mandant-Reminders:
      - Telefonnummer-Platzhalter: muss von Daugelaite/Geier ergänzt werden
      - USt-IdNr-Platzhalter: muss ergänzt werden sobald BZSt zugeteilt
      - Google Fonts DSGVO-Risiko falls externe Schriften geladen werden (LG München I, 3 O 17493/20)
      - Sync-Hinweis: Bei Änderung der .md Files müssen die .html Subpages manuell synchronisiert werden

WICHTIGE EINSCHRÄNKUNGEN
=========================

- Keine externen JavaScript-Bibliotheken hinzufügen
- Keine Tracking-Scripts, keine Analytics
- Keine Design-Änderungen außer den vier explizit aufgelisteten Copy-Updates
- Das aktuelle visuelle Erscheinungsbild der Imkarton-Site muss exakt erhalten bleiben

Beginne mit der Implementation. Reihenfolge:
1. impressum.html (komplett)
2. datenschutz.html (komplett)
3. Geänderte index.html (komplett, mit den 5 Copy-Updates)
4. sitemap.xml
5. robots.txt
6. legal_docs/README.md
7. Abschluss-Report mit Test-Checklist

Los.
```

---

## NUTZUNGSHINWEIS

**Voraussetzung:**
1. Lege die fünf Markdown-Files in legal_docs/:
   - IMPRESSUM.md
   - DATENSCHUTZ.md
   - COOKIE_HINWEIS.md
   - VORHALT_AGB_B2C.md
   - VORHALT_AGB_B2B.md
   - VORHALT_Widerrufsbelehrung.md

**Workflow:**
1. Phase 1 absenden in Claude Code
2. Antwort prüfen, Anpassungen einbauen falls nötig
3. Phase 2 absenden
4. Files testen, push, Cloudflare deployt
5. Final-Test auf imkarton.pages.dev

**Was NICHT mehr gemacht werden muss (im Vergleich zu Importia):**
- Keine Logo-Vergrößerung
- Keine Halo-Reduktion
- Keine Maus-Effekt-Entfernung
- Imkarton ist visuell sauber, nur die Texte stimmen nicht
