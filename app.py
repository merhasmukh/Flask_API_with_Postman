from flask import Flask


app=Flask(__name__)


@app.route("/",methods=["POST","GET"])
def main():
    return "hi"

if __name__=="__main__":
    main()
    app.run('0.0.0.0')