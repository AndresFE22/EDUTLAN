from flask import Flask, send_file, request, Blueprint
from proyectosflask.diccionarioelectronico import diccionarioElectronico
from proyectosflask.diccionariokogui import diccionarioKogui

app = Flask(__name__, static_folder='./staticP')

sub_app_diccionarioelectronico = diccionarioElectronico()
sub_app_diccionariokogui = diccionarioKogui()

def select_subapp(request):
    path = request.path
    if path.startswith('/diccionarioelectronico'):
        return sub_app_diccionarioelectronico
    elif path.startswith('/diccionariokogui'):
        return sub_app_diccionariokogui
    else:
        return None

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/<path:path>')
def dynamic_routing(path):
    sub_app = select_subapp(request)
    if sub_app:
        with app.test_request_context(request.path):
            return sub_app.dispatch_request()
    else:
        return "404 - Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)
