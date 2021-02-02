
[![CI](https://github.com/lfvilella/turing-machine/workflows/CI/badge.svg?event=push)](https://github.com/lfvilella/turing-machine/actions?query=event%3Apush+branch%3Amain+workflow%3ACI)
[![license](https://img.shields.io/github/license/lfvilella/turing-machine.svg)](https://github.com/lfvilella/turing-machine/blob/main/LICENSE)

# Turing Machine
UENP's work on the subject of computer theory.

*Needs docker installed.*

Tech Stack:

- Python
- Fastapi
- ReactJS
- Docker / docker-compose

## Running locally
Choose one these options to build the docker container.

```
$ make build
```
or
```
$ cp template.env .env
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

[Formal Docs](https://docs.google.com/document/d/1nlEpVr7OHQRJP5lWXS8RJxbuFCGRZvcVUT6BC7LsM2A/edit?usp=sharing)
