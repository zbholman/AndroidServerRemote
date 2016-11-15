
package ist440.pibraking;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.CompoundButton;
import android.widget.ImageView;
import android.widget.ToggleButton;

import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;

import java.util.Properties;

public class PiBraking extends AppCompatActivity {



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pi_braking);

        final String username = "pi";
        final String password = "raspberry";
        final String hostname = "104.39.123.213";

        final String scriptDir = "python /home/pi/PSUABFA16IST440/BrakingSystem";
        final int port = 22;


        final ToggleButton absBrake = (ToggleButton) findViewById(R.id.absBrake);

        final ImageView imageView =(ImageView) findViewById(R.id.fRight);
        final ImageView imageView2 =(ImageView) findViewById(R.id.rLeft);
        final ImageView imageView3 =(ImageView) findViewById(R.id.rRight);
        final ImageView imageView4 =(ImageView) findViewById(R.id.fLeft);

        imageView.setVisibility(View.INVISIBLE);
        imageView2.setVisibility(View.INVISIBLE);
        imageView3.setVisibility(View.INVISIBLE);
        imageView4.setVisibility(View.INVISIBLE);




        absBrake.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = scriptDir + "/servo1.py";

                        protected Void doInBackground(Integer... params) {
                            try {
                                executeRemoteCommand(username, password, hostname, command, port);
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                            return null;
                        }
                    }.execute(1);
                    if (success) {
                        imageView.setVisibility(View.VISIBLE);
                        imageView2.setVisibility(View.VISIBLE);
                        imageView3.setVisibility(View.VISIBLE);
                        imageView4.setVisibility(View.VISIBLE);

                    }
                } else {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = "^c";

                        protected Void doInBackground(Integer... params) {
                            try {
                                executeRemoteCommand(username, password, hostname, command, port);
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                            return null;
                        }
                    }.execute(1);
                    if (success) {
                        imageView.setVisibility(View.INVISIBLE);
                        imageView2.setVisibility(View.INVISIBLE);
                        imageView3.setVisibility(View.INVISIBLE);
                        imageView4.setVisibility(View.INVISIBLE);

                    }
                }

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



