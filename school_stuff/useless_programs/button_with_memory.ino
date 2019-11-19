//leds
const int led1 = 13;
const int led2 = 14;
const int led3 = 15;
const int led4 = 16;

//buttons
const int but1=A1;
const int but2=A2;
const int but3=A3;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(but1, INPUT_PULLUP);
}

void loop() {
  if ((digitalRead(but1) == 0) and (digitalRead(led1) == 0)){
    digitalWrite(led1, HIGH);
    delay(100);
  }
  else if ((digitalRead(but1) == 0) and (digitalRead(led1) == 1)){
    digitalWrite(led1, LOW);
    delay(100);
  }
  else{
    delay(100);
  }
}
