# 🧠 Teste de Personalidade - Big Five

Um protótipo de teste de personalidade baseado no modelo dos **Cinco Grandes Fatores** (Big Five), que avalia a porcentagem de cada traço emocional em um indivíduo. O sistema é desenvolvido com **Django, HTML e CSS**.

## 🚀 Funcionalidades
- 📊 **Avaliação personalizada**: Responda perguntas e obtenha um perfil com as porcentagens dos 5 grandes traços de personalidade.
- 🎨 **Interface intuitiva**: Design simples e acessível para facilitar o uso.
- 🗃️ **Armazenamento de resultados**: Salve e consulte avaliações passadas.
- ⚡ **Desenvolvido com Django**: Utiliza um backend robusto para processar e armazenar respostas.

## 🏗️ Tecnologias Utilizadas
- **Python** + **Django** 🐍 - Backend
- **HTML5** + **CSS3** 🎨 - Frontend
- **SQLite** (ou outro banco de dados) 🗄️ - Armazenamento de respostas

## 🎯 Como Rodar o Projeto
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/teste-personalidade.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd teste-personalidade
   ```
3. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
5. Aplique as migrações:
   ```sh
   python manage.py migrate
   ```
6. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```
7. Acesse no navegador:
   ```
   http://127.0.0.1:8000/
   ```

## 📌 Estrutura do Projeto
```
teste-personalidade/
│── core/                 # Aplicação principal
│   ├── models.py         # Modelos do banco de dados
│   ├── views.py          # Lógica das páginas
│   ├── urls.py           # Rotas da aplicação
│── templates/            # Templates HTML
│── static/               # Arquivos CSS e JS
│── db.sqlite3            # Banco de dados SQLite
│── manage.py             # Gerenciador do Django
│── requirements.txt      # Dependências do projeto
```

## 🔥 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um **pull request** ou relatar **issues**. 🚀

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário. 📝

