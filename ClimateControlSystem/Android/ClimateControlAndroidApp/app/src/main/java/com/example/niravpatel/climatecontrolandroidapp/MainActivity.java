package com.example.niravpatel.climatecontrolandroidapp;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;
import android.widget.ToggleButton;

import java.util.Properties;

public class MainActivity extends AppCompatActivity {



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final String username = "pi";
        final String password = "raspberry";
        final String hostname = "10.0.0.157";

        final String scriptDir = "/home/pi/Desktop";
        final int port = 22;

        final Button btntest = (Button) findViewById(R.id.btntest);

        btntest.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                new AsyncTask<Integer, Void, Void>() {
                    String command = scriptDir + "/FanOne.py";

                    protected Void doInBackground(Integer... params) {
                        try {
                            executeRemoteCommand(username, password, hostname, command, port);
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                        return null;
                    }
                }.execute(1);

            }


        });
    }


    // This method is connects to the pi, and runs the command given
    public void executeRemoteCommand(String username,
                                     String password,
                                     String hostname,
                                     String command,
                                     int port)
            throws JSchException {
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

