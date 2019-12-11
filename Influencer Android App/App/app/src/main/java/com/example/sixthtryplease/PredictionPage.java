package com.example.sixthtryplease;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.SystemClock;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.math.RoundingMode;
import java.text.DecimalFormat;

public class PredictionPage extends AppCompatActivity {

    TextView followerCurrent, followerPredict, retweetCurrent, blob;
    Socket client;
    BufferedReader in = null;
    PrintWriter os = null;
    String user_name;
    String[] temparray = new String[6];
    float one,two,three,four,five;

    private static DecimalFormat df = new DecimalFormat("0.00");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_prediction_page);

        blob = (TextView)findViewById(R.id.textView8);


        Intent intent = getIntent();
        user_name = intent.getStringExtra("USER_NAME");


        getGraphValues(user_name);
        SystemClock.sleep(2000);

        blob.setText("You have tweeted " + df.format(one) + " times this month with an average of " + df.format(two)  + " retweet and " + df.format(three) + " likes. if you were to tweet 5 times in the next month you will get approximately " + df.format(four)  + " retweets and " + df.format(five)  + " likes");
    }

    public void gotoSetGoalsPages(View view) {
        //Intent intent = new Intent(this, SetGoalsPage.class);
        //startActivity(intent);
    }

    public void getGraphValues(final String username){
        Runnable runnable = new Runnable() {
            public void run() {
                try {
                    System.out.println(username);
                    client = new Socket("192.168.0.16", 9000);

                    //Create Input Stream
                    os = new PrintWriter(client.getOutputStream());
                    in = new BufferedReader(new InputStreamReader(client.getInputStream()));
                    os.write("prediction");
                    os.write(" ");
                    os.write(username);
                    os.write(" ");

                    os.flush();



                    String data = in.readLine();
                    temparray =  data.split(" ");


                    for(int i = 0; i < temparray.length; i++){
                        System.out.println("Prediction " + temparray[i]);
                    }

                    one = Float.parseFloat((temparray[1]));
                    two = Float.parseFloat((temparray[2]));
                    three = Float.parseFloat((temparray[3]));
                    four = Float.parseFloat((temparray[4]));
                    five = Float.parseFloat((temparray[5]));




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
