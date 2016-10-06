package saac.androidapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.view.View.OnClickListener;
import android.widget.EditText;

public class Main extends AppCompatActivity {

/*
    This Android application was starter in September as part of the IST 440 Group 6, Safety and Access Control Systems
    This application will be a control board to support and communicate with the car robot in order to perform necessary functions
    Functions included:
    - Unlock, Lock, and Alarm settings. This will be in the form of visual buttons as well as a keypad code.
    - Create JSON objects upon successful event calls to send to Pi robot for logging

    This app was primarily developed by team member: Matt Handwerk
     */
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
        final EditText editText3 = (EditText) findViewById(R.id.editText3);

        //ALL NUMBER BUTTONS AND ACTION BUTTON DECLARATIONS

        //All number buttons have same code, see BUTTON 1 for comments
        //BUTTON 1
        assert button != null;
        assert button2 != null;
        assert button3 != null;
        assert button4 != null;
        assert button5 != null;
        assert button6 != null;
        assert button7 != null;
        assert button8 != null;
        assert button9 != null;
        assert button10 != null;
        assert button11 != null;
        assert button12 != null;
        assert editText != null;
        assert editText2 != null;
        assert editText3 != null;

        button.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                //gets current text and sets temp variables as content

                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                //checks if door was just unlocked/wrong password was entered
                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("1");

                    sCode = "*";
                    sNum = "1";
                }
                //checks if PASSWORD is 1 digit away from being 6, therefore it need to authenticate
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "1";
                    //CORRECT
                    if(sNum.matches("123456")){
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                    }
                    //INCORRECT
                    else{
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                //If string is not empty, adds space and * for better visual display of Asterisks
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "1");
                }
            }
        });

        //BUTTON 2
        button2.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("2");
                    sCode = "*";
                    sNum = "2";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "2";
                    if(sNum.matches("123456")){
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "2");
                }
            }
        });

        //BUTTON 3
        button3.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("3");
                    sCode = "*";
                    sNum = "3";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "3";
                    if(sNum.matches("123456")){
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "3");
                }
            }
        });

        //BUTTON 4
        button4.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("4");
                    sCode = "*";
                    sNum = "4";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "4";
                    if(sNum.matches("123456")){
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "4");
                }
            }
        });

        //BUTTON 5
        button5.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("5");
                    sCode = "*";
                    sNum = "5";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "5";
                    if(sNum.matches("123456")){
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "5");
                }
            }
        });

        //BUTTON 6
        button6.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("6");
                    sCode = "*";
                    sNum = "6";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "6";
                    if(sNum.matches("123456")){
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "6");
                }
            }
        });

        //BUTTON 7
        button7.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("7");
                    sCode = "*";
                    sNum = "7";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "7";
                    if(sNum.matches("123456")){
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "7");
                }
            }
        });

        //BUTTON 8
        button8.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("8");
                    sCode = "*";
                    sNum = "8";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "8";
                    if(sNum.matches("123456")){
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "8");
                }
            }
        });

        //BUTTON 9
        button9.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("9");
                    sCode = "*";
                    sNum = "9";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "1";
                    if(sNum.matches("123456")){
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "9");
                }
            }
        });

        //CLEAR button
        //Sets both code and display string to empty
        button10.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                    editText.setText("");
                    editText2.setText("");
                    editText3.setText("");
            }
        });

        //BUTTON 0
        button11.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();

                if (sCode.matches("") || sCode.matches("Doors Unlocked!") || sCode.matches("Wrong Password")){
                    editText3.setText("");
                    editText.setText("*");
                    editText2.setText("0");
                    sCode = "*";
                    sNum = "0";
                }
                else if (sCode.matches("\\* \\* \\* \\* \\*")){
                    sNum = sNum + "0";
                    if(sNum.matches("123456")){
                        editText.setText("");
                        editText3.setText("Doors Unlocked!");
                    }
                    else{
                        editText.setText("");
                        editText3.setText("Wrong Password");
                    }
                }
                else {
                    editText.setText(sCode + " *");
                    editText2.setText(sNum + "0");
                }
            }
        });

        //Backspace Button
        button12.setOnClickListener(new OnClickListener() {
            public void onClick(View arg0) {
                String sCode = editText.getText().toString();
                String sNum = editText2.getText().toString();
                int codeLen = sCode.length();
                int numLen = sNum.length();
                StringBuilder myCode = new StringBuilder(sCode);

                //checks for empty string
                if(codeLen != 0) {
                    if (codeLen == 1) {
                        codeLen -= 1;
                        myCode.deleteCharAt(codeLen);
                    } else {
                        codeLen -= 1;
                        myCode.deleteCharAt(codeLen);
                        codeLen -= 1;
                        myCode.deleteCharAt(codeLen);
                    }


                    StringBuilder myNum = new StringBuilder(sNum);
                    numLen -= 1;
                    myNum.deleteCharAt(numLen);

                    //sets newly modified text as string
                    editText.setText(myCode.toString());
                    editText2.setText(myNum.toString());
                }
            }
        });


    }

}
