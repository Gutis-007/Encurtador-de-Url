# Encurtador de URL Django

## Breve Descrição

Encurtador de URL desenvolvido com **Python**, **Django** e **SQLite3** no backend para cadastro e registro de URLs encurtadas. O projeto permite criar URLs curtas que redirecionam para as URLs originais.

## Como Configurar

#### Instalação do `venv (Virtual Environment)`

> Caso opte por usar um nome personalizado, adicione o nome no `.gitignore` para que a pasta não suba para o repositório.

- Para criar um ambiente virtual, execute:
  ```bash
  python3 -m venv .venv
  ```
  ou, se preferir um nome personalizado:
  ```bash
  python3 -m venv .{nomepersonalizado}
  ```

#### Instalação das Dependências do Projeto

As dependências do projeto estão listadas no arquivo [`requirements.txt`](./requirements.txt).

##### No Windows:
> É necessário habilitar a execução de scripts no PowerShell. Veja mais informações [aqui](https://learn.microsoft.com/pt-br/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4).

1. Ative o ambiente virtual:
   ```bash
   .venv\Scripts\activate
   ```
2. Instale as dependências:
   ```bash
   python -m pip install -r requirements.txt
   ```

##### No Linux:

1. Ative o ambiente virtual:
   ```bash
   source .venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   python -m pip install -r requirements.txt
   ```

#### Criação do Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
# Configurações de ambiente
DEBUG = False
DATABASE_URL = "sqlite:///db.sqlite3"
```

## Estrutura do Projeto

- [`api`](./api/): Diretório que centraliza as funcionalidades da aplicação.

#### A partir de `/api`, temos:

- [`urls.py`](./api/urls.py): Define as rotas da API, organizadas por funções.
- [`models.py`](./api/models.py): Define os modelos do Django ORM para a aplicação.

## Tecnologias Utilizadas

<div style="display: inline_block">
<br>
  <img align="center" alt="PYTHON" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img align="center" alt="DJANGO" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img align="center" alt="SQLITE" src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
</div>

## Como Executar

1. Certifique-se de que o ambiente virtual está ativado e as dependências estão instaladas.

2. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

3. Inicie o servidor de desenvolvimento do Django:
   ```bash
   python manage.py runserver
   ```

4. Abra o navegador e acesse `http://127.0.0.1:8000/api/shorten/` para usar o endpoint de encurtamento de URL.

   Você pode usar uma ferramenta como **Postman** ou **cURL** para enviar uma requisição `POST` para esse endpoint com o JSON da URL original:

   ```json
   {
     "url_original": "https://www.exemplo.com"
   }
   ```

   O servidor responderá com a URL curta gerada.

## Referências e Desafios

Para explorar desafios adicionais e alternativas, veja o [Desafio-BackEnd](https://github.com/backend-br/desafios).

## URL para Visualização

Após iniciar o servidor, você pode acessar o endpoint `/api/shorten/` em `http://127.0.0.1:8000/api/shorten/` para encurtar URLs e testar o redirecionamento.

---

Se precisar de mais alguma informação ou ajuste, estou à disposição!
