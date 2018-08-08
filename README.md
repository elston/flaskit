Flask Webpack Starter Kit
========================

Yet another boilerplate web  application 


Technology
----------------
- Docker
- Python 3.5
- Flask
- Nodejs
- Webpack
- Postgres 9.6
- Nginx
- Gunicorn
- Virtualenv


Getting Started for Local Development
====================================================================


Installing and bootstraping
--------------------------------------------------------------------

### Install Docker

https://docs.docker.com/installation/

### Install Docker Compose

http://docs.docker.com/compose/install/

### Install the app's

In the project books ./book/dev/ (where the `Makefile` file is located), run:

```
make build
```

then

```
make bootstrap
```

then

```
make db
```

then test db

```
psql -U mark -h localhost
```

if all OK, down db

```
make down
```

then migrate db

```
make migrate
```


Helper commands
--------------------------------------------------------------------

### To run any command inside the Docker container
```
make shell_[and name of container]
```


### Clear untagged Docker containers

```
make clear
```

### To view runing Docker containers

```
make ps
```

In backend (backer) container
--------------------------------------------------------------------

### To run

```
make shell_backer
```

### Then...

```
runserver.sh
```


In frontend (fronter) container
--------------------------------------------------------------------

### To run

```
make shell_fronter
```


### Then...

```
cd /fronter
yarn [name of commands from packege.json]
```



In browser
--------------------------------------------------------------------

open in brouser url ```http://localhost:3000```



Getting Started with testing or production
====================================================================


### This will start the containers in the background.

```
make up
```

When you need finish all containers:

```
make down
```

### View the logs

```
docker logs [-f] [name of container getting from docker ps -a]
```


Acknowledgment
====================================================================
* kriasoft - [react-starter-kit](https://github.com/kriasoft/react-starter-kit)
* Cory House - [react-slingshot](https://github.com/coryhouse/react-slingshot)
* Steven Loria - [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask)
