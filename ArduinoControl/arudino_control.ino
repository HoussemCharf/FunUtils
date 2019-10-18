
#define RELAY1  7
void setup()

{

  Serial.begin(9600);
  pinMode(RELAY1, OUTPUT);

}

void loop()

{

  if (Serial.available()) {
    char serialListener = Serial.read();
    Serial.println(serialListener);
    if (serialListener == '0') {
      digitalWrite(RELAY1, 0);
      Serial.println("Light OFF");
    }
    else if (serialListener == '1') {
      digitalWrite(RELAY1, 1);
      Serial.println("Light ON");
    }
  }


}