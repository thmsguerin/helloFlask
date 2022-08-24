# helloFlask

Mon helloFlask utilise Python 3.8.6    
prise en main de pyenv et poetry   
Test de site web local avec jinja    
    
pyenv ---> installer python vXXX 
       
poetry ---> rend transparent la creation d'un projet Python   
 -> gestion de l'env virtuel    
 -> arborescence du projet   
 -> gestion des dependances   
 -> packaging d'un projet    
   
# MEMO
   
## Installation et utilisation de Pyenv
   
*pyenv install 3.8.6*   
pour installer python 3.8.6   
puis aller dans le dossier et faire    
*pyenv local 3.8.6*      
pour le set en python par defaut du dossier    
     
*pyenv versions*    
permet de voir les versions de python et les env virtuels   
      
*pyenv virtualenv "version python" "nom de l'env"*   
pour creer un virtual environnement  
    
     
See all available python installations:    
*pyenv install --list*   
     
Install some python versions:    
*pyenv install  3.7.5*     
*pyenv install  2.7.17*    
*pyenv install  3.8.0*    
   
See all python installations that you have installed:    
*pyenv versions*   
    
Set the default/global from one of the python versions.    
*pyenv global 3.8.0*   
    
In the current directory, set the python version. This creates the file .python-version.    
*pyenv local 2.7.17*    
    
To see which python is currently being used.   
*pyenv version*     
    
    
Installation et utilisation de Poetry
---
Install poetry via curl   
*curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python*    
    
Add poetry to your shell    
*export PATH="$HOME/.poetry/bin:$PATH"*    
   
Configure poetry to create virtual environments inside the project's root directory    
*poetry config virtualenvs.in-project true*     
    
        
Installation et utilisation de jinja2
---
    
      
