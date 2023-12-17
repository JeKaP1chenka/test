docker build -t "container" .
cd ..
docker run --name tests -v %cd%:/tmp -w /tmp -d container
