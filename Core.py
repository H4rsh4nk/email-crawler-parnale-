import requests

from Get_Links import Get_Links
from Get_Email import Get_Email
from bs4 import BeautifulSoup
from tqdm import tqdm

class Core(object):
    def __init__(self):
        self.__Get_Email = Get_Email()
        self.__Get_Links = Get_Links()
        self.__Emails = []

    def URL(self, _URL):
        try:
            # Search Links
            self.__Get_Links.Search_Links(_URL)

            print("\n>>> [" + _URL + "]")

            for Link in tqdm(set(self.__Get_Links._Get_Links__All_Links), desc=">>> "):
                # True if the link starts with HTTP or WWW
                if Link.startswith(("http", "www")):
                    # Get HTML
                    HTML = BeautifulSoup(requests.get(Link).text, "html.parser")

                    # Search Email
                    self.__Get_Email.Search_Email(HTML)
                else:
                    # Get HTML
                    HTML = BeautifulSoup(requests.get(_URL + Link).text, "html.parser")

                    # Search Email
                    self.__Get_Email.Search_Email(HTML)
            
            # My code for excel
            # print(_URL + " : " + self.__Get_Email._Get_Email__Emails)
            # Add Emails to List
            self.__Emails = (self.__Get_Email._Get_Email__Emails)
        except Exception:
            pass