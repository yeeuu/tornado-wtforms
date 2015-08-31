import os
import sys
my_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(my_dir, '..')))

import tornado.ioloop
import tornado.web

from wtforms.fields import IntegerField
from wtforms.validators import InputRequired
from tornado_wtforms import Form

class SumForm(Form):
    a = IntegerField(validators=[InputRequired()])
    b = IntegerField(validators=[InputRequired()])

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        form = SumForm(self)
        if form.validate():
            self.write(str(form.data['a'] + form.data['b']))
        else:
            self.set_status(400)
            self.write("" % form.errors)

application = tornado.web.Application([
    (r"/", IndexHandler),
])

if __name__ == "__main__":
    application.listen(10240)
    tornado.ioloop.IOLoop.instance().start()
