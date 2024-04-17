# a3data

Teste Técnico - Machine Learning Engineer

Para iniciar a API existem 2 possibilidades:
- Linha de comando:
		- Ter o Python instalado (versão 3.8+)
		- Instalar as dependências: `pip install -r requirements.txt`
		- Rodar a pipeline: `python pipeline.py`
		- Iniciar o servidor: `uvicorn main:app --reload`
		- Acessar a api pelo endereço http://127.0.0.1:8000
- Docker:
		- Ter a linha de comando do Docker instalada
		- Buildar a imagem: `docker build -t <nome do app> .`
		- Rodar a imagem: `docker run -p 8080:8080 <nome do app>`
		- Acessar a api pelo endereço http://127.0.0.1:8080

Após iniciada a API e acessado o endereço dela, o usuário será direcionado para a documentação da API no endpoint /docs, lá o usuário poderá interagir com a api clicando no a opção de post /iris/, try it out e adicionando valores nos campos indicados para obter uma classificação.