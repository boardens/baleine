<p align="center">
  <img src="https://raw.githubusercontent.com/boardens/baleine/c46bcf05417026ab95c1bb036f2e53b84d66b324/img/logo.svg" width="320px">
</p>

# baleine <sup>beta<sup>
🐋 Run code snippets from discord over docker.

> Baleine is a discord bot that allow users to run<br>
> code snippets safely accross the server.

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

### Configuration

Create a [discord bot](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) and define it token in `config.json`.

```json
{
  "prefix": "%",
  "token": "your token"
}
```

## Usage

```bash
'baleine' usage :
(Run code snippets from discord over docker.)
%help, %h             # display help and info
%list, %l             # display all languages available
%[language]           # run code snippet
```

## Compatibilities

Each language settings are stored in `lang.json`.

```json
{
  "name": "ruby",
  "image": "ruby:latest",
  "command": "ruby {FILE_PATH}",
  "manager": "gem install {PACKAGE}",
  "hello": "puts \"hello world\"",
  "ext": "rb"
},
```

> ⚠️ We're currently experiencing issues with compiled languages.

| Argument | Description |
|---|---|
| `name` | Displayed language name |
| `image` | Docker image corresponding |
| `command` | Script run command |
| `manager` | Package manager command |
| `hello` | Hello world script |
| `ext` | Language extension |

Currently supported languages :
- Go
- Lua
- Javascript
- Perl
- Python 2, 3
- Ruby
- Shell
- Swift

## License

[GPL-3.0](https://github.com/boardens/watson/LICENSE/) License
