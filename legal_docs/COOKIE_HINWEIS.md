# COOKIE-HINWEIS & EMPFEHLUNG

**Stand: April 2026**

---

## Beratungsempfehlung vorab

Eine Visitenkartenseite, die ausschließlich auf Cloudflare Pages gehostet ist und KEINE der folgenden Tools einsetzt:

- Google Analytics, Matomo, Plausible (mit Cookies)
- Meta Pixel / Facebook Pixel
- Google Tag Manager mit Tracking-Tags
- YouTube-/Vimeo-Embeds (im Standard-Modus)
- Google Maps (eingebettet)
- Google Fonts (extern geladen)
- Schriftarten von externen CDNs (z.B. fonts.googleapis.com)
- Externe Skripte mit Tracking-Funktion

**...benötigt im Idealfall KEINEN Cookie-Banner.**

Cloudflare Pages selbst setzt im Auslieferungsbetrieb in der Regel keine **technisch nicht notwendigen** Cookies. Cloudflare-eigene Sicherheits-Cookies (z.B. `__cf_bm` für Bot-Management) gelten als technisch erforderlich nach § 25 Abs. 2 Nr. 2 TDDDG und benötigen keine Einwilligung, müssen aber in der Datenschutzerklärung erwähnt werden (ist bereits im Hosting-Abschnitt der Datenschutzerklärung abgedeckt).

## Empfehlung für die Imkarton-Site

**Variante A (empfohlen für jetzt): KEIN Cookie-Banner**

Solange die Site rein statisch ist, keine Drittanbieter-Skripte lädt, keine Webfonts extern lädt, keine Embeds enthält und kein Tracking nutzt, ist ein Cookie-Banner rechtlich nicht erforderlich und sogar UX-schädlich.

**Pflicht in diesem Fall:** Datenschutzerklärung verlinken (ist bereits gegeben durch Footer-Link) und die Cloudflare-Verarbeitung dort transparent darstellen (ist bereits in der Datenschutzerklärung enthalten).

## Wichtiger Hinweis zu Google Fonts

Falls die Imkarton-Site Schriften extern von Google Fonts (fonts.googleapis.com) lädt, besteht ein DSGVO-Risiko nach LG München I (Urteil vom 20.01.2022, 3 O 17493/20). Das Gericht hat in diesem Urteil erkannt, dass die unautorisierte Übertragung der IP-Adresse an Google ohne ausdrückliche Einwilligung des Nutzers eine Verletzung des allgemeinen Persönlichkeitsrechts darstellt.

**Empfehlung:** Vor Live-Schaltung prüfen, ob Schriften extern geladen werden. Falls ja:

- **Beste Lösung:** Schriften lokal hosten (Self-Hosting via @font-face mit Files in `/assets/fonts/`)
- **Akzeptable Lösung:** Cookie-Consent-Banner mit Einwilligung vor Font-Load
- **Schlechteste Lösung:** Status quo + DSE-Erweiterung um Google-Fonts-Abschnitt (transparente Information, aber kein Risikoausschluss)

**Variante B (für später): Cookie-Banner mit Einwilligung**

Sobald einer der folgenden Punkte zutrifft, MUSS ein einwilligungsbasierter Cookie-Banner integriert werden (mit "Alle ablehnen"-Button auf der ersten Ebene, gleichwertig zu "Alle akzeptieren", entsprechend OLG-Rechtsprechung und Aufsichtsbehörden-Praxis):

- Einbindung von Google Analytics, Meta Pixel oder vergleichbaren Tools
- Einbindung von Google Fonts ohne lokales Hosting
- Einbindung von YouTube-Videos ohne "youtube-nocookie.com"-Modus
- Einbindung von Google Maps
- Einbindung von Werbenetzwerken
- Einbindung von Tracking- oder Retargeting-Skripten
- Aktivierung eines Shop-Bereichs mit Bestell- und Zahlungsfunktionen

---

## OPTION: Minimaler Hinweistext (falls Mandant trotzdem einen Hinweis möchte)

