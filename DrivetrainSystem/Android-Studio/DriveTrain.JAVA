#IST 440 Penn State Abington
#Professor: Joseph Oakes
#Fall 2016
#DriveTrain
#Author: Tapan Patel and Joesph Altomare
#Version: 5
    
package drivetrain.ist440.drivetrain;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.graphics.Color;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.support.annotation.RequiresApi;
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

import static drivetrain.ist440.drivetrain.R.id.imageButton_Stop;


public class DriveTrain extends AppCompatActivity {

    // Windows 10
    String address;
    final int handlerState = 0;
    public String readMessage;
    Handler bluetoothHandler;
    ImageButton imageButton_Up,imageButton_Down,imageButton_Left,imageButton_Right;
    Button btnDis,btn_Park,btn_Reverse,btn_Neutral,btn_Drive;
    TextView txt_Speed;
    //int mCounter = 50;
    int minSpeed = 0, maxSpeed = 50;
    Runnable runnable = new Runnable() {
        @Override
        public void run() {
            try {

                bluetoothHandler = new Handler() {
                    public void handleMessage(android.os.Message msg) {
                        if (msg.what == handlerState) {
                            readMessage = (String) msg.obj;
                            txt_Speed.setText(readMessage);         // print speed of the car

                        }

                    }

                };
            } catch (Exception e) {
                // TODO: handle exception
                Toast.makeText(getBaseContext(), "Handler not called", Toast.LENGTH_SHORT).show();

            } finally {

                bluetoothHandler.postDelayed(this, 1000);
            }

        }
    };


    private BluetoothAdapter btAdapter = null;
    private BluetoothSocket btSocket = null;
    private ConnectedThread mConnectedThread;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_drive_train);

        btnDis = (Button) findViewById(R.id.btnDis);
        btn_Drive = (Button) findViewById(R.id.btn_Drive);
        btn_Neutral = (Button) findViewById(R.id.btn_Neutral);
        btn_Reverse = (Button) findViewById(R.id.btn_Reverse);
        btn_Park = (Button) findViewById(R.id.btn_Park);

        imageButton_Up = (ImageButton) findViewById(R.id.imageButton_Up);
        imageButton_Down = (ImageButton) findViewById(R.id.imageButton_Down);
        imageButton_Left = (ImageButton) findViewById(R.id.imageButton_Left);
        imageButton_Right = (ImageButton) findViewById(R.id.imageButton_Right);
        txt_Speed = (TextView) findViewById(R.id.txt_Speed);

        btn_Park.setBackgroundColor(Color.RED);
        btn_Park.setBackgroundColor(Color.WHITE);


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

                if(imageButton_Up.isPressed()){
                    btn_Drive.setBackgroundColor(Color.GREEN);
                    btn_Reverse.setBackgroundColor(Color.WHITE);
                    btn_Reverse.setClickable(false);
                    btn_Neutral.setClickable(false);
                    btn_Park.setClickable(false);

                    mConnectedThread.write( "w" );    // Send the signal to car to move up
                    Toast.makeText( getBaseContext(), "Car Ready To Move", Toast.LENGTH_SHORT ).show();

                    Toast.makeText(getBaseContext(), "Drive Mode", Toast.LENGTH_SHORT).show();
            }}
        });
        imageButton_Down.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if (imageButton_Down.isPressed()) {
                    btn_Reverse.setBackgroundColor(Color.RED);
                    btn_Drive.setBackgroundColor(Color.WHITE);
                    btn_Drive.setClickable(false);
                    btn_Neutral.setClickable(false);
                    btn_Park.setClickable(false);

                    Toast.makeText(getBaseContext(), "Reverse Mode", Toast.LENGTH_SHORT).show();
                }
            }
        });

        imageButton_Right.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if(imageButton_Up.isPressed()){
                    btn_Drive.setBackgroundColor(Color.GREEN);
                    btn_Reverse.setBackgroundColor(Color.WHITE);
                    btn_Reverse.setClickable(false);
                    btn_Neutral.setClickable(false);
                    btn_Park.setClickable(false);

                    Toast.makeText(getBaseContext(), "Drive Mode", Toast.LENGTH_SHORT).show();
                }}
        });

        imageButton_Left.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if(imageButton_Up.isPressed()){
                    btn_Drive.setBackgroundColor(Color.GREEN);
                    btn_Reverse.setBackgroundColor(Color.WHITE);
                    btn_Reverse.setClickable(false);
                    btn_Neutral.setClickable(false);
                    btn_Park.setClickable(false);

                    Toast.makeText(getBaseContext(), "Drive Mode", Toast.LENGTH_SHORT).show();
                }}
        });

    }

    private void findViewById(ImageButton imageButton_stop) {

    }


    private void Disconnect() {
        if (btSocket != null) //If the btSocket is busy
        {
            try {
                btSocket.close(); //close connection
            } catch (IOException e) {
                Toast.makeText(getBaseContext(), "Error", Toast.LENGTH_SHORT).show();
            }
        }
        finish(); //return to the first layout

    }


    private BluetoothSocket createBluetoothSocket(BluetoothDevice device) throws IOException, NoSuchMethodException, InvocationTargetException, IllegalAccessException {

        int port = 1;
        Method m = device.getClass().getMethod("createRfcommSocket", int.class);
        btSocket = (BluetoothSocket) m.invoke(device, port);

        //creates secure outgoing connecetion with BT device using Port Number
        return btSocket;
    }

    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    @Override
    public void onResume() {
        super.onResume();

        //Get MAC address from DeviceListActivity via intent
        Intent intent = getIntent();

        //Get the MAC address from the DeviceListActivty via EXTRA
        address = intent.getStringExtra(DeviceList.EXTRA_ADDRESS);

        //create device and set the MAC address
        BluetoothDevice device = btAdapter.getRemoteDevice(address);

        try {
            btSocket = createBluetoothSocket(device);
        } catch (IOException e) {
            Toast.makeText(getBaseContext(), "Socket creation failed", Toast.LENGTH_LONG).show();
        } catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
            e.printStackTrace();
        }
        // Establish the Bluetooth socket connection.
        try {
            btSocket.connect();
        } catch (IOException e) {
            try {
                btSocket.close();
            } catch (IOException e2) {
                //insert code to deal with this
            }
        }
        mConnectedThread = new ConnectedThread(btSocket);
        mConnectedThread.start();
        mConnectedThread.write("x");
    }

    @Override
    public void onPause() {
        super.onPause();
        try {
            //Don't leave Bluetooth sockets open when leaving activity
            btSocket.close();
        } catch (IOException e2) {
            //insert code to deal with this
        }
    }

    //Checks that the Android device Bluetooth is available and prompts to be turned on if off
    private void checkBTState() {

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
