package com.example.niravpatel.climatecontrolandroidapp;

import android.media.Image;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ToggleButton;
import android.widget.Switch;



public class MainActivity extends AppCompatActivity {

    private ToggleButton btnToggleAC,btnToggleHeat;
    private Switch switchFan;
    ImageButton btntemp1Inc,btntemp1Dec,btntemp2Inc,btntemp2Dec;
    TextView temp1,temp2;
    int tempCounter1 , tempCounter2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnToggleAC = (ToggleButton) findViewById(R.id.btnToggleAC);
        btnToggleHeat = (ToggleButton) findViewById(R.id.btnToggleHeat);
        btntemp1Inc = (ImageButton) findViewById(R.id.btnTemp1Inc);
        btntemp1Dec = (ImageButton) findViewById(R.id.btnTemp1Dec);

        switchFan = (Switch) findViewById(R.id.switchFan);

        btnToggleAC.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {

                StringBuffer result = new StringBuffer();
                result.append("Air Conditioner: ").append(btnToggleAC.getText());

                Toast.makeText(MainActivity.this, result.toString(),
                        Toast.LENGTH_SHORT).show();

            }
        });

        btnToggleHeat.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {

                StringBuffer result = new StringBuffer();
                result.append("Heat : ").append(btnToggleHeat.getText());

                Toast.makeText(MainActivity.this, result.toString(),
                        Toast.LENGTH_SHORT).show();

            }
        });

        btntemp1Inc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                tempCounter1 ++;
                temp1.setText(tempCounter1);

            }
        });
    }
}