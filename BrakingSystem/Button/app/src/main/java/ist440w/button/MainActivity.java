package ist440w.button;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ToggleButton;

public class MainActivity extends AppCompatActivity {
    TextView textView;
    ImageView imageView, imageView2, imageView3, imageView4;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView = (TextView)findViewById(R.id.result_text);
        imageView = (ImageView)findViewById(R.id.imageView);
        imageView2 = (ImageView)findViewById(R.id.imageView2);
        imageView3 = (ImageView)findViewById(R.id.imageView3);
        imageView4 = (ImageView)findViewById(R.id.imageView4);



    }
    public void changeButtonState(View view)
    {
        boolean checked = ((ToggleButton)view).isChecked();
        if(checked)
        {
            textView.setText("All Brake On");
            textView.setVisibility(View.VISIBLE);
            imageView.setVisibility(View.VISIBLE);
            imageView2.setVisibility(View.VISIBLE);
            imageView3.setVisibility(View.VISIBLE);
            imageView4.setVisibility(View.VISIBLE);


        }
        else
        {
            textView.setText("All Brakes Off");
            imageView.setVisibility(View.INVISIBLE);
            imageView2.setVisibility(View.INVISIBLE);
            imageView3.setVisibility(View.INVISIBLE);
            imageView4.setVisibility(View.INVISIBLE);


        }
    }


}