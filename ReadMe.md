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

Run ngrok in Background:

ngrok/ngrok http 80 -log=stdout > ngrok.log &

Check random ngrok address

curl localhost:4040/api/tunnels
parkingpage.namecheap.com





Power Saving:

Use this command to turn HDMI off:  /opt/vc/bin/tvservice -o

And this command to turn it on:  /opt/vc/bin/tvservice -p

Use this command to turn USB off entirely:
echo 0x0 > /sys/devices/platform/soc/3f980000.usb/buspower

and this to turn it on:
echo 0x1 > /sys/devices/platform/soc/3f980000.usb/buspower

So turn shut wifi down using ifdown wlan0
and turn it on using ifup wlan