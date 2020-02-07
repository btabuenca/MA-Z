#define VALVULA 2
#define FUGAS 35
#define PESO 36
#define HUMEDADSUELO 37

float valuePeso = 0;
int valueFugas = 0;
int valueHumedad = 0;

void setup() {
  pinMode(VALVULA,OUTPUT);
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  valuePeso = analogRead(PESO);
  valueFugas = analogRead(FUGAS);
  valueHumedad = analogRead(HUMEDADSUELO);
  valueHumedad = map(valueHumedad,4095,0,0,100);
  valuePeso = map(valuePeso,256.00,4095.00,0.00,23.63);
  valuePeso = valuePeso / 2.205;
  Serial.print("Moisture : ");
  Serial.print(valueHumedad);
  Serial.print("%");
  Serial.print(" Peso : ");
  Serial.print(valuePeso);
  Serial.print("Kg");
  Serial.print(" Fugas : ");
  Serial.println(valueFugas);

  delay(1000);
}
