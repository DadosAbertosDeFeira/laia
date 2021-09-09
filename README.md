# pedidos
Cadastre e acompanhe o status dos seus pedidos de informação 📃

#### Configurando seu ambiente

Para rodar o projeto Pedidos, você precisa instalar o [Poetry](https://python-poetry.org/docs/master/#installation), para conseguir instalar automaticamente todas as dependências do projeto.


#### Carregue as variáveis de ambiente

Para a aplicação funcionar, é necessário criarmos um arquivo `.env`, um arquivo de configuração que é individual por possuir dados sensíveis. Para configurar sua `.env`, busque pelo exemplo de configuração `.env.example` na raiz do projeto, faça uma cópia e deixe o arquivo com a extensão `.env`. 

#### Instale as dependências do projeto

```bash
poetry install
```

#### Rode o shell do Poetry e inicie o ambiente virtual.
```bash
poetry shell
```

#### Crie um usuário para incluir seus pedidos
```bash
python manage.py createsuperuser
```

#### Rode a aplicação Django
```bash
python manage.py runserver
```

#### Aplique as migrations
```bash
python manage.py migrate
```

