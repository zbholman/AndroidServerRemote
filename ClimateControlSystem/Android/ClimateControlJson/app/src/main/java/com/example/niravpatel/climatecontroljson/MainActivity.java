package com.example.niravpatel.climatecontroljson;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.util.JsonWriter;
import android.widget.Button;
import android.widget.TextView;
import org.json.JSONObject;
import org.json.JSONArray;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final TextView text1 = (TextView) findViewById(R.id.TextView1);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

       FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        Button up = (Button) findViewById(R.id.upButton);
        Button down = (Button) findViewById(R.id.downButton);

        up.setOnClickListener(new View.OnClickListener() {
            int counter = 55;

            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
                 counter ++;

                JSONObject jsonObj = new JSONObject();
                JSONArray jsonArray = new JSONArray();

                try {
                    jsonObj.put("temp",counter);
                    jsonObj.put("name", "Climate System");

                    text1.setText(jsonObj.toString());

                } catch (Exception ex) {
                    ex.printStackTrace();

                }
            }
        });

        down.setOnClickListener(new View.OnClickListener() {
            int counter;
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
                counter --;

                JSONObject jsonObj = new JSONObject();
                JSONArray jsonArray = new JSONArray();

                try {
                    jsonObj.put("temp",counter);
                    jsonObj.put("name", "Climate System");

                    text1.setText(jsonObj.toString());

                } catch (Exception ex) {
                    ex.printStackTrace();

                }
            }
        });


        }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
