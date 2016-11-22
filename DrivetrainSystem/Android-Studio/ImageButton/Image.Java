 private GoogleApiClient client;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_drive_train);

        btnDis = (Button) findViewById(R.id.btnDis);
        btn_Drive = (Button) findViewById(R.id.btn_Drive);
        btn_Neutral = (Button) findViewById(R.id.btn_Neutral);
        btn_Reverse = (Button) findViewById(R.id.btn_Reverse);
        btn_Park = (Button) findViewById(R.id.btn_Park);

       // imageButton_NoGear = (ImageButton) findViewById(R.id.imageButton_NoGear);
        imageButton_Up = (ImageButton) findViewById(R.id.imageButton_Up);
        imageButton_Down = (ImageButton) findViewById(R.id.imageButton_Down);
        imageButton_Left = (ImageButton) findViewById(R.id.imageButton_Left);
        imageButton_Right = (ImageButton) findViewById(R.id.imageButton_Right);
      //  imageButton_Stop = (ImageButton) findViewById(R.id.imageButton_Stop);
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
                    btn_Park.setClickable(false);
                    btn_Park.setBackgroundColor(Color.WHITE);

                    mConnectedThread.write("w");    // Send the signal to car to move up
                    Toast.makeText(getBaseContext(), "Car Ready To Move", Toast.LENGTH_SHORT).show();

                    Toast.makeText(getBaseContext(), "Drive Mode", Toast.LENGTH_SHORT).show();
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
                    btn_Park.setClickable(false);
                    btn_Park.setBackgroundColor(Color.WHITE);

                    Toast.makeText(getBaseContext(), "Reverse Mode", Toast.LENGTH_SHORT).show();
                }
            }
        });

        imageButton_Right.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if (imageButton_Up.isPressed()) {
                    btn_Drive.setBackgroundColor(Color.GREEN);
                    btn_Reverse.setBackgroundColor(Color.WHITE);
                    btn_Reverse.setClickable(false);
                    btn_Neutral.setClickable(false);
                    btn_Park.setClickable(false);
                    btn_Park.setBackgroundColor(Color.WHITE);

                    Toast.makeText(getBaseContext(), "Drive Mode", Toast.LENGTH_SHORT).show();
                }
            }
        });

        imageButton_Left.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if (imageButton_Up.isPressed()) {
                    btn_Drive.setBackgroundColor(Color.GREEN);
                    btn_Reverse.setBackgroundColor(Color.WHITE);
                    btn_Reverse.setClickable(false);
                    btn_Neutral.setClickable(false);
                    btn_Park.setClickable(false);
                    btn_Park.setBackgroundColor(Color.WHITE);

                    Toast.makeText(getBaseContext(), "Drive Mode", Toast.LENGTH_SHORT).show();
                }
            }
        });
