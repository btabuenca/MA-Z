#define FUGAS 35;

int value = 0;

void setup() {
  Serial.begin(115200);
  delay(1000);
}

void loop() {
  value = analogRead(FUGAS);

  // Hay que meter un map.
  // value = map(value,550,0,0,100);
  Serial.println(value);
  delay(500);
}
