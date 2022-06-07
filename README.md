# Instruções

Para rodar o projeto, deve-se ter instalado o Python, Django e Django Rest Framework.

Exemplo (Windows):

- Instale o Python;
- Mude o diretório para a pasta deste projeto 'cd your_path\AthleteEvents', substituindo your_path pelo caminho onde está localizado o diretório AthleteEvents;
- Crie um ambiente virtual, se não houver, digitando: 'python -m venv .venv'. Substitua .venv pelo nome que deseja que seu ambiente virtual tenha;
- Ative o ambiente virtual: .venv\Scripts\activate;
- Instale o Django: 'pip install django';
- Instale o Django Rest Framework: 'pip install djangorestframework';
- Garanta que tudo esteja correto com os comandos: 'python manage.py makemigrations' e em seguida 'python manage.py migrate';
- Rode o projeto com: 'python manage.py runserver';
- Acesse no seu navegador o local onde o servidor foi iniciado (ex: http://127.0.0.1:8000/). No entanto, não foi definida uma página inicial. Para rodar o projeto, leia os passos abaixo.

### Utilizando o projeto
- Para listar todas as informações do banco de dados, adicione 'events/' no caminho: http://127.0.0.1:8000/events/;
- Para acrescentar um evento no banco de dados, utilizar o método POST em http://127.0.0.1:8000/events/ e, em json, fornecer as informações como no exemplo abaixo:

{
	"event_key": 1,
	"Name": "A Dijiang",
	"Sex": "M",
	"Age": 24,
	"Height": 180,
	"Weight": 80,
	"Team": "China",
	"NOC": "CHN",
	"Games": "1992 Summer",
	"Year": 1992,
	"Season": "Summer",
	"City": "Barcelona",
	"Sport": "Basketball",
	"Event": "Basketball Men's Basketball",
	"Medal": "Gold"
}

- Para acessar algum evento específico: http://127.0.0.1:8000/events/id (substituir id pelo número de identificação do evento, que é a coluna referente à chave primária do banco de dados, não à event_key, que é um número único para o atleta);
- Para atualizar o evento, é só utilizar o mesmo caminho (http://127.0.0.1:8000/events/id) e utilizar o método PUT, informando os valores dos campos no mesmo formato do método POST;
- Para deletar o evento dado em http://127.0.0.1:8000/events/id, utilizar o método DELETE;
- Para preencher o banco de dados com a planilha 'athlete_events.csv', utilizar o método customizado 'FILL' em http://127.0.0.1:8000/events/.
