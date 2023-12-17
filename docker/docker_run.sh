docker build -t "container" .
cd ..
docker run --name tests -it -v $PWD:/tmp -w /tmp container
