import re

class Get_Email(object):
    def __init__(self):
        self.__EMAIL_REGEX = r"""[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"""
        self.__Emails = []

    def Search_Email(self, _HTML):
        try:
            # Finding all tags in HTML
            for Email in _HTML.find_all():
                # True if the string matches this type EmailName@DomainName
                if bool(re.match(self.__EMAIL_REGEX, Email.text)):
                    # Add Email to List
                    # self.__Emails.append(Email.text +"\n")
                    # My code for excel
                    # print(Email.text)
                    self.__Emails = Email.text 
        except Exception:
            pass