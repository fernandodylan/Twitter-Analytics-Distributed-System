package com.example.kloutapp;

import androidx.appcompat.app.AppCompatActivity;


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;


public class MainActivity extends AppCompatActivity {

    Button connect;
    EditText response;
    TextView view;

    private Exception exception;
    private Socket socket;

    private static final int SERVERPORT = 9000;
    private static final String SERVER_IP = "99.244.233.24";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        response = (EditText) findViewById(R.id.editText);
        connect = (Button) findViewById(R.id.btnconn);

    }
    public void connectSocket(View v){
        ConnectServer connectServer = new ConnectServer();
        connectServer.execute(response.getText().toString());

    }
}


