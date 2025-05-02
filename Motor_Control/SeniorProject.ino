int in1 = 5;
int in2 = 6;
int ena = 8;  // Enable A for PWM control

char command = ' ';

void setup() {
  Serial.begin(9600); // Start serial communication
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(ena, OUTPUT);
}

void loop() {
  // Check if a character has been sent via Serial
  if (Serial.available() > 0) {
    command = Serial.read(); // Read the character
    Serial.print("Received: ");
    Serial.println(command);

    if (command == 'm') {
      // Move motor forward
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      analogWrite(ena, 150);  // Adjust speed (0-255)
      Serial.println("Motor moving...");
    } else if (command == 's') {
      // Stop motor
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW);
      analogWrite(ena, 0);
      Serial.println("Motor stopped.");
    }
  }
}