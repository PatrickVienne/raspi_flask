pip steps:
pip install -r web\requirements.txt
pip freeze > requirements.txt

conda steps:
conda create -n pisite python=2.7
activate pisite
...
conda env export -f environment.yml

clean docker:
docker rmi $(docker images -q)
docker rm $(docker ps -a -q)

git:
https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud
git checkout
git clean -f
git reset --hard


gpg:
to avoid "host not found" for keyserver write this line in /etc/resolv.conf:
nameserver 8.8.8.8

ngrok:
unzip ngrok
ngrok/ngrok http 80