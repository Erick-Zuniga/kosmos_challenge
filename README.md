# Instalación
Clonar el repositorio
```
git clone https://github.com/Erick-Zuniga/kosmos_challenge.git
```
cambiar a la carpeta del proyecto
```
cd kosmos_challenge
```
crear un ambiente con conda y activarlo
```
conda create -n kosmos
conda activate kosmos
```
instalar pip
```
conda install pip
```
instalar los paquetes necesarios usando pip
```
pip install -r requirements.txt
```
# Ejecución
Para levantar el servidor, ejecutar
```
python app.py
```
Una vez levantado el servidor, la ruta al la que se le tiene que hacer post es `localhost:5000/ner`. A continuación se presenta un ejemplo utilizando `curl` desde la terminal
```
curl -X POST -H "Content-Type: application/json" -d '{"oraciones": ["Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.", "San Francisco considera prohibir los robots de entrega en la acera."]}' localhost:5000/ner
```