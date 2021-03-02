int analogVal1 = 0;
int analogVal2 = 0;
void setup() {
  Serial.begin(9600);

}

void loop() {
  analogVal1 = analogRead(A0);
  analogVal2 = analogRead(A1);
  Serial.print(analogVal1);
  Serial.print(" , ");
  Serial.println(analogVal2);
  delay(1000);
}
