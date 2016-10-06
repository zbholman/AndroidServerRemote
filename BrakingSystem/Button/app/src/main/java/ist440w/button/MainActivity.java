package ist440w.button;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        configureImageButton();
    }

    private void configureImageButton(){
        ImageButton btn = (ImageButton) findViewById(R.id.imageButton4);
        btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "You clicked the RearRight", Toast.LENGTH_SHORT).show();
                ImageButton btn = (ImageButton) findViewById(R.id.imageButton2);
                btn.setOnClickListener(new View.OnClickListener() {

                    @Override
                    public void onClick(View v) {
                        Toast.makeText(MainActivity.this, "You clicked the RearLeft", Toast.LENGTH_SHORT).show();
                        ImageButton btn = (ImageButton) findViewById(R.id.imageButton3);
                        btn.setOnClickListener(new View.OnClickListener() {

                            @Override
                            public void onClick(View v) {
                                Toast.makeText(MainActivity.this, "You clicked the FrontLeft", Toast.LENGTH_SHORT).show();
                                ImageButton btn = (ImageButton) findViewById(R.id.imageButton);
                                btn.setOnClickListener(new View.OnClickListener() {

                                    @Override
                                    public void onClick(View v) {
                                        Toast.makeText(MainActivity.this, "You clicked the FrontRight", Toast.LENGTH_SHORT).show();


                                    }
                                });
                            }
                        });
                    }
                });
            }
        });
    }
}