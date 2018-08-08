export PROJECT = flaskit
# export REQNAME = prod
# export NGINX_CONF = simple
export NGINX_CONF = ssl
export FLASK_CONFIGURATION = base


include ../../security.sh

all:
	@echo "Hello $(LOGNAME), nothing to do by default"

# ========= pull ==============
.PHONY: pull_postgres
pull_postgres:
	@echo "---> pull postgres:9.6"
	@docker pull postgres:9.6

.PHONY: pull_python
pull_python:
	@echo "---> pull python:3.6-slim-jessie"
	@docker pull python:3.6-slim-jessie


.PHONY: pull_nginx
pull_nginx:
	@echo "---> pull nginx:1.13.8-alpine"	
	@docker pull nginx:1.13.8-alpine	

.PHONY: pull_certbot
pull_certbot:
	@echo "---> pull certbot/certbot"
	@docker pull certbot/certbot


.PHONY: pull_all
pull_all:
	@make pull_postgres
	@make pull_python
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
	# @make build_registrar
	# @make build_crowdface
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
# restart_registrar:
# 	@docker-compose \
# 		-p $(PROJECT) \
# 		-f run.yml \
# 		restart -t 0 registrar

# restart_crowdface:
# 	@docker-compose \
# 		-p $(PROJECT) \
# 		-f run.yml \
# 		restart -t 0 crowdface

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

