#Use webscraping to get the url of a youtube video by just typing the name

import re, requests, subprocess, urllib.parse, urllib.request

def ytlink(video_name):
    
    music_name = video_name
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    print(clip2)
ytlink("Never gonna give you up")
