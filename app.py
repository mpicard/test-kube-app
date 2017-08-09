from sanic import Sanic, response


app = Sanic()


@app.route("/")
async def root(request):
    return response.json({"hello": "kubernetes"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
