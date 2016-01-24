import urllib2
import json
import webbrowser
from VideoObject import VideoObject


def youtube_searcher(base_url, search_query, youtube_key, video_object):
    search_query = search_query.replace(' ', '%20')  # Accounting for multi-word queries
    query_key = 'q=' + search_query
    api_key = 'key=' + youtube_key

    # Now the Final url is Built
    final_url = base_url + '&' + query_key + '&' + api_key

    # Now Fetch the URL using urllib2 module
    response = urllib2.urlopen(final_url)
    actual_response = response.read()

    json_file = open('C:\Users\kalkurs\PycharmProjects\untitled\Youtube.json', 'w')
    json_file.write(actual_response)
    json_file.close()

    # Now print in json format
    # json.dumps did not accept the input in file format
    json_format = json.loads(actual_response)
    video_built = video_object.video_build(json_format)
    return video_built


def youtube_embed(base_url, video_id, youtube_key, video_object):
    part_string = 'part=snippet,contentDetails,statistics,status,player,topicDetails'
    video_identity = 'id=' + video_id
    api_key = 'key=' + youtube_key
    final_url = base_url + '?' + video_identity + '&' + api_key + '&' + part_string

    response = urllib2.urlopen(final_url)
    actual_response = response.read()

    json_file = open('C:\Users\kalkurs\PycharmProjects\untitled\VideoStat.json', 'w')
    json_file.write(actual_response)
    json_file.close()

    # Now print in json format
    # json.dumps did not accept the input in file format
    # read about __init__.py and docString in the class
    json_format = json.loads(actual_response)
    frame = video_object.video_framed(json_format)
    # Modification of iframe tag as din't have http in src URl
    frame.video_frame = frame.video_frame.replace("src=\"//", "src=\"https://")
    return frame


def html_modifier(file_path, video_object):
    with open(file_path, 'r') as html_file:
        text = html_file.read()
        text = text.replace("placehere", video_object.video_frame)
    html_file = open(path, 'w')
    html_file.write(text)

if __name__ == "__main__":
    print "========================================="
    print "Obtain Video Data related to Search Query"
    print "========================================="

    searchQuery = raw_input("\n Enter the Item to search on Youtube \n")
    youtubeAPIKey = 'XXXXXXX'  # API key
    video = VideoObject()
    print "Your search item is " + searchQuery + '\n'

    baseUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&field=item&type=video'
    videoUrl = youtube_searcher(baseUrl, searchQuery, youtubeAPIKey, video)
    print "The video being played is " + videoUrl.video_title + '\n'

    baseUrl = 'https://www.googleapis.com/youtube/v3/videos'
    videoFrame = youtube_embed(baseUrl, videoUrl.video_id, youtubeAPIKey, videoUrl)
    print "The iframe of the video is\n " + videoFrame.video_frame + '\n'

    path ='C:\Users\kalkurs\PycharmProjects\untitled\MagicRecommender.html'
    html_modifier(path, videoFrame)

    webbrowser.open(path, new=0, autoraise=True)
