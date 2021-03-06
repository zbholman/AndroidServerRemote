package com.example.shake.braking_system;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.Switch;

import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;

import java.util.Properties;

import static com.example.shake.braking_system.R.id.btnFL;

public class Braking_System extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_braking__system);

        final String username = "pi";
        final String password = "raspberry";
        final String hostname = "192.168.1.251";

        final String RelayDir = "python /home/pi/Team01/PSUABFA16IST440/BrakingSystem/Relay";
        final int port = 22;
        final ImageButton btnFR = (ImageButton) findViewById(R.id.btnFR);
        btnFR.setOnClickListener(new View.OnClickListener()  {
            @Override
            public void onClick(View v) {
                new AsyncTask<Integer, Void, Void>() {
                    String command = RelayDir + "/Brake_fr.py";

                    protected Void doInBackground(Integer... params) {
                        try {
                            // Execute command on the pi
                            runPiCommand(username, password, hostname, command, port);
                        } catch (JSchException e) {
                            e.printStackTrace();
                        }
                        return null;
                    }
                };
            }

            });
        //ImageButton btnFL = (ImageButton) findViewById(R.id.btnFL);
        //ImageButton btnRR = (ImageButton) findViewById(R.id.btnRR);
        //ImageButton btnRL = (ImageButton) findViewById(R.id.btnRL);


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

