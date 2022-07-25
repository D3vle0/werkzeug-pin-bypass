from flask import Flask, render_template, request, session, escape, redirect, url_for

app = Flask(__name__, static_url_path='/static')
app.config.update(
    DEBUG=True
)

@app.route('/', methods=["GET"])
def hello_world():
    page = request.args.get('page')
    if not page:
        f = open('./index.html', 'r')
    else:
        try:
            path = "./" + page
            f = open(path, 'r')
        except Exception as e:
            return "<h1>" + str(e) + "</h1>"
    return "</br>".join(f.readlines())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)