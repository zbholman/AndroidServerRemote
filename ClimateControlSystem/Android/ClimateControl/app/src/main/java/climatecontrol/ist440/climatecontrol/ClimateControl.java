package climatecontrol.ist440.climatecontrol;


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
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.CompoundButton;
import android.widget.CompoundButton.OnCheckedChangeListener;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;


public class ClimateControl extends AppCompatActivity {

    // String for MAC address
    String address;
    final int handlerState = 0;                    //used to identify handler message
    public String readMessage;
    Handler bluetoothHandler;
    ImageButton imageButtonInc, imageButtonDec;
    Button btnDis;
    TextView txt_Temp, txt_PI_Temp;
    Switch switch_AC, switch_Heat;
    int mCounter = 65;
    int minTemp = 59, maxTemp = 80;
    Runnable runnable = new Runnable() {
        @Override
        public void run() {
            try {

                bluetoothHandler = new Handler() {
                    public void handleMessage(android.os.Message msg) {
                        if (msg.what == handlerState) {                   //if message is what we want
                            readMessage = (String) msg.obj;
                            txt_PI_Temp.setText(readMessage);         // here it print temperature from PI

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
    private ConnectedThread mConnectedThread;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_climate_control);

        btnDis = (Button) findViewById(R.id.btnDis);
        imageButtonInc = (ImageButton) findViewById(R.id.imageButtonInc);
        imageButtonDec = (ImageButton) findViewById(R.id.imageButtonDec);
        txt_Temp = (TextView) findViewById(R.id.txt_Temp);
        txt_PI_Temp = (TextView) findViewById(R.id.txt_PI_Temp);
        switch_AC = (Switch) findViewById(R.id.switch_AC);
        switch_Heat = (Switch) findViewById(R.id.switch_Heat);


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

        switch_AC.setChecked(false);
        switch_Heat.setChecked(false);
        txt_Temp.setTextColor(Color.WHITE);
        txt_Temp.setText(Integer.toString(mCounter));


        imageButtonInc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                mCounter++;
                txt_Temp.setText(Integer.toString(mCounter));

                if (mCounter > maxTemp) {
                    mCounter = maxTemp;
                    Toast.makeText(getBaseContext(), "Max Temperature Reached", Toast.LENGTH_SHORT).show();
                    txt_Temp.setText(Integer.toString(mCounter));

                } else if (imageButtonInc.isPressed() && mCounter > 65) {
                    switch_Heat.setChecked(false);
                    switch_AC.setChecked(true);
                    txt_Temp.setTextColor(Color.RED);
                    // AC Pin goes ON Relay

                    /*
                    mConnectedThread.write( "acON" );    // Send "acON" via Bluetooth
                    Toast.makeText( getBaseContext(), "AC Turned ON", Toast.LENGTH_SHORT ).show();
                    */

                } else if (Integer.toString(mCounter).equals(readMessage)) {
                    Toast.makeText(getBaseContext(), "Temperature is equal", Toast.LENGTH_SHORT).show();
                }

                if (imageButtonInc.isPressed() && mCounter == 65) {
                    switch_Heat.setChecked(false);
                    switch_AC.setChecked(false);
                    txt_Temp.setTextColor(Color.WHITE);
                    // ALL pins on Relay are OFF

                }


            }

        });

        imageButtonDec.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                mCounter--;
                txt_Temp.setText(Integer.toString(mCounter));

                if (mCounter < minTemp) {
                    mCounter = minTemp;
                    Toast.makeText(getBaseContext(), "Min Temperature Reached", Toast.LENGTH_SHORT).show();
                    txt_Temp.setText(Integer.toString(mCounter));

                } else if (imageButtonDec.isPressed() && mCounter < 65) {
                    switch_Heat.setChecked(true);
                    switch_AC.setChecked(false);
                    txt_Temp.setTextColor(Color.BLUE);

                    // HEATING PAD Pin goes ON Relay
                     /*
                    mConnectedThread.write( "heatON" );    // Send "heatON" via Bluetooth
                    Toast.makeText( getBaseContext(), "Heating Turned ON", Toast.LENGTH_SHORT ).show();
                    */

                }
                if (imageButtonDec.isPressed() && mCounter == 65) {
                    switch_Heat.setChecked(false);
                    switch_AC.setChecked(false);
                    txt_Temp.setTextColor(Color.WHITE);
                    // ALL pins on Relay are OFF
                }
            }

        });

        switch_AC.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            @Override
            public void onCheckedChanged(CompoundButton buttonView,
                                         boolean isChecked) {

                if(isChecked){
                     /*
                    mConnectedThread.write( "acON" );    // Send "acON" via Bluetooth
                    */

                    Toast.makeText( getBaseContext(), "AC ON", Toast.LENGTH_SHORT ).show();
                }else{
                     /*
                    mConnectedThread.write( "acOFF" );    // Send "acOFF" via Bluetooth
                    */
                    Toast.makeText( getBaseContext(), "AC OFF", Toast.LENGTH_SHORT ).show();
                }

            }
        });

        switch_Heat.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            @Override
            public void onCheckedChanged(CompoundButton buttonView,
                                         boolean isChecked) {

                if(isChecked){
                     /*
                    mConnectedThread.write( "heatON" );    // Send "heatON" via Bluetooth
                    */

                    Toast.makeText( getBaseContext(), "Heating ON", Toast.LENGTH_SHORT ).show();
                }else{
                     /*
                    mConnectedThread.write( "heatOFF" );    // Send "heatOFF" via Bluetooth
                    */
                    Toast.makeText( getBaseContext(), "Heating OFF", Toast.LENGTH_SHORT ).show();
                }

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

