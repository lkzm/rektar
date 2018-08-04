



class NavMenu():

    title="Title"
    selected=False
    URL='/room"'
    def __init__(self, title, url, bol):
        self.title=title
        self.URL=url
        self.selected=False
    @property
    def html(self):

        if (self.selected==False):
            return "<a href="+self.URL+">"+self.title+"</a>"
        else:
            return "<a href="+self.URL+">"+self.title+"</a>"
