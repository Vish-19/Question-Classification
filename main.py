from flask import Flask, render_template, request
from forms import Query
from Processors import lemmatize, preprocess
from driver import results
import fasttext as ft
app = Flask(__name__)
app.config["SECRET_KEY"] = "abc"

@app.route("/", methods = ["POST", "GET"])
def home():
    form = Query()
    if(form.is_submitted()):
        responses = request.form
        question = list(responses.values())[0]
        q = question
        question = lemmatize(preprocess(question))
        model1 = ft.load_model("./Datasets/Model_C1")
        model2 = ft.load_model("./Datasets/Model_C2")
        r1 = model1.predict(question)
        r2 = model2.predict(question)
        r1 = str(list(r1)[0][0]).replace("__label__", "")
        r2 = str(list(r2)[0][0]).replace("__label__", "")
        if r1 == "HUMAN" and r2 == "ind":
            r = results(q)
            return render_template("home.html", response=question, form=form, r=r)
        return render_template("home.html", response=question, form=form, r=r1)
    return render_template("home.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)