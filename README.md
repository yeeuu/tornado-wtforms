# tornado-wtforms
Package tornado-wtforms is a helper to add wtforms support into tornado web framework.

Work from [wtforms-tornado](https://github.com/puentesarrin/wtforms-tornado)

Usage
===

```
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
```

Installation
===

You can to use pip to install from last source:

    $ pip install git+git://github.com/yeeuu/tornado-wtforms.git
