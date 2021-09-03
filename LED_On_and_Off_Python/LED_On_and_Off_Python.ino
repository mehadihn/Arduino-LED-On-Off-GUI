int x = 1;
String inBytes;
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(2);
  pinMode(LED_BUILTIN,OUTPUT);
}

void loop() {
  if(Serial.available()>0){
    inBytes = Serial.readStringUntil('\n');
    if(inBytes == "on"){
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.write("LED On\n");
    }

    else if(inBytes == "off"){
      digitalWrite(LED_BUILTIN, LOW);
      Serial.write("LED Off\n");
    }

    else{
      Serial.write("Invalid Input Provided\n");
    }
  }
}
