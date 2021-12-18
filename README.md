![Tests](https://github.com/agustindangelo/ahorcado-tdd/actions/workflows/github-actions.yml/badge.svg)

# Instalación en el entorno local
### 1.1: frontend
```
cd frontend
npm install
ng serve --open
```

### 1.2: backend
```
virtualenv --python python3.9 .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
flask run

```

En windows se activa con ```.venv\Scripts\Activate.ps1```

En el navegador: `localhost:4200`

## Opción 2: docker
En el directorio raíz del proyecto:
```
docker run -d -it -p 5000:5000 agustindangelo/ahorcado-backend
docker run -d -it -p 80:80 agustindangelo/ahorcado-frontend
```

En el navegador: `localhost`
