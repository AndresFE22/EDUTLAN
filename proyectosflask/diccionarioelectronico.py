from flask import Blueprint, render_template

def diccionarioElectronico():
    app = Blueprint('diccionarioelectronico', __name__,
                    static_folder='../proyectos/diccionarioelectronico/dist/static',
                    template_folder='../proyectos/diccionarioelectronico/dist')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def dictelect(path):
        return render_template('index.html')

    return app
