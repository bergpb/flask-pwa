test:
	@pytest -vv

format:
	@black flask_pwa sample_app tests
 
check:
	@black flask_pwa sample_app tests --check

.PHONY: test format check