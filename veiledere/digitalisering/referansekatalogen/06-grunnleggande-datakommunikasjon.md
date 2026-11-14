---
veileder: "Referansekatalogen for IT-standardar"
utgiver: "Digitaliseringsdirektoratet (Digdir)"
kilde: "https://www.digdir.no/standarder/grunnleggande-datakommunikasjon/1488"
hentet: "2026-11-14"
---

# Referansekatalogen for IT-standardar Grunnleggande datakommunikasjon

Bruksområdet gjeld protokollar for grunnleggande datakommunikasjon.

Laga: 13. mai 2020

Sist endra: 08. februar 2024

## Anbefalte og obligatoriske standardar

Offentlege verksemder bør ha støtte for alle standardane innanfor dette bruksområdet. Andre standardar kan støttast i tillegg. Her er anbefalte og obligatoriske krav til standardar innanfor dette bruksområdet:

Kravet om sikker datakommunikasjon frå offentlege nettstader vart innført 8. oktober 2021.

*"Forskrift om IT-standarder i offentlig sektor" regulerer dette kravet i §11:*

**§ 11.*****Obligatoriske standarder for kryptert datakommunikasjon med offentlige nettsteder og -tjenester***

Nettsteder og andre offentlige tjenester, herunder applikasjonsgrensesnitt (API-er), som benytter hypertekstoverføringsprotokollen (http) skal kryptere kommunikasjonen med transportlagssikkerhet i henhold til standarden HTTP over TLS [RFC 2818] ved bruk av protokollene HTTP/1.1 [RFC 7230 til RFC 7235] og TLS 1.2 [RFC 5246] eller TLS 1.3 [RFC 8446]. Fram til 1.1.2024 skal TLS 1.2 brukes, hvis en av kommunikasjonspartene ber om det. Kravet gjelder ikke lukkede tjenester hvor forvaltningsorganet ivaretar sikkerheten på annen måte. Dersom en tjeneste får en forespørsel om kommunikasjon over HTTP uten bruk av TLS skal tjenesten svare ved omdirigering til same URL med bruk av HTTP over TLS.

Anbefalinga om sikker bruk av domenenamnsystemet vart innført 30.10.2018.

Det er anbefalt å nytte Domain Name System Security Extensions (DNSSEC) [RFC 4033, RFC 4034 og RFC 4035] for alle domenenamn ei verksemd har registrert, og at det berre vert nytta resolvarar som validerer DNS-oppslag.

**Krav til bruk av standardar**

- RFC 4033 – DNS Security Introduction and Requirements
- RFC 4034 – Resource Records for the DNS Security Extensions
- RFC 4035 – Protocol Modifications for the DNS Security Extensions

Desse standardane vert reviderte enkeltvis av IETF og Digitaliseringsdirektoratet vil oppdatere anbefalinga med gjeldande versjon av kvar standard når dette skjer. Dersom ein revisjon fører til større endringar vil Digitaliseringsdirektoratet vurdere behovet for å revidere heile anbefalinga. Revisjonar som fører til større endringar vil verte behandla av Standardiseringsrådet.

Anbefalinga om transportsikring av e-post mellom e-postservarar vart innført 1.12.2016 og sist oppdatert 11.1.2019.

Det er anbefalt å nytte transportsikring av e-post mellom e-post servarar, både ved sending av e-post til offentlege verksemder og ved sending av e-post til innbyggarar og næringsliv. Som prioritert løysing er det anbefalt å nytte SMTP Security via Opportunistic DNS-Based Authentication of Named Entities (DANE) Transport Layer Security (RFC 7672). Dersom motpart i utvekslinga av ei e-postmelding ikkje støttar denne spesifikasjonen skal SMTP Service Extension for Secure SMTP over Transport Layer Security (RFC 3207) i opportunistisk modus brukast. Det er også anbefalt at «SMTP TLS Reporting» (RFC 8460) vert brukt.

Dette gjeld e-post utveksling som går over Internett (SMTP), og ikkje anna meldingsutveksling som skal gå føre seg ved hjelp av løysing for utveksling av meldingar mellom offentlege verksemder.

**Krav til bruk av standardar**

RFC 7672 – SMTP Security via Opportunistic DNS-Based Authentication of Named Entities (DANE) Transport Layer Security (TLS)

RFC 7671 – The DNS-Based Authentication of Named Entities (DANE) Protocol: Updates and Operational Guidance

RFC 3207 – SMTP Service Extension for Secure SMTP over Transport Layer Security

RFC 8460 – SMTP TLS Reporting

