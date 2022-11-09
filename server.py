from dojos_ninjas import app
from dojos_ninjas.controllers import dojos, ninjas
app.secret_key = "estessecreto"


if __name__=="__main__":
    app.run(debug=True)