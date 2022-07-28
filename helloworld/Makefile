.PHONY: serve
serve:
	@functions-framework --target hello_http --debug

.PHONY: test
test:
	@pytest -v ./tests

.PHONY: requirements
requirements:
	@poetry export --without-hashes --format=requirements.txt > requirements.txt

.PHONY: deploy
deploy: requirements
	@gcloud functions deploy hello_http --runtime python310 --trigger-http --allow-unauthenticated

.PHONY: undeploy
undeploy:
	@gcloud functions delete hello_http

.PHONY: prod-logs
prod-logs:
	@gcloud functions logs read hello_http
