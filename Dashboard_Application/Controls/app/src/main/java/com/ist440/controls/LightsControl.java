package com.ist440.controls;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class LightsControl extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lights_control);

        final String username = "pi";
        final String password = "raspberry";
        final String hostname = "192.168.1.251";
        final int port = 22;

    }
}
