docker build -f Dockerfile -t nrrd .


docker run -dit --name nrrd -v /tmp:/tmp nrrd /bin/bash -c "/etc/rc.local;/bin/bash" 



# test

docker exec -it nrrd bash


pvpython hello.py