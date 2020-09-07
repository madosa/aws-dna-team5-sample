.PHONY: build invoke-local-echo deploy lock

build:
	@sam build --use-container

invoke-local-echo:
	@sam local invoke "SlackEchoFunction" -e events/echo.json

deploy: build
	@sam deploy --no-confirm-changeset

lock:
	@poetry export -f requirements.txt -o requirements.txt -n --without-hashes