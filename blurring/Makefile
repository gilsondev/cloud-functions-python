.PHONY: test
test:
	@pytest -v ./tests

.PHONY: requirements
requirements:
	@poetry export --without-hashes --format=requirements.txt > requirements.txt

.PHONY: deploy
deploy: requirements
	@gcloud functions deploy blur_images --runtime python310 --trigger-bucket=gilsondevlabs

.PHONY: undeploy
undeploy:
	@gcloud functions delete blur_images

.PHONY: prod-logs
prod-logs:
	@gcloud functions logs read blur_images
