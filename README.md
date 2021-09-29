# Laiá

[![CI](https://github.com/DadosAbertosDeFeira/pedidos/actions/workflows/ci.yml/badge.svg)](https://github.com/DadosAbertosDeFeira/pedidos/actions/workflows/ci.yml)

Cadastre e acompanhe o status dos seus pedidos de informação 📃✨

## Configurando seu ambiente

Para rodar o projeto Laiá, você precisa instalar o [Poetry](https://python-poetry.org/docs/master/#installation),
para conseguir instalar automaticamente todas as dependências do projeto.

### Instale as dependências do projeto

```bash
poetry install
```

### Configure o pre-commit

Instale o pre-commit localmente rodando `pre-commit install`. Dessa forma, o código que você commitar já estará formatado,
com os imports ordenados e mais arrumado.

### Carregue as variáveis de ambiente

Para a aplicação funcionar, é necessário criarmos um arquivo `.env`, um arquivo de configuração que é individual por possuir dados sensíveis.
Para configurar sua `.env`, busque pelo exemplo de configuração `.env.example` na raiz do projeto,
faça uma cópia e deixe o arquivo com a extensão `.env`.

### Rode o shell do Poetry e inicie o ambiente virtual.

```bash
poetry shell
```

### Crie um usuário para incluir seus pedidos

```bash
python manage.py createsuperuser
```

#### Aplique as migrations
```bash
python manage.py migrate
```

## Rodando a aplicação

```bash
python manage.py runserver
```

Acesse [localhost:8000](http://localhost:8000).
