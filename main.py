from joblib import load
from flask import Flask, request, render_template, url_for

app = Flask(__name__)
clf = load("models/model.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method=="POST":
    hasil_prediksi = clf.predict([[request.form['palo'],
                                  request.form['lelo'],
                                  request.form['pako'],
                                  request.form['leko']]])
 
    pred = hasil_prediksi[0]

    if pred == 0:
      d = 'setosa'
    elif pred == 1:
      d = 'versicolor'
    else :
      d = 'versicolor'

    return render_template("index.html",hasil = d)

  else:
    return render_template("index.html")

@app.route('/modeling')
def modeling():
  return render_template("modeling.html")

# KALAU DI-ONLINE'KAN BARIS DI BAWAH INI DIHAPUS SAJA
app.run(debug=True)