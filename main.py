from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from os import walk
from markdown import markdown
from datetime import datetime

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="cours")

monRepertoire = '.\\media'
extension = '.md'

def parcourir(cible,rep):
    sousmonRepertoire=monRepertoire+"\\"+rep
    cours={}
    for (repertoire, sousRepertoires, fichiers) in walk(sousmonRepertoire):
        # pour chaque fichier dans la liste des fichiers
        for fichier in fichiers:
            if fichier.endswith(extension):
                adresse = repertoire[::]+'\\'+fichier
                with open(adresse, "r") as f_in:
                    contenu = f_in.read()
                    contenu = markdown(contenu)
                if len(cible) == 0 or cible in contenu:
                    cours[fichier[:-len(extension)]] = [repertoire[len(monRepertoire)+1::], contenu]

    return cours

def lecture_dossier():
    listeRepertoire = []

    for (repertoire, sousRepertoires, fichiers) in walk(monRepertoire):
        for fichier in fichiers:
            if fichier.endswith(extension):
                listeRepertoire.append(repertoire[len(monRepertoire) + 1::])

    return list(set(listeRepertoire))

@app.get("/", response_class=HTMLResponse)
async def root(request: Request, cible: str = '', rep: str = ''):
    print("Ma fonction python s'execute")
    cours = parcourir(cible, rep)
    # fonction différente afin d'avoir tous les dossiers ...
    # ... et non pas seulement ceux issue de la recherche en cours
    liste_repertoire = lecture_dossier()
    print(liste_repertoire)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "cours": cours, "liste_repertoire": liste_repertoire}
    )
