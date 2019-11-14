package com.example.kloutapp;

import android.os.AsyncTask;

import java.io.DataOutputStream;
import java.io.PrintWriter;
import java.net.Socket;

public class ConnectServer extends AsyncTask<String,Void,Void> {

    Socket s;
    DataOutputStream dos;
    PrintWriter pw;

    @Override
    protected Void doInBackground(String... voids) {
        String message = voids[0];

        try {

            s = new Socket("192.197.54.35", 9000);
            pw = new PrintWriter(s.getOutputStream());
            pw.flush();
            pw.close();
            s.close();

        }catch(Exception e){
            e.printStackTrace();
        }

        return null;
    }
}
