from mysite.application import app
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URL"] = os.environ["DATABASE_URL"]
# conn().execute("INSERT INTO text(id,name) VALUES (1,'22too')")


if __name__ == '__main__':
    app.run(debug=True)
