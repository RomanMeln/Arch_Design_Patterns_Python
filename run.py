from melka_framework.main import Framework
from urls import routes, fronts
from wsgiref.simple_server import make_server

application = Framework(routes, fronts)

with make_server('', 8050, application) as httpd:
    print("Запуск на порту 8050...")
    httpd.serve_forever()
