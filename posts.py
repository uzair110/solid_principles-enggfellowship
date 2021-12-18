class Post:
    def __init__(self, user, text):
        self.user = user
        self.text = text
    
    def postOnWeb(self):
        return (self.user, self.text)


class PostWithPicture(Post):
    def __init__(self, user, text, picture):
        super.__init__(self, user, text)
        self.picture = picture
    
    def postOnWeb(self):
        return (self.user, self.text, self.picture)


class PostWithVideo(Post):
    def __init__(self, user, text, video):
        super.__init__(self, user, text)
        self.video = video
    
    def postOnWeb(self):
        return (self.user, self.text, self.video)





