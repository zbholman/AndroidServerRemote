package ist440.android;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.Session;

import java.io.ByteArrayOutputStream;
import java.util.Properties;

public class MainActivity extends AppCompatActivity {
    private Button allBrakeSSH;
    public String Ausgabe;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        //Button press event listener
        allBrakeSSH.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                new AsyncTask<Integer, Void, Void>() {

                    @Override
                    protected Void doInBackground(Integer... params) {
                        try {
                               Ausgabe = executeRemoteCommand("pi", "raspberry", "192.168.1.112",22);

                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                        return null;
                    }
                }.execute(1);
            }
        });
    }


    public static String executeRemoteCommand(String username, String password, String hostname, int port, String SSH)
            throws Exception {
        JSch jsch = new JSch();
        Session session = jsch.getSession(username, hostname, port);
        session.setPassword(password);

        //Avoid asking for key confirmation
        Properties prop = new Properties();
        prop.put("StringHostKeyChecking", "no");
        session.setConfig(prop);

        session.connect();

        //SSH channel
        ChannelExec channelssh = (ChannelExec)
                session.openChannel("exec");
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        channelssh.setOutputStream(baos);

        //Execute command
        //channelssh.setCommand("cd Desktop");
        //channelssh.setCommand("sudo java -classpath .:classes:/opt/pi4j/lib/'*' SimpleTextServer");
        channelssh.setCommand("sudo reboot");
        channelssh.connect();
        channelssh.disconnect();


        return baos.toString();


    }
}




