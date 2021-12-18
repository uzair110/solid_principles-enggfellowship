class Post:
    def __init__(self, user, text):
        self.user = user
        self.text = text
    
    def postOnWeb(self):
        if self.isPicture:
            return (self.user, self.text, self.picture)
        
        if self.isVideo:
            return (self.user, self.text, self.video)
        
        return (self.user, self.text)

        #The code has to be modified at new extention