from django.shortcuts import render


def home():
    return render("index.html")


if __name__ == "__main__":
    app.run()
    ip = '127.0.0.0'
    app.run(host=ip)