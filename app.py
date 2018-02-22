import cherrypy
import os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('html'))

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

    @cherrypy.expose
    def paid(self):
        tmpl = env.get_template('paid.html')
        return tmpl.render()
        
class DataView(object):
    exposed = True
    @cherrypy.tools.accept(media='application/json')
    @cherrypy.expose
    def seller(self):
        rawData = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))
        tmpl = env.get_template('seller.html')
        b = json.loads(rawData)
# do something with b, in this case I am returning it inside another object
        return json.dumps({'x': 4, 'c': b})
        return tmpl.render()

@cherrypy.expose
class SenderRoutes(object):
    def GET(self, sender_id):
        return dumps([r for r in records])

    @cherrypy.tools.accept(media='application/json')
    def POST(self, sender_id):
        raw = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))
        b = json.loads(raw)
        # read out start, end
        start = b["start"]
        assert "lat" in start
        assert "long" in start
        assert "id" in start
        end = b["end"]
        assert "lat" in end
        assert "long" in end
        assert "id" in end
        routes.insert_one({
            "start": start, "end": end, "sender": int(sender_id)
        })
        return dumps({"status": "ok"})


config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    },
    '/assets': {
        'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)),
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'assets',
    }
}

cherrypy.quickstart(HelloWorld(), '/', config=config)