from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('/home.html')

@app.route('/about')
def about():
    return render_template('/about.html')

if __name__ == "__main__":

            #EL DEBUG ACTUALIZA EL MAIN SIN REINICIAR EL SERVER
    app.run(debug = True) 