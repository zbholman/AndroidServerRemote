package saac.androidapp;

/*
    Class: IST440W
    Professor: Joseph Oakes
    Penn State Abington
    Team 6 - Safety and Access Control

    This Android application was started in September as part of the IST 440 Group 6, Safety and Access Control Systems
    This application will be a control board to support and communicate with the car robot in order to perform necessary functions
    Functions included:
    - Unlock, Lock, and Alarm settings. This will be in the form of visual buttons as well as a keypad code.
    - Create JSON objects upon successful event calls to send to Pi robot for logging

    This app was primarily developed by team member: Matt Handwerk
 */

import android.media.MediaPlayer;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.view.View.OnClickListener;
import android.widget.EditText;
import android.widget.ImageButton;

import com.google.android.gms.appindexing.Action;
import com.google.android.gms.appindexing.AppIndex;
import com.google.android.gms.common.api.GoogleApiClient;

//Imports for SSH into Pi
import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.Properties;

public class Main extends AppCompatActivity {
    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    private GoogleApiClient client;

    public void runPiCommand(String user, String pass, String host, String command, int port) throws JSchException {
        // New Jsch object for connecting
        JSch jsch = new JSch();

        // Try to create a session using username, hostname, and port
        Session session = null;
        try {
            session = jsch.getSession(user, host, port);
        } catch (JSchException e) {
            e.printStackTrace();
        }

        // Set the password for the session
        assert session != null;
        session.setPassword(pass);

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



    //Start of the app
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        final String user = "pi";
        final String pass = "IST440FA";
        final String host = "104.39.120.129";

        final String dir = "sudo python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem";
        final int port = 22;

        //Instantiates widgets for use in onclick
        Button button = (Button) findViewById(R.id.button);
        Button button2 = (Button) findViewById(R.id.button2);
        Button button3 = (Button) findViewById(R.id.button3);
        Button button4 = (Button) findViewById(R.id.button4);
        Button button5 = (Button) findViewById(R.id.button5);
        Button button6 = (Button) findViewById(R.id.button6);
        Button button7 = (Button) findViewById(R.id.button7);
        Button button8 = (Button) findViewById(R.id.button8);
        Button button9 = (Button) findViewById(R.id.button9);
        Button button10 = (Button) findViewById(R.id.button10);
        Button button11 = (Button) findViewById(R.id.button11);
        Button button12 = (Button) findViewById(R.id.button12);

        //Fields to contain password and password asterisks, as well as event description
        final EditText editText = (EditText) findViewById(R.id.editText);
        final EditText editText2 = (EditText) findViewById(R.id.editText2);
        final EditText editText3 = (EditText) findViewById(R.id.editText3);

        //Picture buttons
        ImageButton lockButton = (ImageButton) findViewById(R.id.lockButton);
        ImageButton unlockButton = (ImageButton) findViewById(R.id.unlockButton);
        ImageButton alarmButton = (ImageButton) findViewById(R.id.alarmButton);

        //Initialize media player files
        final MediaPlayer unlock = MediaPlayer.create(this, R.raw.unlockcar);
        final MediaPlayer alarm = MediaPlayer.create(this, R.raw.setalarm);
        final MediaPlayer lock = MediaPlayer.create(this, R.raw.lockcar);
        //final MediaPlayer alarm = MediaPlayer.create(this, R.raw.setalarm);

        //ALL NUMBER BUTTONS AND ACTION BUTTON DECLARATIONS

        //All number buttons have same code, see BUTTON 1 for comments
        //BUTTON 6 has correct passcode and UNLOCK ssh call

        assert button != null;
        assert button2 != null;
        assert button3 != null;
        assert button4 != null;
        assert button5 != null;
        assert button6 != null;
        assert button7 != null;
        assert button8 != null;
        assert button9 != null;
        assert button10 != null;
        assert button11 != null;
        assert button12 != null;
        assert editText != null;
        assert editText2 != null;
        assert editText3 != null;
        assert unlockButton != null;
        assert lockButton != null;
        assert alarmButton != null;


        //LOCK BUTTON
        lockButton.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                //JSON Object LOCK
                        /*JSONObject jsonObj = new JSONObject();
                        JSONArray jsonArray = new JSONArray();
                        try {
                            jsonObj.put("CD", 23790);
                            jsonObj.put("Lock", "Door Lock Event");

                            jsonArray.put("system1");
                            jsonArray.put("system2");

                            jsonObj.put("sys", jsonArray);

                        }catch (Exception ex)
                        {
                            ex.printStackTrace();

                        }*/

                //Starts SSH asynchronously, so app does not hesitate when making connection
                String command = dir + "/Doors_locked.py";
                startASync(user, pass, host, command, port);

                }
        });

        //UNLOCK BUTTON
        unlockButton.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                //JSON Object UNLOCK
                /*JSONObject jsonObj = new JSONObject();
                        JSONArray jsonArray = new JSONArray();
                        try {
                            jsonObj.put("CD", 23789);
                            jsonObj.put("Unlock", "Door Unlock Event");

                            jsonArray.put("system1");
                            jsonArray.put("system2");

                            jsonObj.put("sys", jsonArray);

                        }catch (Exception ex)
                        {
                            ex.printStackTrace();

                        }*/

                //Starts SSH asynchronously, so app does not hesitate when making connection
                String command = dir + "/Doors_unlock.py";
                startASync(user, pass, host, command, port);

            }
        });

        //SET ALARM BUTTON
        alarmButton.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                //JSON Object ALARM
                        /*JSONObject jsonObj = new JSONObject();
                        JSONArray jsonArray = new JSONArray();
                        try {
                            jsonObj.put("CA", 33789);
                            jsonObj.put("Alarm", "Alarm Set event");

                            jsonArray.put("system1");
                            jsonArray.put("system2");

                            jsonObj.put("sys", jsonArray);

                        }catch (Exception ex)
                        {
                            ex.printStackTrace();

                        }*/

                //Starts SSH asynchronously, so app does not hesitate when making connection

                String command = dir + "/car_alarm.py";
                startASync(user, pass, host, command, port);

            }
        });


        //BUTTON 1
        button.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                //gets current text and sets temp variables as content
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                //checks if door was just unlocked/wrong password was entered
                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")) {
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("1");

                    sCode = "*";
                    sNum = "1";
                }
                //checks if PASSWORD is 1 digit away from being 6, therefore it needs to authenticate
                else if (sCode.matches("\\* \\* \\* \\* \\*")) {
                    sNum = sNum + "1";
                    //CORRECT
                    if (sNum.matches("123456")) {
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                    }
                    //INCORRECT
                    else {
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                //If string is not empty, adds space and * for better visual display of Asterisks
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "1");
                }
            }
        });

        //BUTTON 2
        button2.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")) {
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("2");
                    sCode = "*";
                    sNum = "2";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")) {
                    sNum = sNum + "2";
                    editText.setText("");
                    editText3.setText("Wrong Password");
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "2");
                }
            }
        });

        //BUTTON 3
        button3.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")) {
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("3");
                    sCode = "*";
                    sNum = "3";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")) {
                    sNum = sNum + "3";
                    editText.setText("");
                    editText3.setText("Wrong Password");
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "3");
                }
            }
        });

        //BUTTON 4
        button4.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")) {
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("4");
                    sCode = "*";
                    sNum = "4";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")) {
                    sNum = sNum + "4";
                    editText.setText("");
                    editText3.setText("Wrong Password");
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "4");
                }
            }
        });

        //BUTTON 5
        button5.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")) {
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("5");
                    sCode = "*";
                    sNum = "5";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")) {
                    sNum = sNum + "5";
                    editText.setText("");
                    editText3.setText("Wrong Password");
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "5");
                }
            }
        });

        //BUTTON 6
        button6.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")) {
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("6");
                    sCode = "*";
                    sNum = "6";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")) {
                    sNum = sNum + "6";
                    if (sNum.matches("123456")) {
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                        //JSON Object UNLOCK
                        /*JSONObject jsonObj = new JSONObject();
                        JSONArray jsonArray = new JSONArray();
                        try {
                            jsonObj.put("CD", 23789);
                            jsonObj.put("Unlock", "Door Unlock Event");

                            jsonArray.put("system1");
                            jsonArray.put("system2");

                            jsonObj.put("sys", jsonArray);

                        }catch (Exception ex)
                        {
                            ex.printStackTrace();

                        }*/

                        String command = dir + "/Doors_unlock.py";
                        startASync(user, pass, host, command, port);
                    }
                    else {
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "6");
                }
            }
        });

        //BUTTON 7
        button7.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")) {
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("7");
                    sCode = "*";
                    sNum = "7";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")) {
                    sNum = sNum + "7";
                    editText.setText("");
                    editText3.setText("Wrong Password");
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "7");
                }
            }
        });

        //BUTTON 8
        button8.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")) {
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("8");
                    sCode = "*";
                    sNum = "8";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")) {
                    sNum = sNum + "8";
                    editText.setText("");
                    editText3.setText("Wrong Password");
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "8");
                }
            }
        });

        //BUTTON 9
        button9.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")) {
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("9");
                    sCode = "*";
                    sNum = "9";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")) {
                    sNum = sNum + "1";
                    editText.setText("");
                    editText3.setText("Wrong Password");
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "9");
                }
            }
        });

        //CLEAR button
        //Sets both code and display string to empty
        button10.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                editText.setText("");
                editText2.setText("");
                editText3.setText("");
            }
        });

        //BUTTON 0
        button11.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")) {
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("0");
                    sCode = "*";
                    sNum = "0";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")) {
                    sNum = sNum + "0";
                    editText.setText("");
                    editText3.setText("Wrong Password");
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "0");
                }
            }
        });

        //Backspace Button
        button12.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();
                int codeLen = sCode.length();
                int numLen = sNum.length();
                StringBuilder myCode = new StringBuilder(sCode);

                //checks for empty string
                if (codeLen != 0) {
                    if (codeLen == 1) {
                        codeLen -= 1;
                        myCode.deleteCharAt(codeLen);
                    } else {
                        codeLen -= 1;
                        myCode.deleteCharAt(codeLen);
                        codeLen -= 1;
                        myCode.deleteCharAt(codeLen);
                    }


                    StringBuilder myNum = new StringBuilder(sNum);
                    numLen -= 1;
                    myNum.deleteCharAt(numLen);

                    //sets newly modified text as string
                    editText.setText(myCode.toString());
                    editText2.setText(myNum.toString());
                }
            }
        });


        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client = new GoogleApiClient.Builder(this).addApi(AppIndex.API).build();
    }

    //Starts SSH asynchronously, so app does not hesitate when making connection
    //5 arguments for Pi command line to log in and activate functionality.
    public void startASync(final String user, final String pass, final String host, final String command, final int port) {
        new AsyncTask<Integer, Void, Void>() {
            protected Void doInBackground(Integer... params) {
                try {
                    // Execute command on the pi
                    runPiCommand(user, pass, host, command, port);
                } catch (JSchException e) {
                    e.printStackTrace();
                }
                return null;
            }
        }.execute(1);
    }

    @Override
    public void onStart() {
        super.onStart();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client.connect();
        Action viewAction = Action.newAction(
                Action.TYPE_VIEW, // TODO: choose an action type.
                "Main Page", // TODO: Define a title for the content shown.
                // TODO: If you have web page content that matches this app activity's content,
                // make sure this auto-generated web page URL is correct.
                // Otherwise, set the URL to null.
                Uri.parse("http://host/path"),
                // TODO: Make sure this auto-generated app deep link URI is correct.
                Uri.parse("android-app://saac.androidapp/http/host/path")
        );
        AppIndex.AppIndexApi.start(client, viewAction);
    }

    @Override
    public void onStop() {
        super.onStop();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        Action viewAction = Action.newAction(
                Action.TYPE_VIEW, // TODO: choose an action type.
                "Main Page", // TODO: Define a title for the content shown.
                // TODO: If you have web page content that matches this app activity's content,
                // make sure this auto-generated web page URL is correct.
                // Otherwise, set the URL to null.
                Uri.parse("http://host/path"),
                // TODO: Make sure this auto-generated app deep link URI is correct.
                Uri.parse("android-app://saac.androidapp/http/host/path")
        );
        AppIndex.AppIndexApi.end(client, viewAction);
        client.disconnect();
    }
}
