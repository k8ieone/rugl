# Dva modely
## ISO/OSI
 * Application
 * Presentation
 * Session
 * Transport
 * Network
 * Datalink
 * Physical

## TCP/IP
 * Application
 * Transport
 * Internet
 * Network access layer

TCP je zjednodušené - **Application**, **Presentation** a **Session** (ISO) je sloučeno do **Application** (TCP). **Datalink** a **Physical** (ISO) je sloučen do **Network Access Layer** (TCP).
OSI se používá většinou teoreticky. TCP se používá v praxi.

# Dva hlavní protokoly vrstvy Internet
 * IP
 * ICMP

## IP
 * IP protokol rozdělí data na packety.
 * PDU = protocol data unit.
 * Bezstavový protokol.
 * IP protokol je "best effort" protokol, není prováděna zpětná kontrola zda packet dorazil.
 * Verze 4 a 6.

## ICMP
 * Základní protokol pro zpětnou vazbu.
 * Verze 4 a 6.
 * Příkladem je *ping*.
# Dva hlavní protokoly vrstvy Transport
 * TCP
 * UDP
## TCP
 * Stavový protokol.
 * Probíhá zpětná kontrola zda packety dorazily.
 * PDU je **segment**.
 * Segmenty se seřadí do správného pořadí.

## UDP
 * Bezestavový.
 * Nemá korekci chyb.
 * Nenavazuje a neukončuje připojení.
 * Předpokládá, že oprava bude provedena ve vyšší vrstvě.
 * Je mnohem rychlejší, nižší *overhead*.

# Jak to funguje?
IP hlavička/Data - **packet** 
TCP hlavička/IP hlavička/Data - **segment**

# Network access layer
 * PDU = *frame*
 * Header/Data/Trailer - **frame**
 * V položce *Data* se nachází všechno z předchozích vrstev.
 * Header obsahuje *source* a *destination* MAC.
 * MAC má formát DE:AD:BE:EF:00:00 (AB:CD:EF:AB:CD:EF).
 * První tři jsou *vendor*, další tři jsou unikátní pro každé zařízení.
