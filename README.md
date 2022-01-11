I wrote this piece of code that automatically plays the "1to50" online game. The game is available at https://zzzscore.com/1to50/en/.
The game consists of 25 tiles with a number between 1 to 50 on them. The objective of the game is to click from 1 to 50 in increasing order as quickly as possible. The score is a stopwatch value in seconds, showing how long it took you to click from 1 through to 50.

Since there are only 25 tiles but the number go from 1 to 50, every tile changes its number once you click on it. So every tile eventually requires two clicks to be fully eliminated.

I used Selenium to automate this game play, completing the game in between 5-12 seconds. Manually, the game can take minutes to complete.
