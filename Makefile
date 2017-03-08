VENV_TMP_DIR = '.tmpvenv'
VENV_DIR = 'venv-tnb'
PYTHON = 'python3.5'

############################
# Help	
############################
help:
	@echo "usage: make <command>"
	@echo
	@echo "   srv-install-dev		to install the server in development mode"
	@echo "   srv-install			to install the server in production mode"
	@echo "   compile				to compile the frontend assets"


srv-install-dev:
	@echo ""
	@test -d $(VENV_TMP_DIR) || virtualenv --python $(PYTHON) $(VENV_TMP_DIR)
	@. $(VENV_TMP_DIR)/bin/activate \
		&& pip install -U pip \
		&& pip install -U virtualenv \
		&& { test -d $(VENV_DIR) || virtualenv --always-copy --python $(PYTHON) $(VENV_DIR); } \
		&& $(VENV_DIR)/bin/pip install -U pip \
		&& $(VENV_DIR)/bin/pip install -U -e . \
		&& $(VENV_DIR)/bin/pip install -r py-requirements/dev.txt -r py-requirements/test.txt
	@echo "Done!"

frontend-install-dev:
	npm install

install-dev: srv-install-dev frontend-install-dev

test-srv:
	@$(VENV_DIR)/bin/coverage run --source src/python/trust_network_backend/tnb $(VENV_DIR)/bin/py.test tests/python; \
        echo "Coverage report for python tests: "; \
		$(VENV_DIR)/bin/coverage report |grep -v '\-\-\-\-\-\-\-\-'|grep -v 'src/python' \
		    |sed 's/Name/    /g' ; \
		$(VENV_DIR)/bin/coverage html

clean:
	rm -rf $(VENV_TMP_DIR)
	rm -rf $(VENV_DIR)
	rm -rf dist
	find . -name trust_network_backend.egg-info |xargs -I this rm -rf this
	find . -name __pycache__ |xargs -I this rm -rf this


serve:
	$(VENV_DIR)/bin/tnb_serve

compile:
	npm run compile