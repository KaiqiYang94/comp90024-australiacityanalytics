sudo apt install git

git clone https://kaiqiypublic:kaiqiypublicpw@bitbucket.org/xingh1/comp90024-australiacityanalytics.git


## deployment 


sudo apt-get update

sudo apt-get install git

wget https://nodejs.org/dist/latest/node-v7.10.0-linux-x64.tar.gz


## Adding user

sudo adduser kaiqi

sudo usermod -aG sudo kaiqiy

sudo nano /etc/ssh/sshd_config

PasswordAuthentication no ==>

PubkeyAuthentication yes

sudo systemctl reload sshd



# 
curl -X DELETE http://admin:password@localhost:5984/_global_changes