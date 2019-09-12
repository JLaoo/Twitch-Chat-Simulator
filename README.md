# Twitch Simulator
Link to original repository: https://github.com/JLaoo/Twitch-Chat-Simulator
# Introduction
Here I attempt to simulate twitch chat by collecting a lot of chat messages and then using a neural net to predict chat messages.

# Notes
- The authorization token I'm using has been redacted. You can get your own by logging into your twitch account [here](https://twitchapps.com/tmi/).
- Trained model for ~9 days of CPU time. Logs can be seen in nohup.out. I think I overfitted but I also can't really think of any cons of overfitting in this case since my goal is to replicate a League of Legends Twitch stream.
- Model and data preparation algorithm taken from zackthoutt's Game of Thrones Book 6 generator found [here](https://github.com/zackthoutt/got-book-6).
# WIP
- Currently working on customizing the text generation from zackthoutt so that it's more in line with twitch messages as opposed to actual sentences in a book. Progress can be seen in generate_text.ipynb
- Will update README with detailed steps soon.
