package com.example.niravpatel.climatecontrolandroidapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.Toast;
import android.widget.ToggleButton;
import android.widget.Switch;



public class MainActivity extends AppCompatActivity {

    private ToggleButton btnToggleAC;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // initiate a Switch
        Switch simpleSwitch = (Switch) findViewById(R.id.switchAuto);

        // check current state of a Switch (true or false).
        Boolean switchState = simpleSwitch.isChecked();

        simpleSwitch.setTextOn("On"); // displayed text of the Switch whenever it is in checked or on state
        simpleSwitch.setTextOff("Off"); // displayed text of the Switch whenever it is in unchecked i.e. off state

        btnToggleAC = (ToggleButton) findViewById(R.id.btnToggleAC);
        btnToggleAC.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {

                StringBuffer result = new StringBuffer();
                result.append("Air Conditioner: ").append(btnToggleAC.getText());

                Toast.makeText(MainActivity.this, result.toString(),
                        Toast.LENGTH_SHORT).show();

            }
        });
    }
    }