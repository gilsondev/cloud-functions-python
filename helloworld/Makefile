.PHONY: serve
serve:
	@functions-framework --target hello_http --debug

.PHONY: test
test:
	@pytest -v ./tests

.PHONY: requirements
requirements:
	# @poetry export --without-hashes --format=requirements.txt > requirements.txt
	@poetry export --without-hashes --format=requirements.txt > requirements.txt
