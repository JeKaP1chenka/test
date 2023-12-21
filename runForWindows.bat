docker rm tests
docker build -t "container" .
docker run --name tests container