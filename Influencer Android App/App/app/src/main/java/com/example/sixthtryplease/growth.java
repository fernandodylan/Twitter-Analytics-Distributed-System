package com.example.sixthtryplease;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;

import com.github.mikephil.charting.charts.BarChart;
import com.github.mikephil.charting.data.BarData;
import com.github.mikephil.charting.data.BarDataSet;
import com.github.mikephil.charting.data.BarEntry;
import com.github.mikephil.charting.interfaces.datasets.IBarDataSet;
import com.github.mikephil.charting.utils.ColorTemplate;

import java.util.ArrayList;

public class growth extends AppCompatActivity {

    BarChart mybargraph;
    ArrayList numRetweets, numRetweetsweek, months,week;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my_growth);

        //INITIALIZE THE GRAPH
        mybargraph = findViewById(R.id.bargraph);
        mybargraph.animateY(3000);
        numRetweets = new ArrayList();
        months = new ArrayList();
        //POPULATE THE GRAPH WITH ENTRIES FROM THE THREAD
        numRetweets.add(new BarEntry(20, 0));
        numRetweets.add(new BarEntry(30, 1));
        numRetweets.add(new BarEntry(3, 2));
        numRetweets.add(new BarEntry(92, 3));
        numRetweets.add(new BarEntry(22, 4));
        numRetweets.add(new BarEntry(14, 5));



        months.add("2008");
        months.add("2009");
        months.add("2010");
        months.add("2011");
        months.add("2012");
        months.add("2013");

        //BUILD THE GRAPH
        BarDataSet bardataset = new BarDataSet(numRetweets, "No of retweets");

        BarData data = new BarData(months, bardataset);
        bardataset.setColors(ColorTemplate.LIBERTY_COLORS);
        bardataset.setBarShadowColor(20);
        mybargraph.setData(data);
        mybargraph.setDescription("Number of retweets per month");




    }





}
