# Instalace Windows?
## Pojmy OS
 * *Multi-user* - Dva nebo více uživatelů je schopno pracovat s programy a periferiemi.
 * *Multitasking* - Může běžět více než jedna aktualizace
 * *Multiprocessing* - OS podporuje více než jeden fyzický procesor.
 * *Multithreading* - Program může být rozdělen na menší části. Umožňuje nekolika částem programu běžet zároveň.

## Základní funkce OS:
 * Kontrola přístupu k hardwaru - Instalace a načítání správných ovladačů.
 * Správa souborů a složek
 * Poskytnutí uživatelského rozhraní - Příkazový řádek nebo grafické rozhraní.
 * Správa aplikací

## Migrace dat:
 * Při instalaci OS je třeba se ujistit že uživatelská data budou přesunuta do nového OS
 * *User State Migration Tool* - Nástroj pro přesun uživatelských dat of Microsoftu.
 * *Windows Easy Transfer* - Umožňuje přesun dat z Windows Vista/7/8 do Windows 8.1
 * *PCmover Express* - Program vyvýjený v partnerství MS a Laplink. Nahrazue *WET*.

## Dělení HDD:
 * Dva hlavní *Schémata Dělení*:
   * MBR
     * Maximálně 4 primární oddíly
     * Maximální velikost oddílu 2TB
     * Nelze zálohovat *tabulku oddílů*
     * Informace o oddílech a bootloader jsou na jednom místě
     * Používá se u staršich počítačů
   * GPT
     * Maximálně 128 oddílů (Windows)
     * Maximální velikost oddílu 9,4ZB
     * Ukládá zálohu *tabulky oddílů*
     * Data o oddílech a booloader jsou na několika místech na disku
     * Počítač musí podporovat UEFI a mít 64-bitový OS

## Pojmy dělení disků:
 * Primární oddíl - Obsahuje OS a systémové soubory. U GPT jsou pouze primární oddíly.
 * Aktivní oddíl - Obsahuje OS. Pouze primární oddíl může být označen jako aktivní. U MBR lze označit jen jeden oddíl jako aktivní.
 * Rozšřený oddíl - Pouze u MBR, jeden z primárních oddílů lze označit jako *extended* a pak je možno vytvořit až 23 logických oddlů.
 * *Basic disk*
 * *Dynamic disk* - Lze vytvřit oddíl přes několik fyzických disků, také je možno libovolně měnit velikost oddílů nezávisle na tom zda jsou *vedle sebe*
 * Formátování - Vytvoření systému souborů.
