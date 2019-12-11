package com.example.sixthtryplease;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class RecoverAcc extends AppCompatActivity {
    EditText myemail;
    int valid =1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recover_acc);
        myemail = (EditText) findViewById(R.id.enteredEm);
    }

    public void retriAccFun(View view) {

        String theEmail = myemail.getText().toString();
        //send email to server to validate
        if (valid==1){
            Toast.makeText(getApplicationContext(),"Check your email to recover, your password",Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(getApplicationContext(),"Account doesn't exist",Toast.LENGTH_SHORT).show();
        }



    }

    public void gotoLogin(View view) {
        Intent intent = new Intent(this,MainActivity.class);
        startActivity(intent);

    }


}