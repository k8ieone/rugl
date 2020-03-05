---
marp: true
paginate: true
_paginate: false
---

<!-- class: invert -->
<!-- theme: uncover -->

# Mikroprocesory
###### Autor: Rostislav Medvěd
---
## Co to je?
 * Elektronický obvod
 * Vykonává operace s daty v paměti
---
## Typická operace
1. Fetch and Decode - nahrání z paměti
1. Find data
1. Execute
1. Write back
---
## Specifikace
 * Počet jader
 * Počet vláken
 * Frekvence
 * TDP (tepelný výstup)
 * Cache (mezipaměti)
 * ISA (instrukční sada)
   * Popřípadě různá rozšíření ISA
   * Další funkce procesoru
 * Mikroarchitektura (implementace ISA)
---
## Instrukční sady
 * Dělí se na **RISC** a **CISC**
 * Definuje datové typy, registry a další věci
 * Umožňují velké změny designu procesoru
 * V tomto jsou procesory Intel a AMD stejné:

### Zjednodušeně
(X86_64)
`./OnePlusOne`
`=1`

---
### Příklady ISA:
 * CISC (spousty velkých instrukcí):
   * X86
   * X86_64
 * RISC (málo malých instrukcí):
   * ARM
   * RISC-V
   * Power ISA
   * MIPS
 * EPIC:
   * IA-64 (Itanium)
---
## Mikroarchitektury
 * Zde se i různé generace procesorů velice liší
 * Toto způsobuje rozdíly v rychlosti a spotřebě
 * Určuje jakým způsobem dojde procesor k výsledku
#### Nezávisle na mikroarchitektuře

`./OnePlusOne`
`=1`

---
## Příklady mikroarchitektur
 * Pro X86_64:
   * AMD Piledriver Family 15h
   * AMD Zen+
   * AMD Zen 2
   * Intel NetBurst
   * Intel Haswell
   * Intel Skylake
 * Pro IA-64:
   * Merced
   * Kittson
---
# Děkuji za pozornost
```
Kernel panic - not syncing: Attempted to kill init!
```
---
## Zdroje
[Wikipedia - Processor](https://en.wikipedia.org/wiki/Processor_(computing))
[Wikipedia - Processor architecture](https://en.wikipedia.org/wiki/Processor_architecture)
[Wikipedia - ISA](https://en.wikipedia.org/wiki/Instruction_set_architecture)
[Wikipedia - Microarchitecture](https://en.wikipedia.org/wiki/Microarchitecture)
Wikipedia - List of [AMD](https://en.wikipedia.org/wiki/List_of_AMD_CPU_microarchitectures)/[Intel](https://en.wikipedia.org/wiki/List_of_Intel_CPU_microarchitectures) CPU microarchitectures
[Wikipedia - Intel Core (microarchitecture)](https://en.wikipedia.org/wiki/Intel_Core_(microarchitecture))