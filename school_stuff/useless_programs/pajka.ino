#include <EEPROM.h>

#define pinLatch 4
#define pinClk 7
#define pinData 8
byte cislice=3;
// Above is the display magic

//leds
const int led1 = 13; // heating is on
const int led2 = 12; // if the heating logic is active
const int led3 = 11;
const int led4 = 10;

//buttons
const int but1=A1; // -button
const int but2=A2; // +button
const int but3=A3; // toggle

//other variables
byte temperature_target;

void setup() {
  pinMode(3, OUTPUT);
  pinMode(pinLatch, OUTPUT);
  pinMode(pinClk, OUTPUT);
  pinMode(pinData, OUTPUT);
  // More magic above
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
  if (EEPROM.read(100) == 1){
    temperature_target = 100;
  }
  else {
    temperature_target = EEPROM.read(100);
  }
  tone(3, 750, 100);
  delay(100);
  tone(3, 1000, 50);
}

void loop() {
  byte temperature_current = 255 - analogRead(A4)/4;
  
  // Printing the temperatures to the serial console
  Serial.print("Current temperature is: ");
  Serial.println(temperature_current);
  Serial.print("Target temperature is: ");
  Serial.println(temperature_target);
  
  // Display current temperature on the display
  display_something(temperature_current);
  
  // Check if the heating should be on (compare target and current temperature)
  if (digitalRead(led2) == 0){
    if (temperature_current < temperature_target){
      digitalWrite(led1, LOW);
      digitalWrite(led3, LOW);
    }
    else if (temperature_current > temperature_target){
      digitalWrite(led1, HIGH);
    }
  }
  else if (digitalRead(led2) == 1){
    digitalWrite(led1, HIGH);
  }

  // Buttons and their logic
  //-Button
  if (digitalRead(but1) == 0){
    temperature_target -= 5;
    EEPROM.write(100, temperature_target);
  }
  //+Button
  else if (digitalRead(but2) == 0){
    temperature_target += 10;
    EEPROM.write(100, temperature_target);
  }
  //ON/OFF button
  else if (digitalRead(but3) == 0 and digitalRead(led2) == 0){
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH);
    delay(150);
    tone(3, 1000, 250);
    delay(250);
    tone(3, 500, 150);
  }
  else if (digitalRead(but3) == 0 and digitalRead(led2) == 1){
    digitalWrite(led2, LOW);
    delay(150);
    tone(3, 500, 250);
    delay(250);
    tone(3, 1000, 150);

  }
}

void display_something(int string){
  int counter = 0;
  while (counter < 1000){
    counter += 1;
    zapisCisloNaSegment(string);
  }
}

//Below is even more display magic
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
// End of display magic
