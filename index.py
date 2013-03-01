#-*- coding:utf-8 -*-
import web
import model
import os

urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete'
)

app_root = os.path.dirname(__file__)
template_root = os.path.join(app_root, 'templates/')
render = web.template.render(template_root)

class Index:
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, description="I need to:"),
        web.form.Button('Add todo'),
    )
  
    def GET(self):
        todos = model.get_todos()
        form = self.form()
        return render.index(todos, form)

    def POST(self):
        form = self.form()
        if not form.validates():
            todos = model.get_todos()
            return render.index(todos, form)
        model.new_todo(form.d.title)
        raise web.seeother('/')
		
class Delete:
    def POST(self, id):
	id = int(id)
        model.del_todo(id)
        raise web.seeother('/')

app = web.application(urls, globals()).wsgifunc()
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
