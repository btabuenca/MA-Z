#define VALVULA 2;

void setup() {
  pinMode(VALVULA,OUTPUT);
}

void loop() {
  delay(500);
  activarValvula();
  delay(500);
  desactivarValvula();
}

void activarValvula(){
  digitalWrite(VALVULA, HIGH);
}

void desactivarValvula(){
  digitalWrite(VALVULA, LOW);
}
