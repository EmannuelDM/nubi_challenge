
# Nubi Challenge

[Detalles del challenge](https://github.com/AleSotoNubi/challenge-python-ssr)

## Levantar el proyecto con docker-compose

- Crear un .env a partir del .env.template y completar las constantes que falten.
- Ejecutar docker-compose build
- Ejecutar docker-compose up
- En local puedes acceder a http://0.0.0.0:8000/


## Informacion sobre los endpoints
En local puedes acceder a la documentacion de swagger con http://0.0.0.0:8000/docs

## Ejemplo con queryparams
http://0.0.0.0:8000/user/?order_by=-name&page=1&size=10


## Ejecutar los tests
Puedes ejecutar los tests ejecutando:
docker-compose run --rm fastapi pytest .

## Librerias externas usadas
[fastapi-filter](https://fastapi-filter.netlify.app/)
[fastapi-pagination](https://uriyyo-fastapi-pagination.netlify.app/)
