#!/bin/bash

docker stop auth
docker stop student
docker stop teacher
docker stop single_service


docker rm auth
docker rm student
docker rm teacher
docker rm single_service

docker run --name auth --link mysql:mysql -p 8000:8000 -d auth
docker run --name student --link mysql:mysql -p 8001:8001 -d student
docker run --name teacher --link mysql:mysql -p 8002:8002 -d teacher
docker run --name single_service --link mysql:mysql -p 8003:8003 -d single_service

