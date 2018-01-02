SpotifyPlaylist
===============

Introduction
------------
This code is the result of an assignment given from an interview 


Explanation of the task
--------------------------
The task is to write a program that builds a playlist of Spotify tracks such that it looks like a
message, inspired by various people on the internet doing this thing.

We discussed this a bit and realized this can be done automatically using our metadata API
which is accessible at http://developer.spotify.com/en/metadata-api/overview/

So, your task will be to implement a Python application doing this. You can read the input in
any way you want (command line arguments, run it as a web server and take a query string,
etc). Feel free to use any Python modules or frameworks that are reasonably standard.
The input to the application will be the message, and its output will be a list of Spotify tracks,
i.e. if the input is "if i can't let it go out of my mind", one valid output would be:
! http://open.spotify.com/track/6mcu7D7QuABVwUGDwovOEh
! http://open.spotify.com/track/5ZRxxnab9kLUqZPzoelgGP
! http://open.spotify.com/track/3L0bYyI0FHRiD1xZfbZedz
(this is the beginning of one of the poems on the blog).

To be clear the output should be a playlist that reads out the original text. For instance:
![alt text](https://github.com/luchetto/SpotifyPlaylist/blob/master/playlist_image.png)



Explanation of the code
------------------------

The code receive a message in input and then it tries to build a playlist as similar as possible to the message.

- Capitalization should not matter. The input message can be lower or upper case.
- The code should work for any UTF-8 string
- The code should find the "optimal" solution in terms of unmatched words
- The code should find the "optimal" solution in terms of length of playlist 


How to run the program
----------------------

- Clone or download this repository 
- ``` >> python Playlist_from_text.py```
