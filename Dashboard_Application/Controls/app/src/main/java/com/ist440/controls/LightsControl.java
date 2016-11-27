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
        final String hostname = "104.39.121.91"; // Pi IP on PSU network
//        final String hostname = "192.168.1.251"; // Pi IP on Brian's home network

        final String scriptsDir = "/home/pi/PSUABFA16IST440/LightingSystem/Scripts/";
        final String lightsDir = "python /home/pi/PSUABFA16IST440/LightingSystem/Scroll_phat/";
        final String ledBarLightsDir = "python /home/pi/PSUABFA16IST440/LightingSystem/LedBarLights/";
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

        // Set all icons to invisibule
        iconHazards.setVisibility(View.INVISIBLE);
        iconHighBeams.setVisibility(View.INVISIBLE);
        iconHeadLights.setVisibility(View.INVISIBLE);
        iconLeftTurn.setVisibility(View.INVISIBLE);
        iconRightTurn.setVisibility(View.INVISIBLE);

        // Set default state to false (off)
        switchHighBeams.setChecked(false);
        switchHeadLights.setChecked(false);
        switchLeftTurn.setChecked(false);
        switchRightTurn.setChecked(false);
        switchHazards.setChecked(false);

        // Variables for storing light states

        switchHighBeams.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            // Function that gets called when switch is toggled
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // If the toggle is switched to "ON" run the following
                // turn on high beams
                if (isChecked) {
                    boolean success = true;
                    // Turn off other lights to avoid conflict
                    switchHeadLights.setChecked(false);
                    switchHazards.setChecked(false);
                    switchLeftTurn.setChecked(false);
                    switchRightTurn.setChecked(false);

                    String command = lightsDir + "High_Beams.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If the light turns on, set icon to visible
                    if (success) {iconHighBeams.setVisibility(View.VISIBLE);}

                // If the switch it turned off, turn off the leds
                } else {
                    boolean success = true;
                    String command = lightsDir + "Leds_Off.py";
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
                // turn on head lights
                if (isChecked) {
                    boolean success = true;
                    // Turn off other lights to avoid conflict
                    switchHazards.setChecked(false);
                    switchLeftTurn.setChecked(false);
                    switchRightTurn.setChecked(false);
                    switchHighBeams.setChecked(false);

                    String command = lightsDir + "Running_Lights.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If the light turns on, set icon to visible
                    if (success) {iconHeadLights.setVisibility(View.VISIBLE);}
                } else {
                    boolean success = true;

                    // Turn LEDs off if head light switch is turned off
                    String command = lightsDir + "Leds_Off.py";
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
                    // Turn off other lights to avoid conflict
                    switchHeadLights.setChecked(false);
                    switchHazards.setChecked(false);
                    switchRightTurn.setChecked(false);
                    switchHighBeams.setChecked(false);

                    String command = scriptsDir + "Left_Turn_On.sh";
                    backgroundTask(username, password, hostname, command, port);

                    // If the light turns on, start blinking left turn icon
                    if (success) {
                        iconLeftTurn.setVisibility(View.VISIBLE);
                    }
                    //while (success) {
                        //iconLeftTurn.setVisibility(View.VISIBLE);
                        //iconLeftTurn.startAnimation(animation);
                    //}
                } else {
                    boolean success = true;
                    String command = scriptsDir + "Left_Turn_Off.sh";
                    backgroundTask(username, password, hostname, command, port);

                    // If light turns off, set icon to invisible
                    if (success) {
                        iconLeftTurn.setVisibility(View.INVISIBLE);
                    }
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
                    // Turn off other lights to avoid conflict
                    switchHeadLights.setChecked(false);
                    switchHazards.setChecked(false);
                    switchLeftTurn.setChecked(false);
                    switchHighBeams.setChecked(false);

                    String command = scriptsDir + "Right_Turn_On.sh";
                    backgroundTask(username, password, hostname, command, port);

                    // If the light turns on, start blinking right turn icon
                    if (success) {
                        iconRightTurn.setVisibility(View.VISIBLE);
                        //iconRightTurn.startAnimation(animation);
                    }

                } else {
                    boolean success = true;
                    String command = scriptsDir + "Right_Turn_Off.sh";
                    backgroundTask(username, password, hostname, command, port);

                    // If light turns off, set icon to invisible
                    if (success) {iconRightTurn.setVisibility(View.INVISIBLE);}
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
                    // Turn off other lights to avoid conflict
                    switchHeadLights.setChecked(false);
                    switchLeftTurn.setChecked(false);
                    switchRightTurn.setChecked(false);
                    switchHighBeams.setChecked(false);

                    String command = scriptsDir + "Hazard_On.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If the light turns on, set icon to visible
                    if (success) {iconHazards.setVisibility(View.VISIBLE);}
                } else {
                    boolean success = true;
                    String command = scriptsDir + "Hazard_Off.py";
                    backgroundTask(username, password, hostname, command, port);

                    // If light turns off, start blinking hazards icon
                    if (success) {
                        iconHazards.setVisibility(View.INVISIBLE);
                    }
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
