package saac.androidapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.view.View.OnClickListener;
import android.widget.EditText;

public class Main extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Instantiates widgets for use in onclick
        Button button = (Button) findViewById(R.id.button);
        Button button2 = (Button) findViewById(R.id.button2);
        Button button3 = (Button) findViewById(R.id.button3);
        Button button4 = (Button) findViewById(R.id.button4);
        Button button5 = (Button) findViewById(R.id.button5);
        Button button6 = (Button) findViewById(R.id.button6);
        Button button7 = (Button) findViewById(R.id.button7);
        Button button8 = (Button) findViewById(R.id.button8);
        Button button9 = (Button) findViewById(R.id.button9);
        Button button10 = (Button) findViewById(R.id.button10);
        Button button11 = (Button) findViewById(R.id.button11);
        Button button12 = (Button) findViewById(R.id.button12);
        final EditText editText = (EditText) findViewById(R.id.editText);
        final EditText editText2 = (EditText) findViewById(R.id.editText2);

        //ALL NUMBER BUTTONS AND ACTION BUTTON DECLARATIONS
        button.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText.setText("*");
                    editText2.setText("1");
                    sCode = "*";
                    sNum = "1";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "1";
                    if(sNum.matches("123456")){
                        editText.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "1");
                }
            }
        });

        button2.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText.setText("*");
                    editText2.setText("2");
                    sCode = "*";
                    sNum = "2";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "2";
                    if(sNum.matches("123456")){
                        editText.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "2");
                }
            }
        });

        button3.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText.setText("*");
                    editText2.setText("3");
                    sCode = "*";
                    sNum = "3";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "3";
                    if(sNum.matches("123456")){
                        editText.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "3");
                }
            }
        });

        button4.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText.setText("*");
                    editText2.setText("4");
                    sCode = "*";
                    sNum = "4";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "4";
                    if(sNum.matches("123456")){
                        editText.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "4");
                }
            }
        });

        button5.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText.setText("*");
                    editText2.setText("5");
                    sCode = "*";
                    sNum = "5";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "5";
                    if(sNum.matches("123456")){
                        editText.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "5");
                }
            }
        });

        button6.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText.setText("*");
                    editText2.setText("6");
                    sCode = "*";
                    sNum = "6";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "6";
                    if(sNum.matches("123456")){
                        editText.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "6");
                }
            }
        });

        button7.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText.setText("*");
                    editText2.setText("7");
                    sCode = "*";
                    sNum = "7";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "7";
                    if(sNum.matches("123456")){
                        editText.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "7");
                }
            }
        });

        button8.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText.setText("*");
                    editText2.setText("8");
                    sCode = "*";
                    sNum = "8";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "8";
                    if(sNum.matches("123456")){
                        editText.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "8");
                }
            }
        });

        button9.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText.setText("*");
                    editText2.setText("9");
                    sCode = "*";
                    sNum = "9";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "1";
                    if(sNum.matches("123456")){
                        editText.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "9");
                }
            }
        });

        //clear button
        button10.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                    editText.setText("");
                    editText2.setText("");
            }
        });

        button11.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText.setText("*");
                    editText2.setText("0");
                    sCode = "*";
                    sNum = "0";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "0";
                    if(sNum.matches("123456")){
                        editText.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "0");
                }
            }
        });

        button12.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();
                int codeLen = sCode.length();
                int numLen = sNum.length();
                StringBuilder myCode = new StringBuilder(sCode);
                if(codeLen == 1){
                    codeLen -= 1;
                    myCode.deleteCharAt(codeLen);
                }
                else{
                    codeLen -= 1;
                    myCode.deleteCharAt(codeLen);
                    codeLen -= 1;
                    myCode.deleteCharAt(codeLen);
                }


                StringBuilder myNum = new StringBuilder(sNum);
                numLen -= 1;
                myNum.deleteCharAt(numLen);

                editText.setText(myCode.toString());
                editText2.setText(myNum.toString());
            }
        });


    }

}
