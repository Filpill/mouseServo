#include <Servo.h>

//For reading characters in

const byte numChars = 32;
char receivedChars[numChars];

boolean newData = false;

//Inititalise Servo
Servo yawServo;
Servo pitchServo;

//Define variables for incoming COM Port Data
long tmr;
int flag = 0;
int angle = 0;
String servo_input;
int yaw;
int pitch;
int yaw_angle;
int pitch_angle;
char  c;

void setup() {

  //Inialise Servo Data Pins
  yawServo.attach(3);
  pitchServo.attach(9);

  //Initialise Bluetooth Serial communication + Serial Interupt Signal
  Serial.begin(9600);
  delay(100);
}

void loop() {
  
  //Read Strings into Arduino
    recvWithStartEndMarkers();
    showNewData();
    
     //Convert Character Array to String Object
    String servo_input = receivedChars;
      
    //Extract Control Components
    yaw = servo_input.substring(0, 3).toInt();
    pitch = servo_input.substring(3,7).toInt();

    //Print data to Serial Monitor
    Serial.print("Servo Input:  ");
    Serial.print(receivedChars);
    Serial.print("  Yaw  :  ");   
    Serial.print(yaw);
    Serial.print("  Pitch  :  ");
    Serial.println(pitch);

    //Calling Steer and MotorControl Functions
    yawSteer(yaw);
    pitchSteer(pitch);

  }

void yawSteer(int servo_data){
  //Send Steering Data to Servo
  angle = map(servo_data, 0, 255, 0, 180);
  yawServo.write(angle);
}

void pitchSteer(int servo_data){
  //Send Steering Data to Servo
  angle = map(servo_data, 0, 255, 0, 180);
  pitchServo.write(angle);
}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }
        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void showNewData() {
    if (newData == true ){
        newData = false;
    }
}
