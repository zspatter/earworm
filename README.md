# earworms
A program designed to send catchy lyrics in an attempt to get the song stuck in the recipient's head.

This script chooses a random song from a predefined library of earworms. Once the song is chosen, the link to the song's page on [genius.com](https://genius.com/) is gathered. This link is then shortened using bit.ly, and finally the earworm and link are combined into a single message and sent over SMS via a twilio client. 

## Sample Earworm Message
<p align=center>
  <img src=./sample_message.jpeg alt=sample earworm message height=750>
</p>