Falls der Mandant aus Vorsichtsprinzip einen kurzen Cookie-Hinweis einbauen möchte, ohne einen vollwertigen Consent-Banner zu integrieren, kann folgender Hinweistext genutzt werden. Dieser ist KEINE Einwilligungsabfrage, sondern eine reine Information gemäß Transparenzgrundsatz:

### Empfohlener Hinweistext (kein Banner, sondern z.B. einmalige dezente Bottom-Notiz):

> **Hinweis zur Nutzung dieser Website**
>
> Diese Website nutzt ausschließlich technisch notwendige Cookies und Verbindungsdaten, die für den sicheren Betrieb der Seite erforderlich sind (z.B. zur Abwehr automatisierter Angriffe durch unseren Hosting-Anbieter Cloudflare). Eine Verarbeitung zu Analyse-, Werbe- oder Tracking-Zwecken findet nicht statt.
>
> Weitere Informationen finden Sie in unserer [Datenschutzerklärung](/datenschutz).
>
> [Verstanden]

---

## OPTION: Vollwertiger Consent-Banner-Text (nur falls Tracking eingebaut wird)

Falls in Zukunft Tracking-Tools oder Shop-Funktionen eingebaut werden, hier der Vorlage-Text für einen rechtskonformen Consent-Banner:

### Banner-Layer 1 (gleichwertige Buttons "Alle akzeptieren" und "Alle ablehnen" sind PFLICHT):

> **Cookie-Einstellungen**
>
> Wir verwenden Cookies und ähnliche Technologien, um Ihnen eine optimale Nutzung unserer Website zu ermöglichen. Einige Cookies sind technisch erforderlich, andere helfen uns, das Verhalten unserer Besucher zu analysieren oder Inhalte von Drittanbietern einzubinden.
>
> Ihre Einwilligung umfasst auch die Übermittlung Ihrer Daten in Drittländer (z.B. USA), in denen kein der EU vergleichbares Datenschutzniveau besteht. Sie können Ihre Einwilligung jederzeit in den Cookie-Einstellungen widerrufen.
>
> [ Alle akzeptieren ]   [ Alle ablehnen ]   [ Einstellungen ]
>
> [Datenschutz](/datenschutz) | [Impressum](/impressum)

### Banner-Layer 2 (granulare Auswahl):

> **Cookie-Einstellungen anpassen**
>
> ☑ **Notwendig** (immer aktiv)
> Erforderlich für den Betrieb der Website. Diese Cookies können nicht deaktiviert werden.
>
> ☐ **Statistik**
> Helfen uns zu verstehen, wie Besucher mit unserer Website interagieren.
>
> ☐ **Marketing**
> Werden verwendet, um Besuchern auf Websites zu folgen und relevante Anzeigen einzublenden.
>
> ☐ **Externe Medien**
> Inhalte von Drittanbietern wie Videos oder Karten.
>
> [ Auswahl speichern ]   [ Alle akzeptieren ]

---

## Technische Umsetzungshinweise

Bei späterer Banner-Integration empfehle ich folgende DSGVO-konforme Lösungen:

- **Cookiebot** (kostenpflichtig, sehr DSGVO-konform, automatisches Cookie-Scanning)
- **Usercentrics** (kostenpflichtig, Premium-Lösung)
- **Klaro!** (Open Source, kostenlos, sehr empfehlenswert für statische Sites)
- **Eigenentwicklung** (bei einfachen Setups oft die beste Lösung, volle Kontrolle, kein Drittanbieter)

**Wichtig bei der Banner-Implementierung:**

1. Skripte mit Cookie-Setzung dürfen ERST NACH Einwilligung geladen werden ("Consent before Loading")
2. "Alle ablehnen" muss auf Layer 1 gleichwertig zu "Alle akzeptieren" sein (BGH-Rechtsprechung)
3. Vorausgewählte Checkboxen für nicht-notwendige Cookies sind unzulässig (EuGH "Planet49"-Urteil)
4. Widerruf muss genauso einfach sein wie die Einwilligung (sichtbarer "Cookie-Einstellungen ändern"-Link im Footer)
5. Einwilligung muss dokumentiert werden (Logging mit Zeitstempel und gewählten Optionen)

---

*Stand: April 2026*
