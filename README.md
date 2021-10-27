![Tests](https://github.com/agustindangelo/ahorcado-tdd/actions/workflows/github-actions.yml/badge.svg)

#### Crear un entorno virtual
Linux:

```
$ virtualenv --python python3 .venv
$ source .venv/bin/activate
```

Windows:

```call .venv/Scripts/activate```

#### Instalar paquetes requeridos de Python
```$ pip install -r py.requirements/all.txt```

#### Correr los tests unitarios y los tests de aceptación
```tox```
