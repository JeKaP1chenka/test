docker build -t "container" .
cd ..
docker run --name tests -it -v %cd%:/tmp -w /tmp container
