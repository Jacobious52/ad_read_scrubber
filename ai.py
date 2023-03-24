import yt_dlp as youtube_dl

# download only the subtitles from a youtube video


def download_subtitles(url):
    print('Downloading subtitles from: ' + url)
    ydl_opts = {
        'writesubtitles': True,
        'skip_download': True,
        'outtmpl': 'subtitles'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        return ydl.download([url])


print(download_subtitles('https://www.youtube.com/watch?v=nCrTsWtPVIY'))

# open the downloaded file into a string
with open('subtitles.en.vtt', 'r') as file:
    data = file.read()

# split the string into chunks of 1800 tokens, but don't split in the middle of a word
chunks = [data[i:i + 1800] for i in range(0, len(data), 1800)]
chunks = [chunk[:chunk.rfind(' ')] for chunk in chunks]

# write each chunk to a separate file
for i, chunk in enumerate(chunks):
    with open('subtitles_' + str(i) + '.txt', 'w') as file:
        # todo: prompt should be more strict with output format
        prompt = 'return in json format the start and end time of the ad read in this vtt formatted text below. if there is no ad read, return NONE\n\n'
        # append the prompt to the beginning of the chunk
        file.write(prompt + chunk)

# todo: for each file, do a post to chatgpt, parse the response and chop it from downloaded video
