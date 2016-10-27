const int xInput = A0;
2.const int yInput = A1;
3.const int zInput = A2;
4.const int buttonPin = 2;
5. 
6.// Raw Ranges:
7.// initialize to mid-range and allow calibration to
8.// find the minimum and maximum for each axis
9.int xRawMin = 512;
10.int xRawMax = 512;
11. 
12.int yRawMin = 512;
13.int yRawMax = 512;
14. 
15.int zRawMin = 512;
16.int zRawMax = 512;
17. 
18.// Take multiple samples to reduce noise
19.const int sampleSize = 10;
20. 
21.void setup() 
22.{
23.  analogReference(EXTERNAL);
24.  Serial.begin(9600);
25.}
26. 
27.void loop() 
28.{
29.  int xRaw = ReadAxis(xInput);
30.  int yRaw = ReadAxis(yInput);
31.  int zRaw = ReadAxis(zInput);
32.  
33.  if (digitalRead(buttonPin) == LOW)
34.  {
35.    AutoCalibrate(xRaw, yRaw, zRaw);
36.  }
37.  else
38.  {
39.    Serial.print("Raw Ranges: X: ");
40.    Serial.print(xRawMin);
41.    Serial.print("-");
42.    Serial.print(xRawMax);
43.    
44.    Serial.print(", Y: ");
45.    Serial.print(yRawMin);
46.    Serial.print("-");
47.    Serial.print(yRawMax);
48.    
49.    Serial.print(", Z: ");
50.    Serial.print(zRawMin);
51.    Serial.print("-");
52.    Serial.print(zRawMax);
53.    Serial.println();
54.    Serial.print(xRaw);
55.    Serial.print(", ");
56.    Serial.print(yRaw);
57.    Serial.print(", ");
58.    Serial.print(zRaw);
59.    
60.    // Convert raw values to 'milli-Gs"
61.    long xScaled = map(xRaw, xRawMin, xRawMax, -1000, 1000);
62.    long yScaled = map(yRaw, yRawMin, yRawMax, -1000, 1000);
63.    long zScaled = map(zRaw, zRawMin, zRawMax, -1000, 1000);
64.  
65.    // re-scale to fractional Gs
66.    float xAccel = xScaled / 1000.0;
67.    float yAccel = yScaled / 1000.0;
68.    float zAccel = zScaled / 1000.0;
69.  
70.    Serial.print(" :: ");
71.    Serial.print(xAccel);
72.    Serial.print("G, ");
73.    Serial.print(yAccel);
74.    Serial.print("G, ");
75.    Serial.print(zAccel);
76.    Serial.println("G");
77.  
78.  delay(500);
79.  }
80.}
81. 
82.//
83.// Read "sampleSize" samples and report the average
84.//
85.int ReadAxis(int axisPin)
86.{
87.  long reading = 0;
88.  analogRead(axisPin);
89.  delay(1);
90.  for (int i = 0; i < sampleSize; i++)
91.  {
92.    reading += analogRead(axisPin);
93.  }
94.  return reading/sampleSize;
95.}
96. 
97.//
98.// Find the extreme raw readings from each axis
99.//
100.void AutoCalibrate(int xRaw, int yRaw, int zRaw)
101.{
102.  Serial.println("Calibrate");
103.  if (xRaw < xRawMin)
104.  {
105.    xRawMin = xRaw;
106.  }
107.  if (xRaw > xRawMax)
108.  {
109.    xRawMax = xRaw;
110.  }
111.  
112.  if (yRaw < yRawMin)
113.  {
114.    yRawMin = yRaw;
115.  }
116.  if (yRaw > yRawMax)
117.  {
118.    yRawMax = yRaw;
119.  }
120. 
121.  if (zRaw < zRawMin)
122.  {
123.    zRawMin = zRaw;
124.  }
125.  if (zRaw > zRawMax)
126.  {
127.    zRawMax = zRaw;
128.  }
129.}
