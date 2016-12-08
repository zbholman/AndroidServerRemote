#IST 440 Penn State Abington
#Professor: Joseph Oakes
#Fall 2016
#DriveTrain
#Author: Tapan Patel and Joseph Altomare
#Version: 5



  @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_drive_train);

        #Finds the various button IDs
        btnDis = (Button) findViewById(R.id.btnDis);
        btn_Drive = (Button) findViewById(R.id.btn_Drive);
        btn_Neutral = (Button) findViewById(R.id.btn_Neutral);
        btn_Reverse = (Button) findViewById(R.id.btn_Reverse);
        btn_Park = (Button) findViewById(R.id.btn_Park);

        imageButton_Up = (ImageButton) findViewById(R.id.imageButton_Up);
        imageButton_Neutral = (ImageButton) findViewById(R.id.imageButton_Neutral);
        imageButton_Down = (ImageButton) findViewById(R.id.imageButton_Down);
        imageButton_Left = (ImageButton) findViewById(R.id.imageButton_Left);
        imageButton_Right = (ImageButton) findViewById(R.id.imageButton_Right);
        imageButton_Stop = (ImageButton) findViewById(R.id.imageButton_Stop);
        imageButton_Center = (ImageButton) findViewById(R.id.imageButton_Center);
        txt_Speed = (TextView) findViewById(R.id.txt_Speed);

        btn_Park.setBackgroundColor(Color.RED);



        bluetoothHandler = new Handler();

        ///Set time interval here
        bluetoothHandler.postDelayed(runnable, 1000);


        btAdapter = BluetoothAdapter.getDefaultAdapter();       // get Bluetooth adapter
        checkBTState();                                     // check the status of Bluetooth


        btnDis.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Disconnect();
                Toast.makeText(getBaseContext(), "Exited", Toast.LENGTH_SHORT).show();
            }
        });

        imageButton_Up.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if (imageButton_Up.isPressed()) {
                    btn_Drive.setBackgroundColor(Color.GREEN);
                    btn_Reverse.setBackgroundColor(Color.WHITE);
                    btn_Reverse.setClickable(false);
                    btn_Neutral.setClickable(false);
                    btn_Neutral.setBackgroundColor(Color.WHITE);
                    btn_Park.setClickable(false);
                    btn_Park.setBackgroundColor(Color.WHITE);

                    mConnectedThread.write("w");    // Send the signal to car to move up
                    Toast.makeText(getBaseContext(), "Car Moving", Toast.LENGTH_SHORT).show();

                }
            }
        });

        imageButton_Center.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if (imageButton_Center.isPressed()) {
                    btn_Drive.setBackgroundColor(Color.GREEN);
                    btn_Reverse.setBackgroundColor(Color.WHITE);
                    btn_Reverse.setClickable(false);
                    btn_Neutral.setClickable(false);
                    btn_Neutral.setBackgroundColor(Color.WHITE);
                    btn_Park.setClickable(false);
                    btn_Park.setBackgroundColor(Color.WHITE);

                    mConnectedThread.write("c");    // tired are straight
                    Toast.makeText(getBaseContext(), "Cars Tires Are Straight", Toast.LENGTH_SHORT).show();
                }
            }
        });
        imageButton_Down.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if (imageButton_Down.isPressed()) {
                    btn_Reverse.setBackgroundColor(Color.YELLOW);
                    btn_Drive.setBackgroundColor(Color.WHITE);
                    btn_Drive.setClickable(false);
                    btn_Neutral.setClickable(false);
                    btn_Neutral.setBackgroundColor(Color.WHITE);
                    btn_Park.setClickable(false);
                    btn_Park.setBackgroundColor(Color.WHITE);

                    mConnectedThread.write("s");    // Send the signal to car to move up
                    Toast.makeText(getBaseContext(), "Car Moving Backward", Toast.LENGTH_SHORT).show();

                }
            }
        });

        imageButton_Right.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if (imageButton_Right.isPressed()) {
                    btn_Drive.setBackgroundColor(Color.GREEN);
                    btn_Reverse.setBackgroundColor(Color.WHITE);
                    btn_Reverse.setClickable(false);
                    btn_Neutral.setClickable(false);
                    btn_Neutral.setBackgroundColor(Color.WHITE);
                    btn_Park.setClickable(false);
                    btn_Park.setBackgroundColor(Color.WHITE);

                    mConnectedThread.write("d");    // Send the signal to car to move up
                    Toast.makeText(getBaseContext(), "Car Moving Right", Toast.LENGTH_SHORT).show();
                }
            }
        });

        imageButton_Left.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if (imageButton_Left.isPressed()) {
                    btn_Drive.setBackgroundColor(Color.GREEN);
                    btn_Reverse.setBackgroundColor(Color.WHITE);
                    btn_Reverse.setClickable(false);
                    btn_Neutral.setClickable(false);
                    btn_Park.setClickable(false);
                    btn_Neutral.setBackgroundColor(Color.WHITE);
                    btn_Park.setBackgroundColor(Color.WHITE);

                    mConnectedThread.write("a");    // Send the signal to car to move up
                    Toast.makeText(getBaseContext(), "Car Moving Left", Toast.LENGTH_SHORT).show();

                }
            }
        });

        imageButton_Stop.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if (imageButton_Stop.isPressed()) {
                    btn_Park.setBackgroundColor(Color.RED);
                    btn_Reverse.setBackgroundColor(Color.WHITE);
                    btn_Reverse.setClickable(false);
                    btn_Park.setClickable(false);
                    btn_Drive.setClickable(false);
                    btn_Neutral.setBackgroundColor(Color.WHITE);
                    btn_Drive.setBackgroundColor(Color.WHITE);

                    mConnectedThread.write("p");    // Send the signal to car to move up
                    Toast.makeText(getBaseContext(), "Car Not Moving", Toast.LENGTH_SHORT).show();

                }
            }
        });


        imageButton_Neutral.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if (imageButton_Neutral.isPressed()) {
                    btn_Neutral.setBackgroundColor(Color.BLUE);
                    btn_Reverse.setBackgroundColor(Color.WHITE);
                    btn_Reverse.setClickable(false);
                    btn_Park.setClickable(false);
                    btn_Drive.setClickable(false);
                    btn_Drive.setBackgroundColor(Color.WHITE);
                    btn_Park.setBackgroundColor(Color.WHITE);

                    mConnectedThread.write("n");    // Send the signal to car to move up
                    Toast.makeText(getBaseContext(), "Car Moving Itself", Toast.LENGTH_SHORT).show();

                }
            }
        });
