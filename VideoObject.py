class VideoObject:
    def __init__(self):
        self.video_type = "youtube"
        self.video_id = "none"
        self.video_title = "none"
        self.video_frame = "none"
        self.video_views = 'none'
        self.video_url = 'https://www.youtube.com/watch?v='

    def video_build(self, json_object):
        self.video_id = json_object["items"][0]["id"]["videoId"]
        self.video_title = json_object["items"][0]["snippet"]["title"]
        self.video_url = self.video_url + self.video_id
        return self

    def video_framed(self, json_object):
        self.video_frame = json_object["items"][0]["player"]["embedHtml"]
        self.video_views = json_object["items"][0]["statistics"]["viewCount"]
        return self
