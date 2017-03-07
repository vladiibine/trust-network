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

clean:
	rm -rf $(VENV_TMP_DIR)
	rm -rf $(VENV_DIR)

serve:
	$(VENV_DIR)/bin/tnb_serve
