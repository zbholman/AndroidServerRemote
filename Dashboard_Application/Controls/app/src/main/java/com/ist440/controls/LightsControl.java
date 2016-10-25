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
        final String username = "team";
        final String password = "lightingsystem";
        final String hostname = "75.102.85.173"; // Pi IP on PSU network
//        final String hostname = "192.168.1.251"; // Pi IP on Brian's home network

        final String lightsDir = "python /home/pi/Team04/PSUABFA16IST440/LightingSystem/PythonLights/Scroll_phat/";
        final int port = 22;

        // Create switch for lights
        Switch switchHighBeams = (Switch) findViewById(R.id.switchHighBeams);
        Switch switchHeadLights = (Switch) findViewById(R.id.switchHeadLights);
        Switch switchLeftTurn = (Switch) findViewById(R.id.switchLeftTurn);

        // Create icon images
        final ImageView iconHighBeams = (ImageView) findViewById(R.id.iconHighBeams);
        final ImageView iconHeadLights = (ImageView) findViewById(R.id.iconHeadLights);
        final ImageView iconLeftTurn = (ImageView) findViewById(R.id.iconLeftTurn);

        // Set default state to false (off)
        switchHighBeams.setChecked(false);
        switchHeadLights.setChecked(false);
        switchLeftTurn.setChecked(false);

        switchHighBeams.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            // Function that gets called when switch is toggled
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // If the toggle is switched to "ON" run the following
                // turn on high beams
                if (isChecked) {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = lightsDir + "high_beams.py";
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

                    // If the light turns on, set icon to visible
                    if (success) {iconHighBeams.setVisibility(View.VISIBLE);}
                } else {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = lightsDir + "turn-leds-off.py";
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
                    new AsyncTask<Integer, Void, Void>() {
                        String command = lightsDir + "head_lights.py";
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

                    // If the light turns on, set icon to visible
                    if (success) {iconHeadLights.setVisibility(View.VISIBLE);}
                } else {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = lightsDir + "turn-leds-off.py";
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

                    // If light turns off, set icon to invisible
                    if (success) {iconHeadLights.setVisibility(View.INVISIBLE);}
                }
            }
        });

        // Create listener event for high beams
        switchLeftTurn.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            // Function that gets called when switch is toggled
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // If the toggle is switched to "ON" run the following
                // turn on high beams
                if (isChecked) {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = lightsDir + "turn_signal.py";
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

                    // If the light turns on, set icon to visible
                    if (success) {iconLeftTurn.setVisibility(View.VISIBLE);}
                } else {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = lightsDir + "/turn-leds-off.py";
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

                    // If light turns off, set icon to invisible
                    if (success) {iconLeftTurn.setVisibility(View.INVISIBLE);}
                }
            }
        });

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
