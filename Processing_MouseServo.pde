import processing.serial.*;
Serial myPort;

//Initialising Global Variables
int Y_AXIS = 1;
int X_AXIS = 2;
String angleStatus; 
color c1,c2;

void setup() {
  size(500,500);
  c1 = color(204, 102, 0);
  c2 = color(0, 102, 153);
 
//Initialising Communication Port
myPort = new Serial(this, "COM3", 9600); // Starts the serial communication at 9600 baud rate
myPort.bufferUntil('\n');// Reading Serial Data up to new line. The character '\n' or 'New Line'
}

void serialEvent (Serial myPort){// Checks for available data in the Serial Port
angleStatus = myPort.readStringUntil('\n');//Reads the data sent from the Arduino
}

void draw (){
  
//Drawing Title and Background
  setGradient(0, 0, width, height, c1, c2, Y_AXIS);
  fill(207, 157, 19);
  rect(55,25,395,50);
  fill(0);
  textSize(28);
  text("USB Mouse - Servo Controller",80,60);
  
//Mapping Mouse Movements Between 0 - 255
  float pitch = map(mouseY, 0, height, 0, 255);
  float yaw = map(mouseX, 0, width, 0, 255);
  int thickness = 75;
  float len_scale = 1.25;
  
  fill(255); 
  textSize(16);
  text("Yaw: "+nf(int(yaw),3),26,208);
  fill(50);  rect(25, 215, 255*len_scale,thickness);
  fill(181, yaw, 58);  rect(25, 215, yaw*len_scale,thickness);
  
  fill(255); 
  textSize(16);
  text("Pitch: "+nf(int(pitch),3),391,103);
  fill(50); rect(385, 110, thickness,255*len_scale);
  fill(181, pitch, 58); rect(385, 110, thickness,pitch*len_scale);
  
//String needs to be defined inside the draw function to keep updating strings
  String servo_inputs = '<'+ nf(int(pitch),3) + nf(int(yaw),3) + '>';
  println(servo_inputs);
  myPort.write(servo_inputs); delay(100);
}

void setGradient(int x, int y, float w, float h, color c1, color c2, int axis ) {

  noFill();

  if (axis == Y_AXIS) {  // Top to bottom gradient
    for (int i = y; i <= y+h; i++) {
      float inter = map(i, y, y+h, 0, 1);
      color c = lerpColor(c1, c2, inter);
      stroke(c);
      line(x, i, x+w, i);
    }
  }  
  else if (axis == X_AXIS) {  // Left to right gradient
    for (int i = x; i <= x+w; i++) {
      float inter = map(i, x, x+w, 0, 1);
      color c = lerpColor(c1, c2, inter);
      stroke(c);
      line(i, y, i, y+h);
    }
  }
}
