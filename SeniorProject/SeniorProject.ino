int in1 = 5;
int in2 = 6;
int ena = 8;  // Enable A for PWM control
int s0 = 0;
int s1 = 0;

void setup() {
  Serial.begin(9600); // Start serial communication
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(ena, OUTPUT);
}

void loop() {
  s0 = analogRead(A0); // Read analog input
  s1 = analogRead(A1); // Read analog input
  Serial.println(s0); // Print value (0-1023)
  Serial.println(s1); // Print value (0-1023)
  // Move motor forward with PWM speed control
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(ena, 150);  // Adjust speed (0-255)

  delay(250);  // Run for 3 seconds

  // Stop motor
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(ena, 0);

  delay(1000);  // Wait for 3 seconds before repeating
}
