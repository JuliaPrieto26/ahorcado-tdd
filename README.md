![Tests](https://github.com/agustindangelo/ahorcado-tdd/actions/workflows/github-actions.yml/badge.svg)

# -- STEP 1: Configurar e instalar un entorno virtual
'''$ virtualenv --python python3 .venv'''
'''$ source .venv/bin/activate'''

### -- EN WINDOWS:
'''call .venv/Scripts/activate'''

# -- STEP 2: Instalar paquetes requeridos de Python
'''$ pip install -r py.requirements/all.txt'''

#### Correr los tests unitarios y los tests de aceptación
'''tox'''
