
# Ejecutar la instalación

## Opción 1: entorno local
### 1.1: frontend
```
cd frontend
npm install
ng serve --open
```

### 1.2: backend
```
python3 -m
source .venv/bin/activate
python3 -m pip install requirements.txt
flask run
```

En el navegador: `localhost:4200`

## Opción 2: docker
En el directorio raíz del proyecto:
```
docker run -d -it -p 5000:5000 agustindangelo/ahorcado-backend
docker run -d -it -p 80:80 agustindangelo/ahorcado-frontend
```

En el navegador: `localhost`
