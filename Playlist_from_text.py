import requests
import json
import string
from collections import OrderedDict

class MakePlaylist(object):

    def __init__(self, sentence):
        self.sentence = sentence
    
    def cleaning_data(self, sentence):
        """
        This method removes all the punctuation (except for ! and ?)from the input sentence. 
        It also makes everything lower case
        """
        sentence = "".join(c for c in sentence if c not in ('.', ',', ':', ';'))
        sentence = sentence.lower()
        return sentence    
    
    def split_sentence(self, sentence, start_point):
        """
        This method return a list of 10 words from a string
        sentence: string (string that is splitted) 
        start_point: int (starting point of the splitment) 
        """
        sentence_split=sentence.split()
        if len(sentence_split[start_point:])==0 :
            print ("No sentence")
            return None, False
        else:
            print ("Getting a sample")
            sentence_split = sentence_split[start_point:(start_point+10)]
            print (sentence_split)
            return sentence_split, True

    def get_song_from_sample(self, sentence_sample,headers, counter, number_of_song, printed=False):
        """
        This method get the song from Spotify list
        sentence_sample: list (The sentence from where to retrieve the song)
        counter: int. 
        printed: bool 
        """        
        while counter > 0:
            sentence_sample = sentence_sample[:counter]
            url=str('https://api.spotify.com/v1/search?q=%s&type=track' %' '.join(sentence_sample))
            try:
                r = requests.get(url, headers=headers)
                r.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print (err)
                sys.exit(1)
            song_object = json.loads(r.text)
            if len(song_object['tracks']['items']) == 0:
                print ('No song Found, reducing the sentence')
                counter -= 1
                continue
            if len(song_object['tracks']['items']) != 0:
                print ('Songs list Found from Spotify API. Looking for the exact song in the list')
                for track in song_object['tracks']['items']:
                    if track['name'].lower().split() == sentence_sample[:counter] and counter > 0:
                        print ('There is an exact song', track['name'])
                        printed = True
                        number_of_song += 1
                        return track['name'], track['href'][14:], number_of_song, counter 
                    else:
                        continue
            print ('No exact song found, reducing the sentence')
            counter -= 1
        if counter == 0:
           print ('No Match Found')
           counter = 1
           return None, None, number_of_song, counter       
 
def main():
    sentence = input('Insert your poem:  ')
    token = input('Insert your Auth Token. Go here https://developer.spotify.com/web-api/console/get-search-item/ to make one. You need a Spotify account \n')
    make_playlist = MakePlaylist(sentence)
    sentence = make_playlist.cleaning_data(sentence)
    print ('Processing the poem to retrieve a playlist')
    go_on=True
    start_point = 0
    number_of_song = 0
    playlist = {}
    headers = {
    'Accept': 'application/json',
    'Authorization': str('Bearer %s' %token),
}
    while go_on:
        sentence_list_sample, go_on = make_playlist.split_sentence(sentence, start_point)
        if sentence_list_sample:
            counter = len(sentence_list_sample)
            songs, song_keys, number_of_song, song_length = make_playlist.get_song_from_sample(sentence_list_sample, headers, counter, number_of_song)
            if song_keys and songs:
                  playlist[(number_of_song, songs)]= 'http://open.spotify.com/track/%s' %song_keys
            start_point = start_point + song_length
        else:
            break
    print ("The following is the retrieved playlist from your poem: ")
    print (OrderedDict(sorted(playlist.items(), key=lambda t: t[0])))

if __name__ == '__main__':
    main()
