const int mq135Pin = A0;  // MQ-135 sensor connected to analog pin A0
const int mq9pin = A1;
const int mq2pin = A2;
const int c_button_pin = 9;
const int a_button_pin = 7;

void setup() {
  Serial.begin(9600);     // Start serial communication at 9600 bps
  pinMode(mq135Pin, INPUT);
  pinMode(mq9pin, INPUT);
  pinMode(mq2pin, INPUT);
  pinMode(c_button_pin, INPUT_PULLUP);  
  pinMode(a_button_pin, INPUT_PULLUP);  

}

void loop() {
  int mq135Value = analogRead(mq135Pin);  // Read the analog value from the sensor
  int mq9Value = analogRead(mq9pin);
  int mq2Value = analogRead(mq2pin);

  // Print raw sensor value
  Serial.print(mq135Value);
  Serial.print(" ");
  Serial.print(mq2Value);
  Serial.print(" ");
  Serial.print(mq9Value);
  Serial.print(" ");
  if (digitalRead(c_button_pin) == LOW) {
    Serial.print("1 ");
  }else{
    Serial.print("0 ");
  }
  if (digitalRead(a_button_pin) == LOW) {
    Serial.print("1 ");
  }else{
    Serial.print("0 ");
  }
  Serial.println("");



  delay(200);  // Wait for 1 second before next reading
}