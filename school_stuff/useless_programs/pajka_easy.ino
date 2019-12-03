//Vypadá to, že jsi to vzdal...
//To je v pohodě, můžeš si vypůjčit můj kód...
//Prosím snaž se kód upravir aby nebylo poznat, že je to jenom zkopírované
//Například uprav kolik tlačítka ubírají a přidávají
//Toto nastavení najdeš kousek pod tímto komentářem, je označeno komentářem "tlačítka"
//To samé jde aplikovat na LED diody
//Také třeba uprav tóny a délky tónů.
//Nebo zprávu, která je vypsána do sériové konzole
//Taky prosím o smazání všech (nebo alespoň většiny) komentářů
//Děkuji

#include <EEPROM.h>

#define pinLatch 4
#define pinClk 7
#define pinData 8
byte cislice=3;

//ledky
const int led1 = 10; // topné těleso
const int led2 = 11; // zepnuto/vypnuto
const int led3 = 12; // připraveno k použití
const int led4 = 13;

//tlačítka
const int but1=A3; // -button
const int but2=A2; // +button
const int but3=A1; // on/off

byte teplotaNastavena;

void setup() {
  pinMode(pinLatch, OUTPUT);
  pinMode(pinClk, OUTPUT);
  pinMode(pinData, OUTPUT);
  
  pinMode(3, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(but1, INPUT_PULLUP);
  pinMode(but2, INPUT_PULLUP);
  pinMode(but3, INPUT_PULLUP);

  Serial.begin(9600);
  digitalWrite(led3, HIGH);
  digitalWrite(led4, HIGH);

  //Načíst hodnotu z EEPROM
  if (EEPROM.read(100) == 1){
    teplotaNastavena = 100;
  }
  else {
    teplotaNastavena = EEPROM.read(100);
  }
  //Tón při zapnutí
  tone(3, 6000, 150);
  delay(150);
  tone(3, 7500, 50);
  }

void loop() {
  byte teplotaAktualni = 255 - analogRead(A4)/4;
  
  //Tady píšeme do sériové konzole
  Serial.print("Aktuální teplota: "); // PLEASE CHANGE THIS
  Serial.print(teplotaAktualni);
  Serial.print("\n");
  Serial.print("Nastavená teplota: "); // PLEASE CHANGE THIS
  Serial.print(teplotaNastavena);
  Serial.print("\n");
  
  //Tady zobrazujeme na displeji
  zapisCisloNaSegment(teplotaAktualni);
  
  //Tady kontrolujeme aktuální a nastavenou teplotu
  if (digitalRead(led2) == 0){
    if (teplotaAktualni < teplotaNastavena){
      digitalWrite(led1, LOW);
      digitalWrite(led3, LOW);
    }
    else if (teplotaAktualni > teplotaNastavena){
      digitalWrite(led1, HIGH);
    }
  }
  else if (digitalRead(led2) == 1){
    digitalWrite(led1, HIGH);
  }

  // Tlačítka
  if (digitalRead(but1) == 0){
    teplotaNastavena -= 5;
    EEPROM.write(100, teplotaNastavena);
  }
  else if (digitalRead(but2) == 0){
    teplotaNastavena += 10;
    EEPROM.write(100, teplotaNastavena);
  }
  else if (digitalRead(but3) == 0 and digitalRead(led2) == 0){
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH);
    delay(150);
  }
  else if (digitalRead(but3) == 0 and digitalRead(led2) == 1){
    digitalWrite(led2, LOW);
    delay(150);
}
}

//Magie pro displej
void zapisCisloNaSegment(int hodnota) {
const byte mapaSegment[] = {0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0X80,0X90};
 switch (cislice--) {

 case 1:
 digitalWrite(pinLatch,LOW);
shiftOut(pinData, pinClk, MSBFIRST, mapaSegment[hodnota/ 1000]);
shiftOut(pinData, pinClk, MSBFIRST, 0xF1 );
digitalWrite(pinLatch,HIGH);
break;
 case 2:
digitalWrite(pinLatch,LOW);
shiftOut(pinData, pinClk, MSBFIRST, mapaSegment[((hodnota / 100) % 10)]);
shiftOut(pinData, pinClk, MSBFIRST, 0xF2 );
digitalWrite(pinLatch,HIGH);
 break;
 case 3:
 digitalWrite(pinLatch,LOW);
shiftOut(pinData, pinClk, MSBFIRST, mapaSegment[(hodnota / 10) % 10]);
shiftOut(pinData, pinClk, MSBFIRST, 0xF4 );
digitalWrite(pinLatch,HIGH);
 break;
 default:
 digitalWrite(pinLatch,LOW);
shiftOut(pinData, pinClk, MSBFIRST, mapaSegment[hodnota % 10]);
shiftOut(pinData, pinClk, MSBFIRST, 0xF8 );
digitalWrite(pinLatch,HIGH);
 cislice=3;
 }
}
