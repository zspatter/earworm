# earworms
This program is designed to send catchy lyrics in an attempt to get songs stuck in the recipient's head.

This script chooses a random song from a predefined library of [earworms](https://en.wikipedia.org/wiki/Earworm). Once the song is chosen, the link to the song's lyrics page on [Genius](https://genius.com/) is gathered. This link is then shortened using [Bitly](https://bitly.com/), and finally the earworm and the shortened link are combined into a single message which is then sent over SMS via a [Twilio](https://www.twilio.com/) client. 

## Sample Earworm Message
<p align=center>
  <img src=./sample_message.jpeg alt=sample earworm message height=750>
</p>
