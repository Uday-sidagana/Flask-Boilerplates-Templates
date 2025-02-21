from app import app
from extra_pages import extra


app.register_blueprint(extra)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50000, debug=True)

