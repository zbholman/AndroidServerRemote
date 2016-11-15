// Author: Brian Holman
// Project: IST 440 - Lighting System
// Date: 10-05-2016

package com.ist440.controls;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageButton;

public class Home extends AppCompatActivity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // Get the view from activity_main.xml
        setContentView(R.layout.activity_home);

        // Locate the button in activity_main.xml
        ImageButton lightControls = (ImageButton) findViewById(R.id.btnLightControls);

        // Capture button clicks
        lightControls.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {

                // Start NewActivity.class
                Intent myIntent = new Intent(Home.this,
                        LightsControl.class);
                startActivity(myIntent);
            }
        });
    }
}
