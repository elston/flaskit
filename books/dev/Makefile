include ../global.sh
include ../security.sh


.PHONY: all
all:
	@echo "Hello $(LOGNAME), nothing to do by default"


# ========= pull ==============


.PHONY: pull_postgres
pull_postgres:
	@echo "---> pull postgres ${POSTGRES_TAG}"
	@docker pull postgres:${POSTGRES_TAG}


.PHONY: pull_python
pull_python:
	@echo "---> pull python ${PYTHON_TAG}"
	@docker pull python:${PYTHON_TAG}


.PHONY: pull_node
pull_node:
	@echo "---> pull nginx ${NGINX_TAG}"
	@docker pull nginx:${NGINX_TAG}


.PHONY: pull_nginx
pull_nginx:
	@echo "---> pull node ${NODE_TAG}"
	@docker pull node:${NODE_TAG}


.PHONY: pull_all
pull_all:
	@make pull_postgres
	@make pull_python
	@make pull_node	
	@make pull_nginx


# =========== build ================


.PHONY: build_storage
build_storage:
	@echo "---> build storage"	
	@docker-compose \
		-p $(PROJECT) \
		-f build.yml \
		build storage


.PHONY: build_backer
build_backer:
	@echo "---> build backer"
	@docker-compose \
		-p $(PROJECT) \
		-f build.yml \
		build backer		


.PHONY: build_all
build_all:
	@make build_storage
	@make build_backer	


# ========= bootstrap ==============


# target: bootstrap_storage
.PHONY: bootstrap_storage
bootstrap_storage:
	@echo "---> bootstrap storage"	
	@docker-compose \
		-p $(PROJECT) \
		-f bootstrap.yml \
		run --rm storage /usr/local/bin/bootstrap.sh
	@echo "---> end bootstrap storage"

# target: bootstrap_backer
.PHONY: bootstrap_backer
bootstrap_backer:
	@echo "---> bootstrap backer"
	@docker-compose \
		-p $(PROJECT) \
		-f bootstrap.yml \
		run --rm backer /usr/local/bin/bootstrap.sh
	@echo "---> end bootstrap backer"


# target: bootstrap_fronter
.PHONY: bootstrap_fronter
bootstrap_fronter:
	@echo "---> bootstrap fronter"
	@docker-compose \
		-p $(PROJECT) \
		-f bootstrap.yml \
		run --rm fronter /usr/local/bin/bootstrap.sh
	@echo "---> end bootstrap fronter"


# target: bootstrap_all
.PHONY: bootstrap_all
bootstrap_all:
	@make bootstrap_storage
	@make bootstrap_backer
	@make bootstrap_fronter	
	@make down

# =========== db =======================


# target: db - shell fronter container
.PHONY: db
db:
	@docker-compose \
		-p $(PROJECT) \
		-f db.yml \
		up -d --no-build --no-recreate


# ==========  migrate =================


# target: migrate_backer - migrate db in backer container
.PHONY: migrate_backer
migrate_backer:
	@echo "---> start migrate backer"	
	@docker-compose \
		-p $(PROJECT) \
		-f migrate.yml \
		run --rm backer /usr/local/bin/migrate.sh
	@echo "---> end migrate backer"
	@make down


# =========== shell ======================


# target: shell_backer - shell backer container
.PHONY: shell_backer
shell_backer:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		-f shell.yml \
		run \
		--rm \
		--service-ports \
		--name $(PROJECT)_backer_1 \
		backer \
		/bin/bash	


# target: shell_fronter - shell fronter container
.PHONY: shell_fronter
shell_fronter:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		-f shell.yml \
		run \
		--rm \
		--service-ports \
		--name $(PROJECT)_fronter_1 \
		fronter


# ============ misc ======================


# target: down - down all runing containers from current project
.PHONY: down
down:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		down	

# target: ps - show worked containers
.PHONY: ps
ps:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		ps

# target: clear - to clear untagged containers
.PHONY: clear
clear:
	@../../scripts/clear_untagged.sh


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
