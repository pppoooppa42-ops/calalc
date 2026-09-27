from flask import  Flask, render_template,request
app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def post():
    result = 0
    if request.method == 'POST':
        lvl = request.form.get('level', type=int)
        if lvl is not None and lvl != 0:
            result = (lvl * 80000) - 80000
    return render_template('index.html', result = result)

app.run(debug=True)