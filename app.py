from flask import Flask, render_template, request
import mon_script

app = Flask(__name__)

@app.route('/mdp', methods=['GET', 'POST'])
def index():
    mot_de_passe = None
    if request.method == 'POST':
        try:
            longueur = int(request.form['longueur'])
            mot_de_passe = mon_script.generer_mot_de_passe(longueur)
        except:
            mot_de_passe = "Erreur : Veuillez entrer un nombre valide."
    return render_template('index.html', mot_de_passe=mot_de_passe)

if __name__ == '__main__':
    app.run()
