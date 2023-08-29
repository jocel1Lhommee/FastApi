# Les commandes pour lancer le server Python
 
Commande à écrire dans le terminal :
 
- uvicorn main:app
    
> indique à uvicorn de prendre l'objet app dans le fichier main

 - ou uvicorn main:app --reload
    
> permet de relancer automatiquement le serveur après chaque modification du code

 - ou uvicorn main:app --reload --host 0.0.0.0
    
> à tester... permet d'être consulté à partir d'une autre machine.

> plus d'infos : https://www.uvicorn.org/settings/
     
    