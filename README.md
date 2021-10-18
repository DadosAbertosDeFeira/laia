# Laiá

[![CI](https://github.com/DadosAbertosDeFeira/pedidos/actions/workflows/ci.yml/badge.svg)](https://github.com/DadosAbertosDeFeira/pedidos/actions/workflows/ci.yml)

Cadastre e acompanhe o status dos seus pedidos de informação 📃✨

----

Quer usar esse projeto? Cadastre-se no [Heroku](https://heroku.comhttps://heroku.com) e clique no botão para deploy:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/DadosAbertosDeFeira/laia)

## Configurando seu ambiente

### Carregue as variáveis de ambiente

Para a aplicação funcionar, é necessário criarmos um arquivo `.env`, um arquivo de configuração que é individual por possuir dados sensíveis.
Para configurar sua `.env`, busque pelo exemplo de configuração `.env.example` na raiz do projeto,
faça uma cópia e deixe o arquivo com a extensão `.env`.

Para rodar o projeto Laiá, você pode instalar o [Poetry](https://python-poetry.org/docs/master/#installation),
para conseguir instalar automaticamente todas as dependências do projeto.

A execução é feita com [Docker](https://www.docker.com/) e [docker-compose](https://docs.docker.com/compose/).

### Instale as dependências do projeto

```bash
poetry install
```

### Utilizando docker-compose

```bash
docker-compose up --build
```

Para aplicar as migrations, execute:

```bash
make migrate
```

Outros atalhos podem ser vistos em nosso [Makefile](Makefile).

### Configure o pre-commit

Instale o pre-commit localmente rodando `pre-commit install`. Dessa forma,
o código que você commitar já estará formatado, com os imports ordenados e mais arrumado.

### Rode o shell do Poetry e inicie o ambiente virtual.

```bash
poetry shell
```

### Crie um usuário para incluir seus pedidos

```bash
make createsuperuser
```

#### Aplique as migrations

```bash
make migrate
```

## Rodando a aplicação

```bash
make run
```

Acesse [localhost:8000](http://localhost:8000).
