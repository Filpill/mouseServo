import processing.serial.*;
import controlP5.*;
Serial myPort;
ControlP5 cp5;

//Initialising Global Variables
int yaw = 0;
int pitch = 0;
String angleStatus; 

void setup() {
  
//Inserting Controller Buttons and Sliders

size(500,450);
cp5 = new ControlP5(this);
cp5.addSlider("yaw").setPosition(50,215).  setSize(250, 100). setRange(0,255) .setValue(128);
cp5.addSlider("pitch").setPosition(350,135).  setSize(100, 250). setRange(0,255) .setValue(128);

//Initialising Communication Port
myPort = new Serial(this, "COM3", 9600); // Starts the serial communication at 9600 baud rate
myPort.bufferUntil('\n');// Reading Serial Data up to new line. The character '\n' or 'New Line'
}

void serialEvent (Serial myPort){// Checks for available data in the Serial Port
angleStatus = myPort.readStringUntil('\n');//Reads the data sent from the Arduino
}

void draw (){
  
//Drawing Title and Backround of Controller
  background(26, 82, 30);
  fill(58,107,61);
  rect(10,30,475,50);
  fill(0);
  textSize(28);
  text("USB Mouse - Servo Controller",80,65);
  
  //String needs to be defined inside the draw function to keep updating strings
  //-----Control Parameters-----//
  String servo_inputs = '<'+ nf(yaw,3) + nf(pitch,3) + '>';
  println(servo_inputs);
  myPort.write(servo_inputs); delay(100);
  
}
