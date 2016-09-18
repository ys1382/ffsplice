# ffsplice
Removes sections from a video

I wanted to remove the naughty bits from all the episodes of a TV show for my kids, so I made this. It requires ffmpeg. To run:

python ffsplice.py input bit1 bit2 ...

For example:

python ffsplice.py tvshowwithdragonsand80085.mkv 17:55-24:18 46:03-50:00

will remove the bit from 17:55 to 24:18, and from 46:03 to 50:00, so the output will be several minutes shorter. The output will be in a file called cut_tvshowwithdragonsand8008s.mkv
