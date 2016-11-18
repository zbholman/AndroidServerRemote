package ist440.brakescontrol;

/**
 * Created by QILI JIAN on 11/17/2016.
 */


import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Login extends AppCompatActivity {
    Button b1;
    EditText username, password, hostname;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        b1 = (Button) findViewById(R.id.main_Enter);
    }

    public void Enter(View view) {
        username = (EditText) findViewById(R.id.main_username);
        password = (EditText) findViewById(R.id.main_password);
        hostname = (EditText) findViewById(R.id.main_hostname);

        Intent myIntent = new Intent(Login.this, BrakesControl.class);
        startActivity(new Intent(Login.this, BrakesControl.class));
        myIntent.putExtra("username", username.getText().toString());
        myIntent.putExtra("password", password.getText().toString());
        myIntent.putExtra("hostname", hostname.getText().toString());
        startActivity(myIntent);

    }

}

