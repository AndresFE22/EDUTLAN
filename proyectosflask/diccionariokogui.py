from flask import Blueprint, render_template

def diccionarioKogui():
    app = Blueprint('diccionariokogui', __name__,
                    static_folder='../proyectos/diccionariokogui/dist/static_',
                    template_folder='../proyectos/diccionariokogui/dist')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def dictkogui(path):
        return render_template('index.html')

    return app