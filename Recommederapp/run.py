
import os

from app import create_app

#config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    print (app.root_path)
