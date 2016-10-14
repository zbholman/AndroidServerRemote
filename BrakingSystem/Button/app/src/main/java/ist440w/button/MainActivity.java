package ist440w.button;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ToggleButton;

public class MainActivity extends AppCompatActivity {
    TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView = (TextView)findViewById(R.id.result_text);
        textView.setVisibility(View.INVISIBLE);

    }
    public void changeButtonState(View view)
    {
        boolean checked = ((ToggleButton)view).isChecked();
        if(checked)
        {
            textView.setText("All Brake On");
            textView.setVisibility(View.VISIBLE);
        }
        else
        {
            textView.setText("All Brakes Off");
        }
    }


}