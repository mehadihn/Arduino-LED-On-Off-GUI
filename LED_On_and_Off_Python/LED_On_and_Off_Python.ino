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
      int a = 1+1;
      Serial.print("LED On\n");
      Serial.println(a);
    }

    else if(inBytes == "off"){
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("LED Off12112");
      int a = 2 + 2;
      // String b = String(a);
      Serial.println(a);
    }

    else{
      Serial.write("Invalid Input Provided\n");
    }
  }
}
