# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:03:01 2016

@author: Mark
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    playlist = []
    left_on_disk = max_size
    if songs[0][2] > left_on_disk:
        return []
    else:
        playlist.append(songs[0][0])
        left_on_disk -= songs[0][2]
        
    sorted_remaining_songs = list(songs[1:])
    sorted_remaining_songs.sort(key=lambda x: x[2], reverse = False)
    for song in sorted_remaining_songs:
        if song[2] <= left_on_disk:
            playlist.append(song[0])
            left_on_disk -= song[2]
    return playlist
    



    
        