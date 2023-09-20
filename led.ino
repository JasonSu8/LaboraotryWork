// step 1
int ledPin = 1;
char key;
int ONdelayTime = 500;
int OFFdelayTime = 500;
int i;

// step 2
void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

// step 3
void loop() {
  if(Serial.available() > 0) {
    key = Serial.read();
    delay(1);
    if(key == '1') {
      for(i = 0; i < 6; i++) {
        digitalWrite(ledPin,HIGH);
        delay(ONdelayTime);        
        digitalWrite(ledPin,LOW);
        delay(OFFdelayTime);
      }
    }
  }       
}
