package bluetooth.ist440.testbluetooth;

import android.os.Build;
import android.support.annotation.RequiresApi;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;


import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.os.Handler;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;


public class testBluetooth extends AppCompatActivity {

    Button btnOn, btnOff,btnDis;
    TextView txtString;
    Handler bluetoothIn;

    final int handlerState = 0;                    //used to identify handler message
    private BluetoothAdapter btAdapter = null;
    private BluetoothSocket btSocket = null;
    private StringBuilder recDataString = new StringBuilder();

    private ConnectedThread mConnectedThread;

    // String for MAC address
    private static String address;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );

        setContentView( R.layout.activity_test_bluetooth );

        //Link the buttons and textViews to respective views
        btnOn = (Button) findViewById( R.id.btnON );
        btnOff = (Button) findViewById( R.id.btnOFF );
        txtString = (TextView) findViewById( R.id.text );
        btnDis = (Button) findViewById(R.id.btnDis);

        bluetoothIn = new Handler() {
            public void handleMessage(android.os.Message msg) {
                if (msg.what == handlerState) {                   //if message is what we want
                    String readMessage = (String) msg.obj;
                    txtString.setText(readMessage);         // here it print temperature from PI
                }
            }

        };

        btAdapter = BluetoothAdapter.getDefaultAdapter();       // get Bluetooth adapter
        checkBTState();                                     // check the status of Bluetooth


        // Set up onClick listeners for buttons to send 1 or 0 to turn on/off LED
        btnOff.setOnClickListener( new OnClickListener() {
            public void onClick(View v) {
                mConnectedThread.write( "0" );    // Send "0" via Bluetooth
                Toast.makeText( getBaseContext(), "Turn off LED", Toast.LENGTH_SHORT ).show();
            }
        } );

        btnOn.setOnClickListener( new OnClickListener() {
            public void onClick(View v) {
                mConnectedThread.write( "1" );    // Send "1" via Bluetooth
                Toast.makeText( getBaseContext(), "Turn on LED", Toast.LENGTH_SHORT ).show();
            }
        } );

        btnDis.setOnClickListener( new OnClickListener() {
            public void onClick(View v) {
                Disconnect();
                Toast.makeText( getBaseContext(), "Exited", Toast.LENGTH_SHORT ).show();
            }
        } );



    }

    private void Disconnect()
    {
        if (btSocket!=null) //If the btSocket is busy
        {
            try
            {
                btSocket.close(); //close connection
            }
            catch (IOException e)
            {Toast.makeText( getBaseContext(), "Error", Toast.LENGTH_SHORT ).show();}
        }
        finish(); //return to the first layout

    }


    private BluetoothSocket createBluetoothSocket(BluetoothDevice device) throws IOException, NoSuchMethodException, InvocationTargetException, IllegalAccessException {

        int port = 1;
        Method m = device.getClass().getMethod("createRfcommSocket", int.class);
        btSocket = (BluetoothSocket) m.invoke(device,port);

        return btSocket;
        //creates secure outgoing connecetion with BT device using Port Number
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
        BluetoothDevice device = btAdapter.getRemoteDevice( address );

        try {
            btSocket = createBluetoothSocket( device );
        } catch (IOException e) {
            Toast.makeText( getBaseContext(), "Socket creation failed", Toast.LENGTH_LONG ).show();
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
        mConnectedThread = new ConnectedThread( btSocket );
        mConnectedThread.start();
        //mConnectedThread.write( "x" );
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
            Toast.makeText( getBaseContext(), "Device does not support bluetooth", Toast.LENGTH_LONG ).show();
        } else {
            if (btAdapter.isEnabled()) {
            } else {
                Intent enableBtIntent = new Intent( BluetoothAdapter.ACTION_REQUEST_ENABLE );
                startActivityForResult( enableBtIntent, 1 );
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
                    bytes = mmInStream.read( buffer );            //read bytes from input buffer
                    String readMessage = new String( buffer, 0, bytes );

                    // Send the obtained bytes to the UI Activity via handler
                    bluetoothIn.obtainMessage( handlerState, bytes, -1, readMessage ).sendToTarget();
                } catch (IOException e) {
                    break;
                }
            }
        }

        //write method
        public void write(String input) {
            byte[] msgBuffer = input.getBytes();           //converts entered String into bytes
            try {
                mmOutStream.write( msgBuffer );                //write bytes over BT connection via outstream
            } catch (IOException e) {
                //if you cannot write, close the application
                Toast.makeText( getBaseContext(), "Connection Failure", Toast.LENGTH_LONG ).show();
                finish();

            }
        }
    }



}
