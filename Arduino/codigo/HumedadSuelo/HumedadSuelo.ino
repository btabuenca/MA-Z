#define HUMEDADSUELO 36;

int value;

void setup()
{
  Serial.begin(9600);
  Serial.println("Reading");
  delay(2000);
}

void loop()
{

  value = analogRead(HUMEDADSUELO);
  value = map(value,550,0,0,100);
  Serial.print("Moisture : ");
  Serial.print(value);
  Serial.println("%");
  delay(1000);
}

int leerHumedadSuelo(){
  value = analogRead(HUMEDADSUELO);
  value = map(value,550,0,0,100);
  return value;
}
