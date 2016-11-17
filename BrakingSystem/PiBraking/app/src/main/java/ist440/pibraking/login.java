//Author: Qili Jian ,  Chak Fung
//Project IST 440 - Braking System
//Date: 10/17/16
package ist440.pibraking;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class login extends AppCompatActivity {
    Button b1;
    EditText ed1,ed2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        b1 = (Button) findViewById(R.id.main_login);
        ed1 = (EditText) findViewById(R.id.main_name);
        ed2 = (EditText) findViewById(R.id.main_password);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ed1.getText().toString().equals("brake") &&
                        ed2.getText().toString().equals("pi")) {
                    Toast.makeText(getApplicationContext(),
                            "Redirecting...", Toast.LENGTH_SHORT).show();
                    startActivity(new Intent(login.this, PiBraking.class));

                } else {
                    Toast.makeText(getApplicationContext(), "Wrong Credentials", Toast.LENGTH_SHORT).show();



                }
            }

        });

    }


}

