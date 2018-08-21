include ../global.sh
include ../security.sh


.PHONY: all
all:
	@echo "Hello $(LOGNAME), nothing to do by default"


# =========== shell ======================

.PHONY: shell_router
shell_router:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		run \
		--rm \
		--name $(PROJECT)_router_1 \
		router \
		/bin/sh	

.PHONY: shell_backer
shell_backer:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		run \
		--rm \
		--name $(PROJECT)_backer_1 \
		backer \
		/bin/bash


# =========== main ======================

# target: up - up all containers
.PHONY: up
up:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		up -d --no-build --no-recreate	


# target: down - down all runing containers
.PHONY: down
down:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		down	

# target: ps - show all runing containers
.PHONY: ps
ps:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		ps



# target: images - show all images in project
.PHONY: images
images:
	@docker images |grep $(PROJECT)


# target: volumes - show all volumes in project
.PHONY: volumes
volumes:
	@docker volume ls |grep $(PROJECT)


# target: rmi - remove all images in project
.PHONY: rmi
rmi:
	@docker rmi `docker images |grep $(PROJECT) |xargs -L1 | awk '{print $1}'`


# target: rmvol - remove all volumes in project
.PHONY: rmvol
rmvol:
	@docker volume rm `docker volume ls |grep $(PROJECT) |xargs -L1 | awk "{print $2}"`
