# Import required libraries.
from youtube_transcript_api import YouTubeTranscriptApi

# Assigning srt variable with the list of dictonaries obtained by the get_transcript() function.
srt = YouTubeTranscriptApi.get_transcript("video_id")

# Open a txt file and join list of dictionaries, adding a space between each list. 
list_end = len(srt)
counter = 0
with open('transcript.txt' , 'w') as f:
	while counter < list_end:
		f.write(srt[counter]['text']+ " ")
		counter += 1
