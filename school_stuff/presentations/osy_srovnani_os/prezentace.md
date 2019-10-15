---
marp: true
---

<!-- class: invert -->
<!-- theme: uncover -->

# Srovnání Linuxových distribucí
 * Linuxové distribuce se funkcionalitou neliší
 * Liší se pouze filozofii aktualizací softwaru a operačního systému, dobou podpory, způsobem podpory a volbou výchozího softwaru

---

#  Ubuntu Desktop
 * Uživatelské prostředí: GNOME3
 * Systém souborů: ext4
 * Správce balíčků: APT (frontend pro dpkg)
 * Init systém: systemd
 * Cyklus vydání nové verze: 6 měsíců, 2 roky (LTS)
 * Délka podpory a bezpečnostních aktualizací: 9 měsíců, 5 let (LTS)
 
---

# Debian
 * Uživatelské prostředí: GNOME3, KDE, Xfce, LXDE (možnost výběru)
 * Systém souborů: ext4
 * Správce balíčků: APT (frontend pro dpkg)
 * Init systém: systemd
 * Cyklus vydání nové verze: 2 roky
 * Délka podpory a bezpečnostních aktualizací: 1 rok po vydání nové stabilní verze

---
 # Fedora
 * Uživatelské prostředí: GNOME3
 * Systém souborů: ext4, xfs (kombinace)
 * Správce balíčků: DNF a RPM
 * Init systém: systemd
 * Cyklus vydání nové verze: 6 měsíců (+rolling)
 * Délka podpory a bezpečnostních aktualizací: 13 měsíců (verze X je podporována 1 měsíc potom co je vydána verze X+2)

---

# CentOS
 * Uživatelské prostředí: GNOME3
 * Systém souborů: xfs
 * Správce balíčků: Yum
 * Init systém: systemd
 * Cyklus vydání nové verze: 3-5 let
 * Délka podpory a bezpečnostních aktualizací: do 10 let

---

 # openSUSE
 * Uživatelské prostředí: KDE, GNOME3, Xfce (možnost výběru)
 * Systém souborů: btrfs
 * Správce balíčků: ZYpp (založeno na RPM)
 * Init systém: systemd
 * Cyklus vydání nové verze: 2-4 roky (+rolling)
 * Délka podpory a bezpečnostních aktualizací: 3 roky

 ---

# Arch Linux
 * Uživatelské prostředí: žádné (možnost doinstalovat jakékoli)
 * Systém souborů: jakýkoli podporovaný (ext4, ZFS, btrfs, xfs, ReiserFS, ...)
 * Správce balíčků: pacman
 * Init systém: systemd
 * Cyklus vydání nové verze: rolling

 ---

 # Gentoo
 * Uživatelské prostředí: žádné (záleží na uživateli)
 * Systém souborů: jakýkoli podporovaný (stejné, jako Arch Linux)
 * Správce balíčků: portage
 * Init systém: openrc
 * Cyklus vydání nové verze: rolling

---

# Názor na budoucnost

---

## Windows:
 * Windows 10 je poslední vydanou verzí Windows
 * Bude pokračovat stálými aktualizacemi (rolling release)
 * Možná bude přejmenován na "Windows"
 * Strategie software-as-a-service
 * Postupně bude ukončena podpora WIN32 aplikací

---

## GNU/Linux:
 * Již je nejpoužívanějším OS pro servery
 * Bude se rozšiřovat do IOT zařízení
 * I do uživatelských počítačů, kvůli ukončení podpory WIN32 a stálým "vylepšením" od Microsoftu