RFC 8446 – The Transport Layer Security (TLS) Protocol – Version 1.3 (August 2018)

RFC 5246 – The Transport Layer Security (TLS) Protocol Version 1.2

Desse standardane vert reviderte enkeltvis av IETF og Digitaliseringsdirektoratet vil oppdatere anbefalinga med gjeldande versjon av kvar standard når dette skjer. Dersom ein revisjon fører til større endringar vil Digitaliseringsdirektoratet vurdere behovet for å revidere heile anbefalinga. Revisjonar som fører til større endringar vil verte behandla av Standardiseringsrådet.

Anbefalte standardar for å motverke falske avsendarar av e-post

Anbefalinga for å motverke falske avsendarar av e-post vart innført 01.11.2018.

Det er anbefalt å nytte Domain-based Message Authentication, Reporting, and Conformance (DMARC) (RFC 7489) og minst ein av de underliggande standardane Sender Policy Framework (SPF) (RFC 7208) og Domain Keys Identified Mail (DKIM) (RFC 6376) for å sikre utveksling av e-post mellom e-post servarar, både ved sending av e-post til offentlege verksemder og ved sending av e-post til innbyggarar og næringsliv.

Det er anbefalt at ein for domene som ikkje vert nytta til sending av e-post bruker Sender Policy Framework (SPF) for å angi at det ikkje vert sendt e-post frå domenet.

Dette gjeld e-post utveksling som går over Internett (SMTP), og ikkje anna meldingsutveksling som skal gå føre seg ved hjelp av løysing for utveksling av meldingar mellom offentlege verksemder.

**Krav til bruk av standardar**

- RFC 7489 – Domain-based Message Authentication, Reporting, and Conformance (DMARC)
- RFC 7208 – Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1
- RFC 7372 – Email Authentication Status Codes
- RFC 6376 – DomainKeys Identified Mail (DKIM) Signatures
- RFC 6377 – DomainKeys Identified Mail (DKIM) and Mailing Lists

Desse standardane vert reviderte enkeltvis av IETF og Digitaliseringsdirektoratet vil oppdatere anbefalinga med gjeldande versjon av kvar standard når dette skjer. Dersom ein revisjon fører til større endringar vil Digitaliseringsdirektoratet vurdere behovet for å revidere heile anbefalinga. Revisjonar som fører til større endringar vil verte behandla av Standardiseringsrådet.

Anbefalinga om Dual stack IPv4 og IPv6 vart innført 30.10.2012.

IPv4 og IPv6 er grunnleggande protokollar for kommunikasjon på internett. Alt IT-utstyr som det offentlege anskaffar bør ha støtte for IPv4 og IPv6. Dette gjeld både programvare og maskinvare.  
"Forskrift om IT-standarder i offentlig sektor", har ein ny paragraf som beskriver dette som et krav fra oktober 2021.

***§ 11 Obligatoriske grunnleggende nettverksstandarder***

*Det er obligatorisk for offentlige virksomheter å sette krav til støtte av både IPv4 og IPv6 i alt nytt nettverksutstyr og all IP-avhengig programvare som kjøpes.*

*Det er obligatorisk for offentlige virksomheter å gjøre alle nye og eksisterende, eksternt publiserte tjenester tilgjengelig både på IPv4 og IPv6, med unntak av peer-to-peer-kommunikasjon mellom offentlige virksomheter, der man kan legge over på best egnet tidspunkt.*

*Alle interne klienter i offentlige virksomheter skal ha tilsvarende tilgang til eksterne tjenester publisert på IPv4 og Ipv6.*

*Nye interne nett og løsninger i offentlige virksomheter skal ha støtte for IPv6, det er tillatt å støtte IPv4 i tillegg.*

Offentlege kommunikasjonstenester bør ha støtte for FTP som er ein protokoll for filoverføring. Den er i utstrakt bruk, men har avgrensingar når det gjeld sikkerheit.  
Kravet betyr berre at verksemda di skal ha ei moglegheit til å ta imot filer ved hjelp av FTP. De må ikkje bruke FTP, men kan velje andre overføringsmetodar for batch-filer viss de ønsker/har behov for dette. FTP bør brukast over ein sikker kommunikasjonskanal.

### Protokollar for å styre trafikken i nettverk basert på IP

Alle offentlege kommunikasjonstenester bør ha støtte for TCP (Transmission Control Protocol). Dette er ein grunnleggande protokoll for å styre trafikken i nettverk basert på IP. Som for IP finst det også tilhøyrande protokollar til TCP. Det er viktig at desse protokollane vert sett på som ein heilskap.

