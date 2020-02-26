BitLocker - Jak funguje s TPM, chyba v BL, jak ověřit zda opravdu šifruje

# IPv6
## Základy IPv6
### IPv6 prefix
 * Pomocí prefixu se identifikuje síť
 * Ekvivalentem v IPv4 je 192.168.1.x
   * 192.168.1 identifikuje síť
   * x identifikuje počítače
 * Délka prefixu se může měnit
 * Každá čtveřice čísel je 8 bitů
 * Například `1111:2222:3333:4444::/64` říká že prvních 64 bitů je použito jako prefix

### Zkrácená podoba
 * Víme, že IPv6 adresa má 8 čtveřic (128b)
 * Když vidíme několik nulových čtveřic za sebou, můžeme je zkrátit takto `2041:0000:140F:0000:0000:0000:875B:131B` -> `2041:0000:140F::875B:131B`
   * Toto zkrácení lze provést pouze jednou
 * Pokud se najde čtveřice, která má jakýkoli počet nul a potom číslo, lze ji napsat jen jako číslo `0007` -> `7`
   * Toto funguje i pro další nulové čtveřice: `0000` -> `0`

# Intrusion Detection/Protection System
## IDS
 * Program, nebo zařízení monitorující síť nebo systém.
 * Detekuje podezřelou aktivitu
 * Nahlásí změnu administrátorovi
## IPS
 * Provede i preventivní akci
 * Přkladem je monitorování systémových souborů
   * Pokud je soubor změněn, systém je vypnut a dokud se vše nevrátí do normálního stavu, nejde zapnout

# BitLocker
## TPM
 * TPM je modul pro bezpečnost
 * Je schopný bezpečně generovat šifrovací klíče
## BitLocker s TPM
 * Při přítomnosti TPM je možné povolit kontrolu systémových souborů při startu systému
 * Při použití BitLockeru s TPM jej lze považovat za přklad Intrusion Protection Systému
## Chyba v BitLockeru
 * Některá SSD mají integrovanou podporu pro šifrování (hardwarové šifrování)
 * Některá SSD ale mají docela špatnou implementaci této funkce
 * Některá se dokonce pouze tváří, že takovou funkci mají
 * Výchozí nastavení BitLockeru je použít HW šifrování, pokud je dostupné
 * Při špatné implementaci této funkce je možné, že soubory vůbec nebudou šifrované
 * Proto je potřeba se ujistit, že BitLocker používá vhodnou metodu šifrování  
  
Toto lze učinit následovně:
 1. Spustit CMD
 1. Příkaz `manage-bde -status C:` ukáže stav BL na disku `C`
 1. Pokud výstup příkazu obsahuje slova "Hardware Encryption", je používána metoda šifrování pomocí hardwaru  
  
Pokud nevěříte svému disku, je možné vynutit softwarové šifrování pomocí Skupinové Zásady:
 1. `Win+R`
 1. `gpedit.msc`
 1. Přejít na `Computer Configuration\Administrative Templates\Windows Components\BitLocker Drive Encryption\Fixed Data Drives`
![Screenshot z gpedit](https://www.howtogeek.com/wp-content/uploads/2018/11/img_5be0c37f4bb22.png)
 1. Položku "Configure use of hardware-based encryption for fixed data drives" přepnout na "Disabled"
![asdf](https://www.howtogeek.com/wp-content/uploads/2018/11/img_5be0c3c74ee53.jpg)