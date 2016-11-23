package com.example.ist.energymonitor;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.os.Build;
import android.os.Handler;
import android.support.annotation.RequiresApi;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;


public class EnergyMonitor extends AppCompatActivity {

    // String for windows address
    String address;
    final int handlerState = 0;                    //used to identify handler message
    public String readMessage;
    public Handler bluetoothHandler;
    Button btnDis;
    TextView txt_PI_Volt, txt_energyused, txt_energyremaining, Label_energyused, Label_energyrem;
    Runnable runnable = new Runnable() {
        @Override
        public void run() {

            try {

                bluetoothHandler = new Handler() {
                    public void handleMessage(android.os.Message msg) {
                        if (msg.what == handlerState) {
                            readMessage = (String) msg.obj;
                            txt_PI_Volt.setText(readMessage);         // print voltage from Pi

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

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_energy_monitor);

        btnDis = (Button) findViewById(R.id.btnDis);
        txt_PI_Volt = (TextView) findViewById(R.id.txt_PI_Volt);
        txt_energyused = (TextView) findViewById(R.id.txt_energyused);
        txt_energyremaining = (TextView) findViewById(R.id.txt_energyremaining);
        Label_energyused = (TextView) findViewById(R.id.Label_energyused);
        Label_energyrem = (TextView) findViewById(R.id.Label_energyrem);


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

        //creates secure outgoing connection with BT device using Port Number
        return btSocket;
    }

    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    @Override
    public void onResume() {
        super.onResume();

        //Get windows address from DeviceListActivity via intent
        Intent intent = getIntent();

        //Get the windows address from the DeviceListActivity via EXTRA
        address = intent.getStringExtra(DeviceList.EXTRA_ADDRESS);

        //create device and set the windows address
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
        ConnectedThread mConnectedThread = new ConnectedThread(btSocket);
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
            if (!btAdapter.isEnabled()) {
                Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                startActivityForResult(enableBtIntent, 1);
            }
        }
    }

    @Override
    public void onStart() {
        super.onStart();
    }

    @Override
    public void onStop() {
        super.onStop();
    }
    //create new class for connect thread
    private class ConnectedThread extends Thread {
        private final InputStream mmInStream;
        private final OutputStream mmOutStream;

        //creation of the connect thread
        ConnectedThread(BluetoothSocket socket) {
            InputStream tmpIn = null;
            OutputStream tmpOut = null;

            try {
                //Create I/O streams for connection
                tmpIn = socket.getInputStream();
                tmpOut = socket.getOutputStream();
            } catch (IOException ignored) {
            }

            mmInStream = tmpIn;
            mmOutStream = tmpOut;
        }


        public void run() {
            byte[] buffer = new byte[1024];  // buffer store for the stream
            int bytes;                      // bytes returned from read()

            // Keep listening to the InputStream until an exception occurs
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
        void write(String input) {
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








