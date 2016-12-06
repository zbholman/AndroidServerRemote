/**
 * Author Qili Jian
 * IST 440W
 * Penn State Abington
 * TEAM 1, Pump Your Brake
 */
package ist440.brakescontrol;



import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.CompoundButton;
import android.widget.ImageView;
import android.widget.ToggleButton;

import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;

import java.util.Properties;


public class BrakesControl extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_brakes_control);

        Intent myIntent =  getIntent();

        // initialize variables for connecting to pi from the Login java class
        final String username = myIntent.getExtras().getString("username");
        final String password = myIntent.getExtras().getString("password");
        final String hostname = myIntent.getExtras().getString("hostname");
        //final String hostname = "192.168.1.105";

        final String scriptDir = "python /home/pi/PSUABFA16IST440/BrakingSystem";
        //final String scriptDir2 = "python /home/pi/PSUABFA16IST440/BrakingSystem/E-Brake Python";
        final int port = 22;

        //Creating toggle button for all brakes
        final ToggleButton absBrake = (ToggleButton) findViewById(R.id.absBrake);
        final ToggleButton sensorBrake = (ToggleButton) findViewById(R.id.sensorBrake);
        final ToggleButton eBrake = (ToggleButton) findViewById(R.id.eBrake);
        final ToggleButton brake = (ToggleButton) findViewById(R.id.brake);

        //Creating the icon for each brake
        final ImageView fRight = (ImageView) findViewById(R.id.fRight);
        final ImageView rLeft = (ImageView) findViewById(R.id.rLeft);
        final ImageView rRight = (ImageView) findViewById(R.id.rRight);
        final ImageView fLeft = (ImageView) findViewById(R.id.fLeft);

        //set all icon to invisible
        fRight.setVisibility(View.INVISIBLE);
        rLeft.setVisibility(View.INVISIBLE);
        rRight.setVisibility(View.INVISIBLE);
        fLeft.setVisibility(View.INVISIBLE);


        brake.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {

            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked){
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = scriptDir + "/braking.py";

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
                        fRight.setVisibility(View.VISIBLE);
                        rLeft.setVisibility(View.VISIBLE);
                        rRight.setVisibility(View.VISIBLE);
                        fLeft.setVisibility(View.VISIBLE);


                    }

                } else {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = scriptDir + "/sensor_stop.py";

                        protected Void doInBackground(Integer... params) {
                            try {
                                executeRemoteCommand(username, password, hostname, command, port);
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                            return null;
                        }
                    }.execute(1);
                    if(success){
                        fRight.setVisibility(View.INVISIBLE);
                        rLeft.setVisibility(View.INVISIBLE);
                        rRight.setVisibility(View.INVISIBLE);
                        fLeft.setVisibility(View.INVISIBLE);
                    }

                }


            }
        });
        absBrake.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked){
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = scriptDir + "/absbraking.py";

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
                        fRight.setVisibility(View.VISIBLE);
                        rLeft.setVisibility(View.VISIBLE);
                        rRight.setVisibility(View.VISIBLE);
                        fLeft.setVisibility(View.VISIBLE);


                    }

                } else {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = scriptDir + "/braking.py";

                        protected Void doInBackground(Integer... params) {
                            try {
                                executeRemoteCommand(username, password, hostname, command, port);
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                            return null;
                        }
                    }.execute(1);
                    if(success){
                        fRight.setVisibility(View.INVISIBLE);
                        rLeft.setVisibility(View.INVISIBLE);
                        rRight.setVisibility(View.INVISIBLE);
                        fLeft.setVisibility(View.INVISIBLE);
                    }

                }


            }


        });
        sensorBrake.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked){
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = scriptDir + "/sensor_stop.py";

                        protected Void doInBackground(Integer... params) {
                            try {
                                executeRemoteCommand(username, password, hostname, command, port);
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                            return null;
                        }
                    }.execute(1);


                } else {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = scriptDir + "/eBrakeOff.py.py";

                        protected Void doInBackground(Integer... params) {
                            try {
                                executeRemoteCommand(username, password, hostname, command, port);
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                            return null;
                        }
                    }.execute(1);
                    if(success){
                        fRight.setVisibility(View.INVISIBLE);
                        rLeft.setVisibility(View.INVISIBLE);
                        rRight.setVisibility(View.INVISIBLE);
                        fLeft.setVisibility(View.INVISIBLE);
                    }

                }


            }


        });
        eBrake.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked){
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = scriptDir + "/eBrakeOn.py";

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
                        fRight.setVisibility(View.VISIBLE);
                        rLeft.setVisibility(View.VISIBLE);
                        rRight.setVisibility(View.VISIBLE);
                        fLeft.setVisibility(View.VISIBLE);


                    }

                } else {
                    boolean success = true;
                    new AsyncTask<Integer, Void, Void>() {
                        String command = scriptDir + "/eBrakeOff.py";

                        protected Void doInBackground(Integer... params) {
                            try {
                                executeRemoteCommand(username, password, hostname, command, port);
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                            return null;
                        }
                    }.execute(1);
                    if(success){
                        fRight.setVisibility(View.INVISIBLE);
                        rLeft.setVisibility(View.INVISIBLE);
                        rRight.setVisibility(View.INVISIBLE);
                        fLeft.setVisibility(View.INVISIBLE);
                    }

                }


            }


        });
    }




    // This method is connects to the pi, and runs the command given
    public void executeRemoteCommand (String username,
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

