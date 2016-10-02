package com.ist440.controls;

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

    private Switch switchFogLights;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lights_control);

        // initialize variables for connecting to pi
        final String username = "pi";
        final String password = "raspberry";
        final String hostname = "192.168.1.251";
        //final String command = "python /home/team/PSUABFA16IST440/SamplePython/helloworld.py";
        final int port = 22;

        // Create switch for lights
        switchFogLights = (Switch) findViewById(R.id.switchFogLights);

        // Set default state to false (off)
        switchFogLights.setChecked(false);

        // Create listener event
        switchFogLights.setOnCheckedChangeListener(new OnCheckedChangeListener() {

            // Function that gets called when switch is toggled
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // Initialize command string, this is what will run on the pi
                String command = "";

                // If the toggle is switched to "ON" run the following
                if (isChecked) {
                    // turn on fog lights
                    command = "python /home/team/PSUABFA16IST440/SamplePython/helloworld.py"; // Need to add command to be executed
                    runPiCommand(username, password, hostname, command, port);
                } else {
                    // Else, turn off fog lights
                    command = ""; // Need to add command to be executed
                    runPiCommand(username, password, hostname, command, port);

                }
            }
        });
    }

    // This method is connects to the pi, and runs the command given
    public void runPiCommand(String username, String password, String hostname, String command, int port) {
        // New Jsch object for connecting
        JSch jsch = new JSch();

        // Initialize a session object
        Session session = null;

        // Try to create a session using username, hostname, and port
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
            channelssh = (ChannelExec)session.openChannel("exec");
        } catch (JSchException e) {
            e.printStackTrace();
        }
        // ByteArrayOutputStream baos = new ByteArrayOutputStream();

        // channelssh.setOutputStream(baos);

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