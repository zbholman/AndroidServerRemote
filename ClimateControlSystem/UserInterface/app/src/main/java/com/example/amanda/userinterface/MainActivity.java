package com.example.amanda.userinterface;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private int mCounter = 60;
    Button increase;
    Button decrease;
    TextView temp;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        increase = (Button) findViewById(R.id.increase);
        temp = (TextView) findViewById(R.id.temp);

        increase.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                mCounter ++;
                temp.setText(Integer.toString(mCounter));

            }

        });

        decrease = (Button) findViewById(R.id.decrease);
        temp = (TextView) findViewById(R.id.temp);

        decrease.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                mCounter --;
                temp.setText(Integer.toString(mCounter));

            }
        });

        //
        //
        //passenger

        //increase_pass = (Button) findViewById(R.id.increase_pass);
        //temp_pass = (TextView) findViewById(R.id.temp_pass);

        //increase_pass.setOnClickListener(new View.OnClickListener() {
          //  @Override
            //public void onClick(View view) {

//                mInteger ++;
  //              temp_pass.setText(Integer.toString(mInteger));

    //        }
      //  });

        //decrease_pass = (Button) findViewById(R.id.decrease_pass);
        //temp_pass = (TextView) findViewById(R.id.temp_pass);

        //decrease_pass.setOnClickListener(new View.OnClickListener() {
          //  @Override
            //public void onClick(View v) {

              //  mInteger --;
                //temp_pass.setText(Integer.toString(mInteger));
            //}
       // });


        //heat



    }


}
