package ist440.brakescontrol;
/**Penn State Abington
 #IST 440W
 #Fall 2016
 #Team Pump Your Brakes
 #Members: Qili Jian,  Chakman Fung, Abu Sakif, David Austin,  **/


import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Login extends AppCompatActivity {
    //define the variables
    Button logIn;
    EditText username, password, hostname;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        //find the id for the in the UI
        logIn = (Button) findViewById(R.id.main_Enter);
    }

    public void Enter(View view) {
        username = (EditText) findViewById(R.id.main_username);
        password = (EditText) findViewById(R.id.main_password);
        hostname = (EditText) findViewById(R.id.main_hostname);

        //User Input to Log In the second activity class.
        Intent myIntent = new Intent(Login.this, BrakesControl.class);
        startActivity(new Intent(Login.this, BrakesControl.class));
        myIntent.putExtra("username", username.getText().toString());
        myIntent.putExtra("password", password.getText().toString());
        myIntent.putExtra("hostname", hostname.getText().toString());
        startActivity(myIntent);

    }

}

