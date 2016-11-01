// Author: Brian Holman
// Project: IST 440 - Lighting System
// Date: 10-05-2016

package com.ist440.controls;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.CompoundButton;
import android.widget.ImageView;
import android.widget.Switch;

import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;

import java.util.Properties;

import static android.widget.CompoundButton.OnCheckedChangeListener;

public class LightsControl extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lights_control);

        // initialize variables for connecting to pi
        final String username = "pi";
        final String password = "raspberry";
        final String hostname = "130.203.105.79"; // Pi IP on PSU network
//        final String hostname = "192.168.1.251"; // Pi IP on Brian's home network

        final String lightsDir = "python /home/pi/Team04/PSUABFA16IST440/LightingSystem/PythonLights/Scroll_phat/";
        final int port = 22;

        // Create switch for lights
        final Switch switchHighBeams = (Switch) findViewById(R.id.switchHighBeams);
        final Switch switchHeadLights = (Switch) findViewById(R.id.switchHeadLights);
        final Switch switchLeftTurn = (Switch) findViewById(R.id.switchLeftTurn);
        final Switch switchRightTurn = (Switch) findViewById(R.id.switchRightTurn);
        final Switch switchHazards = (Switch) findViewById(R.id.switchHazardLight);

        // Create icon images
        final ImageView iconHighBeams = (ImageView) findViewById(R.id.iconHighBeams);
        final ImageView iconHeadLights = (ImageView) findViewById(R.id.iconHeadLights);
        final ImageView iconLeftTurn = (ImageView) findViewById(R.id.iconLeftTurn);
        final ImageView iconRightTurn = (ImageView) findViewById(R.id.iconRightTurn);
        final ImageView iconHazards = (ImageView) findViewById(R.id.iconHazardLight);


        // Set default state to false (off)
        switchHighBeams.setChecked(false);
        switchHeadLights.setChecked(false);
        switchLeftTurn.setChecked(false);
        switchRightTurn.setChecked(false);
        switchHazards.setChecked(false);

        switchHighBeams.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            // Function that gets called when switch is toggled
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // If the toggle is switched to "ON" run the following
                // turn on high beams
                if (isChecked) {
                    boolean success = true;
                    switchHeadLights.setChecked(false);

                    String command = lightsDir + "high_beams.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If the light turns on, set icon to visible
                    if (success) {iconHighBeams.setVisibility(View.VISIBLE);}
                } else {
                    boolean success = true;
                    String command = lightsDir + "turn-leds-off.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If light turns off, set icon to invisible
                    if (success) {iconHighBeams.setVisibility(View.INVISIBLE);}
                }
            }
        });


        // Create listener event for high beams
        switchHeadLights.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            // Function that gets called when switch is toggled
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // If the toggle is switched to "ON" run the following
                // turn on high beams
                if (isChecked) {
                    boolean success = true;
                    switchHighBeams.setChecked(false);

                    String command = lightsDir + "running_lights.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If the light turns on, set icon to visible
                    if (success) {iconHeadLights.setVisibility(View.VISIBLE);}
                } else {
                    boolean success = true;
                    String command = lightsDir + "turn-leds-off.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If light turns off, set icon to invisible
                    if (success) {iconHeadLights.setVisibility(View.INVISIBLE);}
                }
            }
        });

        // Create listener event for left turn signal
        switchLeftTurn.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            // Function that gets called when switch is toggled
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // If the toggle is switched to "ON" run the following
                // turn on high beams
                if (isChecked) {
                    boolean success = true;
                    switchRightTurn.setChecked(false);

                    String command = lightsDir + "turn_signal.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If the light turns on, set icon to visible
                    if (success) {iconLeftTurn.setVisibility(View.VISIBLE);}
                } else {
                    boolean success = true;
                    final String command = lightsDir + "turn-leds-off.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If light turns off, set icon to invisible
                    if (success) {iconLeftTurn.setVisibility(View.INVISIBLE);}
                }
            }
        });

        // Create listener event for right turn signal
        switchRightTurn.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            // Function that gets called when switch is toggled
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // If the toggle is switched to "ON" run the following
                // turn on high beams
                if (isChecked) {
                    boolean success = true;
                    switchLeftTurn.setChecked(false);

                    String command = lightsDir + "turn_signal_2.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If the light turns on, set icon to visible
                    if (success) {iconLeftTurn.setVisibility(View.VISIBLE);}
                } else {
                    boolean success = true;
                    final String command = lightsDir + "turn-leds-off.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If light turns off, set icon to invisible
                    if (success) {iconLeftTurn.setVisibility(View.INVISIBLE);}
                }
            }
        });

        // Create listener event for right turn signal
        switchHazards.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            // Function that gets called when switch is toggled
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // If the toggle is switched to "ON" run the following
                // turn on high beams
                if (isChecked) {
                    boolean success = true;
                    switchLeftTurn.setChecked(false);
                    switchRightTurn.setChecked(false);

                    String command = lightsDir + "hazards.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If the light turns on, set icon to visible
                    if (success) {iconLeftTurn.setVisibility(View.VISIBLE);}
                } else {
                    boolean success = true;
                    final String command = lightsDir + "turn-leds-off.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If light turns off, set icon to invisible
                    if (success) {iconLeftTurn.setVisibility(View.INVISIBLE);}
                }
            }
        });

    }

    public void backgroundTask(final String username, final String password, final String hostname, final String command, final int port) {
        new AsyncTask<Integer, Void, Void>() {
            protected Void doInBackground(Integer... params) {
                // Else, turn off high beams
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
    // This method is connects to the pi, and runs the command given
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
