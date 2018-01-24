import tornado.ioloop
import tornado.web
import os

PORT = int(os.getenv("PORT", 8080))

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("<h1>Python</h1> Running Tornado")

application = tornado.web.Application([
  (r"/", MainHandler),
])

if __name__ == "__main__":
  application.listen(PORT)
  print("server runninng on http://localhost:" + str(PORT))
  tornado.ioloop.IOLoop.instance().start()
