# baleine
🐋 Run code snippets from discord over docker.

> Baleine is a discord bot that allow users to run<br>
> code snippets safely accross the server.

### Supported languages

- Go
- Lua
- Javascript
- Perl
- Python 2, 3
- Ruby
- Shell
- Swift

## Get started

**Note** : Python 3.6 or higher is required.

```bash
# clone the repository
$ git clone https://github.com/boardens/baleine.git

# change the working directory to baleine
$ cd baleine

# install python3 and python3-pip if they are not installed

# install the requirements
$ python3 -m pip install -r requirements.txt
```
### Requirements

```bash
# install docker if it isn't intalled
$ sudo apt-get remove docker docker-engine docker.io containerd runc

# start docker service
$ systemctl start docker || service docker start

# pull docker images
$ docker pull golang:latest
$ docker pull dexec/lua:latest
$ docker pull node:latest
$ docker pull perl:latest
$ docker pull python:2
$ docker pull python:3
$ docker pull ruby:latest
$ docker pull alpine:latest
$ docker pull efrecon/tcl:latest
```
