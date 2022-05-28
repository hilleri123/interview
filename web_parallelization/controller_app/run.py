#!/usr/bin/python3


from app import make_app

from config import urls

if __name__ == "__main__":
    app = make_app(True)
    #app.run(debug=True, host='0.0.0.0')
    app1 = make_app(False, urls[0])
    app1.run(debug=True, host='localhost', port=5001)


