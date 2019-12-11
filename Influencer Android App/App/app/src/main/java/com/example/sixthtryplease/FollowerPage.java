package com.example.sixthtryplease;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.SystemClock;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.RadioButton;
import android.widget.TextView;

import com.github.mikephil.charting.charts.BarChart;
import com.squareup.picasso.Picasso;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;


public class FollowerPage extends AppCompatActivity {
    //GLOBAL VARIABLES
    RadioButton cluster,bar;
    ImageView img;
    BarChart mybargraph;
    ArrayList numRetweets, numRetweetsweek, months,week;
    Socket client;
    BufferedReader in = null;
    PrintWriter os = null;
    String[] temparray = new String[20];
    String[] sixmonths = new String[6];
    float[] sixlikes = new float[6];
    float[] weeklikes =new float[4];
    String[] weeks = new String[4];
    Button graph;
    String url;
    String data;
    String top;
    TextView topfollower;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_follower_page);

        //MAP BUTTONS TO IDS and INITIALIZE GRAPH OBJECTS
        cluster=(RadioButton)findViewById(R.id.barOpt);
        bar=(RadioButton)findViewById(R.id.clusterOpt);
        img= (ImageView)findViewById(R.id.followerChart);
        topfollower = (TextView)findViewById(R.id.topfol);
        Intent intent = getIntent();
        String username = intent.getStringExtra("USER_NAME");
        getGraphValues(username);

        //USING THE URL OBTAINED FROM THE THREAD LOAD IT INTO THE PICTURE
        SystemClock.sleep(3000);
        Picasso.get().load(url).into(img);
        topfollower.setText("Your top follower is " + top);
    }



    public void selectOption1(View view) {
        Picasso.get().load("https://s18287.pcdn.co/wp-content/uploads/2018/03/Fake-Chart-3.jpg").into(img);

    }

    public void selectOption2(View view) {
        Picasso.get().load("https://opendatascience.com/wp-content/uploads/2017/02/fakestwords.png").into(img);
    }

    //THREAD FOR SENDING COMMAND TO SERVER AND RECEIVING VALUES
    public void getGraphValues(final String username){
        Runnable runnable = new Runnable() {
            public void run() {
                try {
                    System.out.println(username);
                    //CHANGE IP ADDRESS AND PORT TO WHERE THE SERVER IS LOCATED
                    client = new Socket("192.168.0.16", 9000);

                    //Create Input Stream
                    os = new PrintWriter(client.getOutputStream());
                    in = new BufferedReader(new InputStreamReader(client.getInputStream()));
                    //SEND THE COMMAND AND USERNAME TO THE SERVER
                    os.write("followers");
                    os.write(" ");
                    os.write(username);
                    os.write(" ");

                    os.flush();

                    //READ THE SERVER BYTE STREAM AS A STRING
                    data = in.readLine();
                    temparray =  data.split(" ");

                    url = temparray[0];
                    top = temparray[1]
;


                    os.close();
                    client.close();




                }catch(Exception e){

                    e.printStackTrace();
                }


            }
        };
        //START THE THREAD
        Thread mythread = new Thread(runnable);
        mythread.start();


    }
}
