const int led1=13;
const int led2=12;
const int led3=11;
const int led4=10;
const int but1=A1;
const int but2=A2;
const int but3=A3;
char var;

void setup() {
  // put your setup code here, to run once:
  pinMode(3, OUTPUT);
  tone(3, 750, 250);
  tone(3, 1000, 200);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(but1, INPUT_PULLUP);
  pinMode(but2, INPUT_PULLUP);
  pinMode(but3, INPUT_PULLUP);
  Serial.begin(9600);
  Serial.print(but1);
}

void loop() {
  if (Serial.available()>0){
    var=Serial.read();
    Serial.print(var);
    //start_function(var);
  }
  
  else if (digitalRead(but1)==0){
    Serial.println("Started led_effect_1");
    led_effect_1();
    Serial.println("Finished led_effect_1");
    }
  else if (digitalRead(but2)==0){
    Serial.println("Started cricket");
    cricket();
    Serial.println("Finished cricket");
  }
  else if (digitalRead(but3)==0){
    Serial.println("Started led_effect_2");
    led_effect_2();
    Serial.println("Finished led_effect_2");
  }
  else {
    delay(50);
    //Serial.println(millis());
    }
}

void led_effect_1(){
  digitalWrite(led1, LOW);
  delay(1);
  digitalWrite(led1, HIGH);
  digitalWrite(led2, LOW);
  delay(1);
  digitalWrite(led2, HIGH);
  digitalWrite(led3, LOW);
  delay(1);
  digitalWrite(led3, HIGH);
  digitalWrite(led4, LOW);
  delay(1);
  digitalWrite(led4, HIGH);
}

void cricket(){
  tone(3, 50, 10);
  tone(3, 150, 10);
  tone(3, 100, 10);
}

void led_effect_2(){
  digitalWrite(led3, LOW);
  delay(150);
  digitalWrite(led2, LOW);
  delay(150);
  digitalWrite(led4, LOW);
  delay(150);
  digitalWrite(led1, LOW);
  delay(150);

  digitalWrite(led3, HIGH);
  delay(150);
  digitalWrite(led2, HIGH);
  delay(150);
  digitalWrite(led4, HIGH);
  delay(150);
  digitalWrite(led1, HIGH);
  delay(150);
}

void start_function(char var){
  if (var == "led_effect_1"){
    led_effect_1();
  }
  else if (var == "led_effect_2"){
    led_effect_2();
  }
  else if (var == "cricket"){
    cricket();
  }
}
