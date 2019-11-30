package com.example.influencecalculatorapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Main2Activity extends AppCompatActivity {

    Button login_button;
    EditText username_edit, password_edit;
    Socket client;
    BufferedReader in = null;
    PrintWriter os = null;
    private Toast toast, toast2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        login_button = (Button) findViewById(R.id.btnlogin);
        username_edit = (EditText) findViewById(R.id.usernametxt);
        password_edit = (EditText) findViewById(R.id.passwordtxt);
        toast = Toast.makeText(this, "Username already in use", Toast.LENGTH_LONG);
    }


    public void logIn(View v) {

        if(username_edit.getText().toString().equals("") || password_edit.getText().toString().equals("")){
            Toast.makeText(this, "Please fill out both fields", Toast.LENGTH_LONG).show();

        }

        Runnable runnable = new Runnable() {
            public void run() {
                try {
                    System.out.println("Does it get here");
                    client = new Socket("10.160.4.158", 9000);

                    //Create Input Stream
                    os = new PrintWriter(client.getOutputStream());
                    in = new BufferedReader(new InputStreamReader(client.getInputStream()));
                    os.write("register");
                    os.write(" ");
                    os.write(username_edit.getText().toString());
                    os.write(" ");
                    os.write(password_edit.getText().toString());
                    os.flush();



                    String received = in.readLine();
                    System.out.println("Message Received " + received);

                    if(received.equals("Verified")){
                        Intent mainintent = new Intent(Main2Activity.this, HomePage.class);
                        startActivity(mainintent);

                    }
                    if(received.equals("Denied2")){
                        toast.show();


                    }



                    os.close();
                    client.close();




                }catch(Exception e){
                    e.printStackTrace();
                }


            }
        };
        Thread mythread = new Thread(runnable);
        mythread.start();


    }
}
