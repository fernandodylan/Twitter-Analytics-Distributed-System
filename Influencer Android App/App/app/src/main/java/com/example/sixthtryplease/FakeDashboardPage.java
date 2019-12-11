package com.example.sixthtryplease;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class FakeDashboardPage extends AppCompatActivity {

    TextView user_name2;
    String user_name;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_fake_dashboard_page);
        user_name2=(TextView)findViewById(R.id.titleUserName);


        /////////////////////////////////////////////////////
        Intent intent = getIntent();
        user_name = intent.getStringExtra("username");

        ///////////////////////////////////////////

        user_name2.setText(user_name);

        System.out.println(user_name);

    }

    //CALL INTENTS TO EACH PAGE FROM THE DASHBOARD PAGE PASSING THEM THE USERNAME
    public void gotoPredPage(View view) {
        Intent intent = new Intent(this, PredictionPage.class);
        intent.putExtra("USER_NAME", user_name);
        startActivity(intent);
    }

    public void gotoFollowPage(View view) {
        Intent intent = new Intent(this, FollowerPage.class);
        intent.putExtra("USER_NAME", user_name);
        startActivity(intent);
    }

    public void likesPerMonthPage(View view) {
        Intent intent = new Intent(this, LikesPerM.class);
        intent.putExtra("USER_NAME", user_name);
        startActivity(intent);
    }

    public void likesPerWeekPage(View view) {
        Intent intent = new Intent(this, LikesPerW.class);
        intent.putExtra("USER_NAME", user_name);
        startActivity(intent);
    }

    public void retweetPerMonthPage(View view) {
        Intent intent = new Intent(this, retweetPerM.class);
        intent.putExtra("USER_NAME", user_name);
        startActivity(intent);
    }

    public void retweetPerWeek(View view) {
        Intent intent = new Intent(this, retweetPerW.class);
        intent.putExtra("USER_NAME", user_name);
        startActivity(intent);
    }
}
