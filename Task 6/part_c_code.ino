// PART-C: Arduino Code for Servo Switching
// Controls two servos using a pushbutton and potentiometer, displays status on LCD

#include <Servo.h>        // Library for controlling servos
#include <LiquidCrystal.h> // Library for the LCD

Servo servoA;  // Create object for Servo A
Servo servoB;  // Create object for Servo B

const int potPin = A0;     // Potentiometer connected to analog pin A0
const int buttonPin = 2;   // Pushbutton connected to digital pin 2

int activeServo = 0;       // 0 = Servo A active, 1 = Servo B active
int lastButtonState = HIGH; // Stores previous button state to detect new presses

// Initialize LCD with pins: RS=7, E=8, D4=9, D5=10, D6=11, D7=12
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
  servoA.attach(3);        // Attach Servo A to pin 3
  servoB.attach(5);        // Attach Servo B to pin 5

  pinMode(buttonPin, INPUT_PULLUP); // Set button pin as input with pull-up resistor
  lcd.begin(16, 2);        // Initialize LCD (16 characters, 2 rows)
  lcd.print("StepXplorer Ready"); // Show welcome message
  delay(1000);             // Wait 1 second
  lcd.clear();             // Clear the LCD
}

void loop() {
  // Read the button state (LOW when pressed, HIGH when not pressed)
  int buttonState = digitalRead(buttonPin);

  // Check for a new button press (LOW now, was HIGH before)
  if (buttonState == LOW && lastButtonState == HIGH) {
    activeServo = 1 - activeServo; // Toggle between Servo A (0) and Servo B (1)
    delay(300);                   // Debounce delay to avoid multiple triggers
  }
  lastButtonState = buttonState;  // Update last button state

  // Read potentiometer value (0-1023) and map to servo angle (0-180)
  int potValue = analogRead(potPin);
  int angle = map(potValue, 0, 1023, 0, 180);

  // Move the active servo to the calculated angle
  if (activeServo == 0) {
    servoA.write(angle);  // Move Servo A
  } else {
    servoB.write(angle);  // Move Servo B
  }

  // Update LCD display
  lcd.setCursor(0, 0);      // Move to top row, first column
  lcd.print("Servo: ");
  lcd.print(activeServo == 0 ? "A " : "B "); // Show active servo (A or B)

  lcd.setCursor(0, 1);      // Move to bottom row, first column
  lcd.print("Angle: ");
  lcd.print(angle);         // Show the angle
  lcd.print("   ");         // Clear leftover digits for clean display
}