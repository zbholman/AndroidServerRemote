package com.ist440.controls;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.CompoundButton;
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
        final String hostname = "192.168.1.251";

        final String lightsDir = "python /home/pi/Team04/PSUABFA16IST440/LightingSystem/PythonLights";
        final int port = 22;

        // Create switch for lights
        Switch switchHighBeams = (Switch) findViewById(R.id.switchHighBeams);

        // Set default state to false (off)
        switchHighBeams.setChecked(false);

        // Create listener event
        switchHighBeams.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            // Function that gets called when switch is toggled
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // If the toggle is switched to "ON" run the following
                // turn on high beams
                if (isChecked) {
                    new AsyncTask<Integer, Void, Void>() {
                        String command = lightsDir + "/high_beam.py";
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
                } else {
                    new AsyncTask<Integer, Void, Void>() {
                        String command = lightsDir + "/checkengine.py";
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
