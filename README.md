
[![CI](https://github.com/lfvilella/turing-machine/workflows/CI/badge.svg?event=push)](https://github.com/lfvilella/turing-machine/actions?query=event%3Apush+branch%3Amain+workflow%3ACI)
[![license](https://img.shields.io/github/license/lfvilella/turing-machine.svg)](https://github.com/lfvilella/turing-machine/blob/main/LICENSE)

# Turing Machine
UENP's work on the subject of computer theory.

*Needs docker installed.*

## Running locally
Choose one these options to build the docker container.

```
$ make build
```
or
```
$ [ -f .env ] || cp template.env .env
$ docker-compose up --build -d
```
*At first time this build lates a little minute, see the logs to verify what's happening...*

To see logs on container:
```
$ docker-compose logs -f --tail=100 frontend
$ docker-compose logs -f --tail=100 backend
```

Open: http://localhost:3000

Docs: http://localhost:8000/api/v.1/docs

Optional:
```
$ make test
```
