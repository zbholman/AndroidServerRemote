package com.ist440.lightingsystem;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.CompoundButton;
import android.widget.ToggleButton;
import com.jcraft.jsch.*;

import java.io.ByteArrayOutputStream;
import java.util.Properties;

public class LightingOptions extends AppCompatActivity {

    private ToggleButton toggleFogLights;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lighting_options);

        final String username = "pi";
        final String password = "raspberry";
        final String hostname = "192.168.1.1";
        final int port = 22;

        toggleFogLights = (ToggleButton) findViewById(R.id.toggleFogLights);
        toggleFogLights.setChecked(false);
        toggleFogLights.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {

            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    // Turn on fog lights
                    String command = "";
                    runPiCommand(username, password, hostname, command, port);
                } else {
                    // Turn off fog lights
                }
            }

        });
    }
    public void runPiCommand(String username, String password, String hostname, String command, int port){
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
