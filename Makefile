.PHONY: test, format, check

test:
	@pytest -vv --driver Chrome

format:
	@black flask_pwa exemple_app tests

check:
	@black flask_pwa exemple_app tests --check