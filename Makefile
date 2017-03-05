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
		&& pip install -U pip \
		&& pip install -U ./src/python/trust_network_backend/
	@echo "Done!"

clean:
	rm -rf $(VENV_TMP_DIR)
	rm -rf $(VENV_DIR)

