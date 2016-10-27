package com.example.ist.energymonitor;

/*
    Class: IST440W
    Professor: Joseph Oakes
    Penn State Abington
    Team 5 - Energy Management System
    author: Chaitali Patel
    The Energy Monitor Android application will control the Energy source of the car.
    The main goal is to communicate with other sub systems to alert users to any changes in depletion of energy and provide further instructions to follow.
*/


import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import java.util.Properties;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        //create Reference with the screen widget components
        TextView energyUsedView = (TextView) findViewById(R.id.energyUsedDisplay);
        TextView energyRemView = (TextView) findViewById(R.id.energyRemDisplay);

    }
}