Alle offentlege kommunikasjonstenester bør ha støtte for UDP (User Datagram Protocol). Dette er også ein grunnleggande protokoll for å styre trafikken i nettverk basert på IP. Som for IP finst det også tilhøyrande protokollar til UDP. Det er viktig at desse protokollane vert sett på som ein heilskap.

## Heimel

Krava er gjeldande.

## Rettleiar

Nettstader som vert brukte av verksemder i offentleg sektor bør etablere ei teknisk løysing som bruker HTTP over TLS (HTTPS) for alle deler av nettstaden.

Digitaliseringsdirektoratet anbefaler at NSMs rettleiar «HTTP over TLS» (sjå nedst på sida) vert følgt så langt det er føremålstenleg og ikkje i konflikt med anna regelverk, for å ta vare på sikker implementasjon og vurdering av kompenserande tiltak for kjende sårbarheiter.

Det er viktig at nettstadene vert sette opp korrekt, og det vert vist til rettleiing frå Nasjonal sikkerheitsmyndigheit (NSM).

**IT-rettleiing for ugraderte system nr. 15 (U-15)**

Nasjonal sikkerheitsmyndigheit (NSM) har utarbeidd ei rettleiing for å etablere HTTP over TLS (HTTPS):  
«Hypertext Transport Protocol Secure – Hvordan autentisere nettsteder og konfidensialitets- og integritetsbeskytte webtrafikk»  
(Sjå nedst på denne sida)

**IT-rettleiing for ugraderte system nr. 14 (U14)**

Nasjonal sikkerheitsmyndigheit (NSM) har utarbeidd ei rettleiing for grunnleggande tiltak for sikring av kommunikasjon over usikre nett ved hjelp av TLS.

Rettleiarane vert forvalta av Nasjonal sikkerheitsmyndigheit og gir ei sikkerheitsfagleg vurdering av korleis HTTPS bør implementerast og korleis kommunikasjon kan sikrast med TLS. For at kommunikasjonen skal sikrast i nødvendig og tilstrekkeleg grad, er det viktig at standardane vert implementerte korrekt. Rettleiarane NSM forvaltar handlar om implementasjon av HTTP over TLS (HTTPS).

**IT-rettleiing for ugraderte system nr. 02 (U-02)**

Nasjonal sikkerheitsmyndigheit (NSM) har utarbeidd ei rettleiing for grunnleggande tiltak for sikring av overføring av e-post mellom e-posttenarar. Denne rettleiaren dekkjer standardane for STARTTLS, DMARC, SPF og DKIM.

- [TCP (Transmission control protocol)](https://www.digdir.no/standarder/tcp-transmission-control-protocol/1732)
- [FTP (File transfer protocol)](https://www.digdir.no/standarder/ftp-file-transfer-protocol/1685)

- [NSMs rettleiar "HTTP over TLS"](https://nsm.no/getfile.php/133705-1592914512/Demo/Dokumenter/https.pdf)
- [NSMs rettleiar for sikring av kommunikasjon med TLS](https://nsm.no/getfile.php/133702-1592914245/Demo/Dokumenter/tls.pdf)
- [Sikrare norske domenenamn med DNSSEC](https://www.norid.no/no/om-domenenavn/veiledere/sikrere-norske-domenenavn-med-dnssec/)
- [Secure Domain Name System (DNS) Deployment Guide, NIST Special Publication800-81-2](https://dx.doi.org/10.6028/NIST.SP.800-81-2)
- [IPv4, IPv6, FTP og andre nettverksprotokollar (Wikipedia)](https://no.wikipedia.org/wiki/IPv4)
- [HTTP 1.1](https://tools.ietf.org/html/rfc7230)
- [HTTP Over TLS](https://tools.ietf.org/html/rfc2818)
- [Transport Layer Security (TLS)](https://tools.ietf.org/html/rfc5246)
- [SMTP Service Extension](https://tools.ietf.org/html/rfc3207)
- [TLS Extensions: Extension Definitions](https://tools.ietf.org/html/rfc6066)
- [HTTP Strict Transport Security (HSTS)](https://tools.ietf.org/html/rfc6797)
- [Online Certificate Status Protocol – OCSP](https://tools.ietf.org/html/rfc6960)
- [Public Key Pinning Extension for HTTP](https://tools.ietf.org/html/rfc7469)
- [UDP (User Datagram Protocol)](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
- [Grunnleggande tiltak for sikring av epost](https://nsm.no/getfile.php/133663-1592828388/Demo/Dokumenter/u-02-grunnleggende-tiltak-for-sikring-av-e-post---endelig.pdf)
