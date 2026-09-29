from flask import Flask, abort, render_template, send_from_directory

app = Flask(__name__, template_folder="Template", static_folder="Static", static_url_path="/assets")

HTML_PAGES = {"portfolio-details.html", "service-details.html", "starter-page.html"}

@app.route("/index.html")
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/<path:page>")
def html_page(page):
    if page not in HTML_PAGES:
        abort(404)
    return send_from_directory(app.root_path, page)

if __name__ == '__main__':
    app.run(debug=True)