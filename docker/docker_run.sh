docker build -t "container" .
cd ..
docker run --name tests -v $PWD:/tmp -w /tmp -d container
