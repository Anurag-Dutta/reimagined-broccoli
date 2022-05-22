package com.example.tic_tac_toe;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    // Player Representation
    // X -> 0
    // O -> 1
    int active_player = 0;
    int [] gamestates = {2, 2, 2, 2, 2, 2, 2, 2, 2};
    // State Meaning
    // 0 -> Filled by X
    // 1 -> Filled by O
    // 2 -> Filled by NULL / is blank
    int[][] winpositions = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                            {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
                            {0, 4, 8}, {2, 4, 6}}; // Winning Positions
    boolean gameActive = true;
    public void playertap(View view)
    {
        ImageView img = (ImageView) view;
        int tappedImage = Integer.parseInt(img.getTag().toString()); // Convert the tag of each state to integer
        if(!gameActive)
        {
            gameReset(view);
        }
        if(gamestates[tappedImage] == 2)
        {
            gamestates[tappedImage] = active_player;
            // img.setTranslationX(-1000f); // Can be used for animation
            if(active_player == 0)
            {
                img.setImageResource(R.drawable.x);
                active_player = 1;
                TextView status = findViewById(R.id.status);
                status.setText("O's Turn - Tap to play");
            }
            else
            {
                img.setImageResource(R.drawable.o);
                active_player = 0;
                TextView status = findViewById(R.id.status);
                status.setText("X's Turn - Tap to play");
            }
            // img.animate().translationXBy(1000f).setDuration(300); // Can be used for animation
        }
        String winner = null;
        for(int[] winPosition: winpositions) // winPosition is the iterator
        {
            if(gamestates[winPosition[0]] == gamestates[winPosition[1]] &&
                    gamestates[winPosition[1]] == gamestates[winPosition[2]] &&
                    gamestates[winPosition[0]] != 2)
            {
                // Some Player have won the game
                if(gamestates[winPosition[0]] == 0)
                {
                    winner = "Hurray!, X have won";
                    gameActive = false;
                }
                else if(gamestates[winPosition[0]] == 1)
                {
                    winner = "Hurray!, O have won";
                    gameActive = false;
                }
                TextView status = findViewById(R.id.status);
                status.setText(winner);
            }
        }
        int blanks = 0;
        for(int i = 0; i < gamestates.length; i++)
        {
            if(gamestates[i] == 2)
            {
                blanks++;
                break;
            }
        }
        if(blanks == 0)
        {
            gameActive = false;
            TextView status = findViewById(R.id.status);
            status.setText("Draw");
        }
    }
    public void gameReset(View view)
    {
        gameActive = true;
        for(int i = 0; i < gamestates.length; i++)
        {
            gamestates[i] = 2;
        }
        // Resetting the 9 squares
        ((ImageView)findViewById(R.id.imageView0)).setImageResource(0);
        ((ImageView)findViewById(R.id.imageView1)).setImageResource(0);
        ((ImageView)findViewById(R.id.imageView2)).setImageResource(0);
        ((ImageView)findViewById(R.id.imageView3)).setImageResource(0);
        ((ImageView)findViewById(R.id.imageView4)).setImageResource(0);
        ((ImageView)findViewById(R.id.imageView5)).setImageResource(0);
        ((ImageView)findViewById(R.id.imageView6)).setImageResource(0);
        ((ImageView)findViewById(R.id.imageView7)).setImageResource(0);
        ((ImageView)findViewById(R.id.imageView8)).setImageResource(0);

        TextView status = findViewById(R.id.status);
        status.setText("X's Turn - Tap to play");
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}