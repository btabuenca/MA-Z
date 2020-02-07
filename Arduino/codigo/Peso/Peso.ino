#define PESO 36

int value = 0;

void setup() {
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  value = analogRead(PESO);

  value = map(value,256,4025,0,100);
  value = value / 2,205;
  Serial.println(value);
  delay(500);
}
