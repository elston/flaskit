include ../global.sh
include ../security.sh


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


.PHONY: pull_nginx
pull_nginx:
	@echo "---> pull nginx ${NGINX_TAG}"
	@docker pull nginx:${NGINX_TAG}


.PHONY: pull_node
pull_node:
	@echo "---> pull node ${NODE_TAG}"
	@docker pull node:${NODE_TAG}


.PHONY: pull_all
pull_all:
	@make pull_postgres
	@make pull_python
	@make pull_nginx
	@make pull_node



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


.PHONY: bootstrap_storage
bootstrap_storage:
	@echo "---> bootstrap storage"	
	@docker-compose \
		-p $(PROJECT) \
		-f bootstrap.yml \
		run --rm storage


.PHONY: bootstrap_backer
bootstrap_backer:
	@echo "---> bootstrap backer"
	@docker-compose \
		-p $(PROJECT) \
		-f bootstrap.yml \
		run --rm backer /usr/local/bin/bootstrap.sh
	@echo "---> end session backer"
	@make down	


.PHONY: bootstrap_fronter
bootstrap_fronter:
	@echo "---> bootstrap fronter"
	@docker-compose \
		-p $(PROJECT) \
		-f bootstrap.yml \
		run --rm fronter /usr/local/bin/bootstrap.sh
	@echo "---> end bootstrap fronter"


.PHONY: bootstrap_all
bootstrap_all:
	@make bootstrap_storage
	@make bootstrap_backer



# =========== db =======================


.PHONY: db
db:
	@docker-compose \
		-p $(PROJECT) \
		-f db.yml \
		up -d --no-build --no-recreate


# ==========  migrate =================


.PHONY: migrate_backer
migrate_backer:
	@docker-compose \
		-p $(PROJECT) \
		-f migrate.yml \
		run --rm backer /usr/local/bin/migrate.sh
	@echo "---> end session backer"
	@make down


# ==========  compile =================

.PHONY: compile_fronter
compile_fronter:
	@make down
	@echo "---> begin compile fronter"	
	@docker-compose \
		-p $(PROJECT) \
		-f compile.yml \
		run --rm fronter /usr/local/bin/compile.sh
	@echo "---> end session fronter"
	@make down

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

# ============ restart ======================

.PHONY: restart_backer
restart_backer:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		restart -t 0 backer

.PHONY: restart_router
restart_router:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		restart -t 0 router	



# ============ misc ======================

.PHONY: up
up:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		up -d --no-build --no-recreate		

.PHONY: down
down:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		down	


.PHONY: ps
ps:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		ps

.PHONY: ps
clear:
	@../../scripts/clear_untagged.sh

