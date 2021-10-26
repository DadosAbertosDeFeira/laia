# Laiá

Laiá é uma aplicação onde você será capaz de cadastrar, atualizar, acompanhar o status dos seus **pedidos de informação** e disponibilizá-los publicamente. 

Não sabe o que é um pedido de informação ou não sabe como fazer uma solicitação? Para saber mais, leia os artigos abaixo ⬇️

- [Como realizar um pedido de informação](https://dadosabertosdefeira.medium.com/como-realizar-um-pedido-de-informa%C3%A7%C3%A3o-35b3cf4e5dbd)

- [Solicitando dados via Lei de Acesso à Informação](https://escoladedados.org/tutoriais/solicitando-dados-via-lei-de-acesso-a-informacao/)

Nessa página você encontrará instruções de instalação e contribuição do Laiá.

1. [Deploy no Heroku](#deploy-no-heroku)

2. [Instalação e configuração do Laiá](#Instalacao-e-configuracao-do-laia)

3. [Como contribuir](#Como_contribuir)

## Deploy no Heroku

Você pode facilmente usar o Laiá via deploy do Heroku. Para isso, basta criar ou acessar seu cadastro no Heroku e clicar no botão abaixo para Deploy:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/DadosAbertosDeFeira/laia)

## Instalação e configuração do Laiá

Para instalar o projeto, certifique-se que você possui os seguintes requisitos instalados localmente na sua máquina:

- Docker;

- Poetry;

- Pre-commit. 

Esses requisitos são essenciais para a execução do Laiá, que é feita com Docker e docker-compose. Utilizamos o Poetry, para instalar automaticamente todas as dependências do projeto e a biblioteca pre-commit para commitar o código formatado.

### Configurando as Variáveis de Ambiente

Para a aplicação funcionar, precisamos carregar as variáveis de ambiente. Ou seja, é necessário criar um arquivo `.env`, um arquivo de configuração individual que contém dados sensíveis.

Para configurar sua `.env`, busque pelo exemplo de configuração nomeado como `.env.example` na raiz do projeto, faça uma cópia e o renomeie para `.env` e pronto! Não é necessário fazer alterações nas informações contidas no corpo desse arquivo.

### Instalando as dependências do projeto

Com as variáveis de ambiente configuradas, chegou a hora de instalarmos as depedências do Laiá. Siga o passo-a-passo a seguir:

#### 1. Instale as dependências do projeto

```bash
poetry install
```

#### 2. Crie sua aplicação com docker-compose

```bash
docker-compose up --build
```

#### 3. Aplique as migrations

```bash
make migrate
```

Outros atalhos podem ser encontrados no nosso arquivo [Makefile](Makefile).

Com as dependências instaladas, podemos iniciar o ambiente virtual do Laiá.



#### Rodando o Laiá

#### 1. Inicie o Ambiente Virtual

```bash
poetry shell
```

Esse comando é responsável por ativar a máquina virtual com todas as dependências previamente instaladas. 

#### 2. Crie seu usuário para inserir pedidos de informação

```bash
make createsuperuser
```

#### 2. Aplique as migrations

```bash
make migrate
```

#### 3. Rode a aplicação

```bash
make run
```

E acesse [localhost:8000](http://localhost:8000) para visualizar o Laiá ou [localhost:8000/admin](http://localhost:8000/admin) para gerenciar seus pedidos. 



#### Rodando os testes

Você pode executar os testes no ambiente virtual criado pelo Poetry com `pytest` ou rodando `make tests` para executar os testes dentro do container.