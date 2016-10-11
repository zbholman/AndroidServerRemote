package com.example.niravpatel.climatecontrolandroidapp;

import android.media.Image;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ToggleButton;
import android.widget.Switch;
import android.widget.CompoundButton;


import android.os.AsyncTask;
import android.widget.ImageView;

import com.google.android.gms.appindexing.Action;
import com.google.android.gms.appindexing.AppIndex;
import com.google.android.gms.appindexing.Thing;
import com.google.android.gms.common.api.GoogleApiClient;
import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;

import java.util.Properties;

import  android.widget.CompoundButton.OnCheckedChangeListener;


public class MainActivity extends AppCompatActivity {

    private ToggleButton btnToggleAC, btnToggleHeat;
    private Switch switchFan;
    ImageButton btntemp1Inc, btntemp1Dec, btntemp2Inc, btntemp2Dec;
    TextView temp1, temp2;
    int tempCounter1, tempCounter2;
    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    private GoogleApiClient client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnToggleAC = (ToggleButton) findViewById(R.id.btnToggleAC);
        btnToggleHeat = (ToggleButton) findViewById(R.id.btnToggleHeat);
        btntemp1Inc = (ImageButton) findViewById(R.id.btnTemp1Inc);
        btntemp1Dec = (ImageButton) findViewById(R.id.btnTemp1Dec);

        btnToggleAC.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {

                StringBuffer result = new StringBuffer();
                result.append("Air Conditioner: ").append(btnToggleAC.getText());

                Toast.makeText(MainActivity.this, result.toString(),
                        Toast.LENGTH_SHORT).show();

            }
        });

        btnToggleHeat.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {

                StringBuffer result = new StringBuffer();
                result.append("Heat : ").append(btnToggleHeat.getText());

                Toast.makeText(MainActivity.this, result.toString(),
                        Toast.LENGTH_SHORT).show();

            }
        });

        btntemp1Inc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                tempCounter1++;
                temp1.setText(tempCounter1);

            }
        });

        //COnnecting with android
        final String username = "pi";
        final String password = "raspberry";
        final String hostname = "10.0.0.157";
        final String lightsDir = "python /home/pi/Team03/PSUABFA16IST440/ClimateControlSystem";
        final int port = 22;

        // Create switch for fan
        Switch switchFan = (Switch) findViewById(R.id.switchFan);
        switchFan.setChecked(false);
        switchFan.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            // Function that gets called when switch is toggled
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // If the toggle is switched to "ON" run the following
                // turn on high beams
                if (isChecked) {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = lightsDir + "/FanOnOff.py";

                        protected Void doInBackground(Integer... params) {
                            try {
                                // Execute command on the pi
                                runPiCommand(username, password, hostname, command, port);
                            } catch (JSchException e) {
                                e.printStackTrace();
                            }
                            return null;
                        }
                    }.execute(1);

                }
            }

        });
    }

    public void runPiCommand(String username, String password, String hostname, String command, int port) throws JSchException {
        // New Jsch object for connecting
        JSch jsch = new JSch();

        // Try to create a session using username, hostname, and port
        Session session = null;
        try {
            session = jsch.getSession(username, hostname, port);
        } catch (JSchException e) {
            e.printStackTrace();
        }

        // Set the password for the session
        assert session != null;
        session.setPassword(password);

        // Avoid asking for key confirmation
        Properties prop = new Properties();
        prop.put("StrictHostKeyChecking", "no");
        session.setConfig(prop);

        // Attempt to connect
        try {
            session.connect();
        } catch (JSchException e) {
            e.printStackTrace();
        }

        // SSH Channel
        ChannelExec channelssh = null;
        try {
            channelssh = (ChannelExec)
                    session.openChannel("exec");
        } catch (JSchException e) {
            e.printStackTrace();
        }
        // Use this if there is any need for output to return to android
//        ByteArrayOutputStream baos = new ByteArrayOutputStream();
//
//        channelssh.setOutputStream(baos);

        // Execute command
        assert channelssh != null;
        channelssh.setCommand(command);
        try {
            channelssh.connect();
        } catch (JSchException e) {
            e.printStackTrace();
        }
        channelssh.disconnect();
    }
}

