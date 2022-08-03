.PHONY: test
test:
	@pytest -v ./tests

.PHONY: requirements
requirements:
	@poetry export --without-hashes --format=requirements.txt > requirements.txt

.PHONY: deploy
deploy: requirements
	@gcloud functions deploy alarm_pubsub --runtime python310 --trigger-topic topic_pubsublab

.PHONY: undeploy
undeploy:
	@gcloud functions delete alarm_pubsub

.PHONY: prod-logs
prod-logs:
	@gcloud functions logs read alarm_pubsub
