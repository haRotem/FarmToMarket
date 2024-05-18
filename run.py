from app.globals import Globals
from app.init import init_app

if __name__ == "__main__":
    init_app()
    Globals.app.run(debug=True, port=80, host='0.0.0.0')
