"""

Implement a web browser with the following methods:

WebBrowser(String homepage) constructs a new instance
of the browser with starting page of homepage.

visit(String page) visits the site page, clearing
all forward history.

back(int n) goes back n number of steps in history and
returns the current page. Note that once you reach the homepage,
you stay on that page even if you go back.

forward(int n) goes forward n number of steps in history and
returns the current page. Note that once you reach the most recent page,
you stay on that page even if you go forward.

Constraints
n ≤ 100,000 where n is the number of calls to visit, back and forward.

"""


class WebBrowser:
    def __init__(self, homepage):
        self.pages = [homepage]
        self.index = 0

    def visit(self, page):
        self.index += 1
        self.pages = self.pages[:self.index]
        self.pages.append(page)
        return

    def back(self, n):
        if self.index - n < 0:
            self.index = 0
            return self.pages[0]
        else:
            self.index -= n
            return self.pages[self.index]

    def forward(self, n):
        if self.index + n > len(self.pages) - 1:
            self.index = len(self.pages) - 1
            return self.pages[-1]
        else:
            self.index += n
            return self.pages[self.index]


browser = WebBrowser("wikipedia.org")
browser.visit("google.com")
browser.visit("stackoverflow.com")
browser.visit("github.com")

assert browser.back(2) == "google.com"
assert browser.forward(1) == "stackoverflow.com"
