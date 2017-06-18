# composetest
testing latest version (1.13) of compose using some samples as starters (thanks to : http://anandmanisankar.com/posts/docker-container-nginx-node-redis-example/ )

quick start:

be sure you have docker and docker-compose installed

git clone https://github.com/vroomvroomvroom/composetest.git
cd composetest/
sudo /usr/local/bin/docker-compose build
sudo /usr/local/bin/docker-compose up -d

curl http://0.0.0.0:80/

sudo /usr/local/bin/docker-compose down --volume

Have fun!


