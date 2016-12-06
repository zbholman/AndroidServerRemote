/**
 * Author: Chakman Fung， QIli Jian, Abu Sakif, David Austin.
 * IST 440W
 * Penn State Abington
 * TEAM 1, Pump Your Brake
 */

package ist440.brakescontrol;



import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Login extends AppCompatActivity {
    //define variables
    Button logIn;
    EditText username, password, hostname;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        logIn = (Button) findViewById(R.id.main_Enter);
    }

    // initialize variables for connecting to pi
    public void Enter(View view) {
        username = (EditText) findViewById(R.id.main_username);
        password = (EditText) findViewById(R.id.main_password);
        hostname = (EditText) findViewById(R.id.main_hostname);

        //prompt for user to enter the info variables

        Intent myIntent = new Intent(Login.this, BrakesControl.class);
        startActivity(new Intent(Login.this, BrakesControl.class));
        myIntent.putExtra("username", username.getText().toString());
        myIntent.putExtra("password", password.getText().toString());
        myIntent.putExtra("hostname", hostname.getText().toString());
        startActivity(myIntent);

    }

}

