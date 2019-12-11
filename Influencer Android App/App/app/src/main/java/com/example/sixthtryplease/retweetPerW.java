package com.example.sixthtryplease;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.SystemClock;
import android.widget.Button;
import android.widget.TextView;

import com.github.mikephil.charting.charts.BarChart;
import com.github.mikephil.charting.data.BarData;
import com.github.mikephil.charting.data.BarDataSet;
import com.github.mikephil.charting.data.BarEntry;
import com.github.mikephil.charting.utils.ColorTemplate;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;

public class retweetPerW extends AppCompatActivity {
    TextView user_name2;
    String user_name;
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

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_retweet_per_w);
        user_name2=(TextView)findViewById(R.id.titleUserName);


        /////////////////////////////////////////////////////
        Intent intent = getIntent();
        user_name = intent.getStringExtra("USER_NAME");

        ///////////////////////////////////////////

        user_name2.setText(user_name);

        mybargraph = findViewById(R.id.bargraph);
        mybargraph.animateY(3000);
        numRetweets = new ArrayList();
        months = new ArrayList();
        System.out.println("USERNAME " +user_name);
        getGraphValues(user_name);

        SystemClock.sleep(6000);

        numRetweets.add(new BarEntry(sixlikes[0], 0));
        numRetweets.add(new BarEntry(sixlikes[1], 1));
        numRetweets.add(new BarEntry(sixlikes[2], 2));
        numRetweets.add(new BarEntry(sixlikes[3], 3));


        months.add(sixmonths[0]);
        months.add(sixmonths[1]);
        months.add(sixmonths[2]);
        months.add(sixmonths[3]);





        BarDataSet bardataset = new BarDataSet(numRetweets, "No of Likes");

        BarData values = new BarData(months, bardataset);
        bardataset.setColors(ColorTemplate.LIBERTY_COLORS);
        bardataset.setBarShadowColor(20);
        mybargraph.setData(values);
        mybargraph.setDescription("Number of likes per month");
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
                    os.write("growth3");
                    os.write(" ");
                    os.write(username);
                    os.write(" ");

                    os.flush();



                    String data = in.readLine();
                    temparray =  data.split(" ");

                    for(int i = 0; i < temparray.length; i++){
                        System.out.println("Months " + temparray[i]);
                    }


                    sixmonths[0] = temparray[0];
                    sixmonths[1] = temparray[1];
                    sixmonths[2] = temparray[2];
                    sixmonths[3] = temparray[3];


                    sixlikes[0] = Float.parseFloat((temparray[4]));
                    sixlikes[1] = Float.parseFloat((temparray[5]));
                    sixlikes[2] = Float.parseFloat((temparray[6]));
                    sixlikes[3] = Float.parseFloat((temparray[7]));




                    for(int i = 0; i < sixmonths.length; i++){
                        System.out.println("Months " + sixmonths[i]);
                    }

                    for(int i = 0; i < sixlikes.length; i++){
                        System.out.println("Likes " + sixlikes[i]);
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
