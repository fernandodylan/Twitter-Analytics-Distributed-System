package com.example.sixthtryplease;

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

public class MainActivity extends AppCompatActivity {

    EditText username_edit, password_edit;
    Button login_button;
    Socket client;
    BufferedReader in = null;
    PrintWriter os = null;
    private Toast toast, toast2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        username_edit=(EditText)findViewById(R.id.myusernameOnMain);
        password_edit=(EditText)findViewById(R.id.password);
        login_button=(Button)findViewById(R.id.loginmine);
        toast = Toast.makeText(this, "Incorrect Username", Toast.LENGTH_LONG);
        toast2 = Toast.makeText(this, "Incorrect Password", Toast.LENGTH_LONG);


    }



    public void recoverAccount(View view) {

        Intent intent = new Intent(this,RecoverAcc.class);
        startActivity(intent);


    }

    public void SignUpNow(View view) {
        Intent intent = new Intent(this,registerAcc.class);
        startActivity(intent);

    }

    public void logOnNow(View view) {
        if(username_edit.getText().toString().equals("") || password_edit.getText().toString().equals("")){
            Toast.makeText(this, "Please fill out both fields", Toast.LENGTH_LONG).show();

        }

        Runnable runnable = new Runnable() {
            public void run() {
                try {
                    System.out.println("Hello");
                    client = new Socket("192.168.0.16", 9000);

                    //Create Input Stream
                    os = new PrintWriter(client.getOutputStream());
                    in = new BufferedReader(new InputStreamReader(client.getInputStream()));
                    os.write("login");
                    os.write(" ");
                    os.write(username_edit.getText().toString());
                    os.write(" ");
                    os.write(password_edit.getText().toString());
                    os.flush();



                    String received = in.readLine();
                    System.out.println("Message Received " + received);

                    if(received.equals("Verified")){
                        Intent mainintent = new Intent(MainActivity.this, FakeDashboardPage.class);
                        mainintent.putExtra("username",username_edit.getText().toString() );
                        startActivityForResult(mainintent,100);

                    }
                    if(received.equals("Denied")){
                        toast2.show();

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
