
from .widgets import LoginPage, SearchPage


class Bot(object):
    def __init__(self, session, retries = 1):
        self.session = session
        self.retries = 1
        self.__offset = 0
        self.__pins = []

    @property
    def login_page(self):
        return LoginPage(self.session)

    @property
    def search_page(self):
        return SearchPage(self.session)

    def authenticate(self, username, password):
        lp = self.login_page
        self.session.get(lp.url)
        lp.authenticate(username, password)
        return self

    def search_for(self, *terms):
        sp = self.search_page
        sp.search_for(*terms)
        return self

    def quit(self):
        self.session.quit()

    def next(self):
        for i in xrange(self.retries + 1):
            if self.__pins:
                break
            else:
                self.search_page.load_more_pins()
                self.__pins = self.search_page.get_pins(offset=self.__offset)
                self.__offset += len(self.__pins)
        else:
            raise StopIteration("No more pins after %i retries" % (self.retries, ))

        return self.__pins.pop(0)

    def __iter__(self):
        return self
