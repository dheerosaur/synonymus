import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app, login_required
from google.appengine.ext import db

# main handler
class MainPage(webapp.RequestHandler):
    " Handler for the home-page etc. "
    def get(self):
        " Renders Home page "
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(webapp.template.render(path, {}))

application = webapp.WSGIApplication(
        [('/', MainPage),],
        debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
