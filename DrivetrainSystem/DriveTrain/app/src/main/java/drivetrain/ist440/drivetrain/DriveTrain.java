package drivetrain.ist440.drivetrain;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.graphics.Color;

import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import android.widget.ImageButton;

import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;


public class DriveTrain extends AppCompatActivity {

    // String for Windows address
    String address;
    final int handlerState = 0;
    public String readMessage;
    Handler bluetoothHandler;
    ImageButton imageButton_Up, imageButton_Down, imageButton_Left, imageButton_Right, imageButton_Neutral, imageButton_Stop, imageButton_Center;
    Button btnDis, btn_Park, btn_Reverse, btn_Neutral, btn_Drive;
    TextView txt_Speed;

    Runnable runnable = new Runnable() {
        @Override
        public void run() {
            try {

                bluetoothHandler = new Handler() {
                    public void handleMessage(android.os.Message msg) {
                        if (msg.what == handlerState) {
                            readMessage = (String) msg.obj;
                            txt_Speed.setText(readMessage);         // here it print the speed of the car

                        }

                    }

                };
            } catch (Exception e) {
                // TODO: handle exception
                Toast.makeText(getBaseContext(), "Handler not called", Toast.LENGTH_SHORT).show();

            } finally {
                //also call the same runnable to call it at regular interval
                bluetoothHandler.postDelayed(this, 1000);
            }

        }
    };


    private BluetoothAdapter btAdapter = null;
    private BluetoothSocket btSocket = null;
    private BluetoothAdapter btAdapter1 = null;
    private BluetoothSocket btSocket1 = null;
    private ConnectedThread mConnectedThread;
    private ConnectedThread mConnectedThread1;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_drive_train);

        btnDis = (Button) findViewById(R.id.btnDis);
        txt_Speed = (TextView) findViewById(R.id.txt_Speed);
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
        btn_Park.setBackgroundColor(Color.RED);

        bluetoothHandler = new Handler();

        ///Set time interval here
        bluetoothHandler.postDelayed(runnable, 1000);

        btAdapter = BluetoothAdapter.getDefaultAdapter();       // get Bluetooth adapter
        btAdapter1 = BluetoothAdapter.getDefaultAdapter();
        checkBTState1();                                     // check the status of Bluetooth and its connection
        checkBTState2();

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


    }

    private void Disconnect() {
        if (btSocket != null && btSocket1 != null) //If the btSocket is busy
        {
            try {
                btSocket.close(); //close connection
                btSocket1.close(); //close connection
            } catch (IOException e) {
                Toast.makeText(getBaseContext(), "Error", Toast.LENGTH_SHORT).show();
            }
        }
        finish(); //return to the first layout

    }

    // for all other controller of how fast the car is moing and turning direction
    private BluetoothSocket createBluetoothSocket(BluetoothDevice device) throws IOException, NoSuchMethodException, InvocationTargetException, IllegalAccessException {

        int port = 1;
        Method m = device.getClass().getMethod("createRfcommSocket", int.class);
        btSocket = (BluetoothSocket) m.invoke(device, port);

        //creates secure outgoing connecetion with BT device using Port Number
        return btSocket;
    }

    //for speed of the car
    private BluetoothSocket createBluetoothSocket1(BluetoothDevice device) throws IOException, NoSuchMethodException, InvocationTargetException, IllegalAccessException {

        int port = 2;
        Method m = device.getClass().getMethod("createRfcommSocket", int.class);
        btSocket1 = (BluetoothSocket) m.invoke(device, port);

        //creates secure outgoing connecetion with BT device using Port Number
        return btSocket1;
    }


    @Override
    public void onResume() {
        super.onResume();

        //Get windows address from DeviceListActivity via intent
        Intent intent = getIntent();

        //Get the windows address from the DeviceListActivty via EXTRA
        address = intent.getStringExtra(DeviceList.EXTRA_ADDRESS);

        //create device and set the windows address
        BluetoothDevice device = btAdapter.getRemoteDevice(address);


        try {
            btSocket = createBluetoothSocket(device);
            btSocket1 = createBluetoothSocket1(device);
        } catch (IOException e) {
            Toast.makeText(getBaseContext(), "Socket creation failed", Toast.LENGTH_LONG).show();
        } catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
            e.printStackTrace();
        }
        // Establish the Bluetooth socket connection.
        try {
            btSocket.connect();
            btSocket1.connect();
        } catch (IOException e) {
            try {
                btSocket.close();
                btSocket1.close();
            } catch (IOException e2) {
                //insert code to deal with this
            }
        }
        mConnectedThread = new ConnectedThread(btSocket); // for connection of moving the cars direction
        mConnectedThread1 = new ConnectedThread(btSocket1); //for how fast the car is going
        mConnectedThread.start();
        mConnectedThread1.start();
        mConnectedThread.write("x");
    }
    @Override
    public void onPause() {
        super.onPause();
        try {
            //Don't leave Bluetooth sockets open when leaving activity
            btSocket.close();
            btSocket1.close();
        } catch (IOException e2) {
            //insert code to deal with this
        }
    }

    //Checks that the Android device Bluetooth is available and prompts to be turned on if off
    private void checkBTState1() {

        if (btAdapter == null) {
            Toast.makeText(getBaseContext(), "Device does not support bluetooth", Toast.LENGTH_LONG).show();
        } else {
            if (btAdapter.isEnabled()) {
            } else {
                Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                startActivityForResult(enableBtIntent, 1);
            }
        }
    }

    private void checkBTState2() {

        if (btAdapter1 == null) {
            Toast.makeText(getBaseContext(), "Device does not support bluetooth", Toast.LENGTH_LONG).show();
        } else {
            if (btAdapter1.isEnabled()) {
            } else {
                Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                startActivityForResult(enableBtIntent, 1);
            }
        }
    }

    //create new class for connect thread
    private class ConnectedThread extends Thread {
        private final InputStream mmInStream;
        private final OutputStream mmOutStream;

        //creation of the connect thread
        public ConnectedThread(BluetoothSocket socket) {
            InputStream tmpIn = null;
            OutputStream tmpOut = null;

            try {
                //Create I/O streams for connection
                tmpIn = socket.getInputStream();
                tmpOut = socket.getOutputStream();
            } catch (IOException e) {
            }

            mmInStream = tmpIn;
            mmOutStream = tmpOut;
        }


        public void run() {
            byte[] buffer = new byte[1024];
            int bytes;

            // Keep looping to listen for received messages
            while (true) {
                try {
                    bytes = mmInStream.read(buffer);            //read bytes from input buffer
                    String readMessage = new String(buffer, 0, bytes);

                    // Send the obtained bytes to the UI Activity via handler
                    bluetoothHandler.obtainMessage(handlerState, bytes, -1, readMessage).sendToTarget();
                } catch (IOException e) {
                    break;
                }
            }
        }

        //write method
        public void write(String input) {
            byte[] msgBuffer = input.getBytes();           //converts entered String into bytes
            try {
                mmOutStream.write(msgBuffer);                //write bytes over BT connection via outstream
            } catch (IOException e) {
                //if you cannot write, close the application
                Toast.makeText(getBaseContext(), "Connection Failure", Toast.LENGTH_LONG).show();
                finish();

            }
        }
    }


}
