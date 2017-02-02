docker rm -f dps
docker run -d --name dps --net host docker-pyweb
