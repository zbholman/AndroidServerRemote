package com.ist440.controls;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.CompoundButton;
import android.widget.Switch;

import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;

import java.io.ByteArrayOutputStream;
import java.util.Properties;

public class LightsControl extends AppCompatActivity {

    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    private Switch switchFogLights;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lights_control);

        final String username = "pi";
        final String password = "raspberry";
        final String hostname = "192.168.1.251";
        final int port = 22;

        switchFogLights = (Switch) findViewById(R.id.switchFogLights);
        switchFogLights.setChecked(false);
        switchFogLights.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {

            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                String command = "";

                if (isChecked) {
                    // turn on fog lights
                    command = ""; // Need to add command to be executed
                    runPiCommand(username, password, hostname, command, port);
                } else {
                    // turn off fog lights
                    command = ""; // Need to add command to be executed
                    runPiCommand(username, password, hostname, command, port);

                }
            }
        });
    }

    public void runPiCommand(String username, String password, String hostname, String command, int port) {
        JSch jsch = new JSch();
        Session session = null;
        try {
            session = jsch.getSession(username, hostname, port);
        } catch (JSchException e) {
            e.printStackTrace();
        }
        session.setPassword(password);

        // Avoid asking for key confirmation
        Properties prop = new Properties();
        prop.put("StrictHostKeyChecking", "no");
        session.setConfig(prop);

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
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        channelssh.setOutputStream(baos);

        // Execute command
        channelssh.setCommand(command);
        try {
            channelssh.connect();
        } catch (JSchException e) {
            e.printStackTrace();
        }
        channelssh.disconnect();

        return;
    }
}
