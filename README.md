<h1>🤖 ChatBot com API Gemini</h1>

Esse projeto é um chatbot criado com python como linguagem principal e framework Flask para interface web, utilizando a API da inteligência arficial do Google, o Gemini. Ele foi desenvolvido a partir da imersão de IA da Alura com o Google.

---
<h2>📚 Bibliotecas usadas</h2>
<ul>
    <li>google.generativeai - SDK do google para fazer integração com a API do Gemini</li>
    <li>dotenv - biblioteca para o armazenamento de variáveis de ambiente</li>
    <li>markdown - biblioteca para o tratamento de arquivos do tipo markdown</li> 
</ul>

---

<h2>⚙️ Como executar</h2>
Baixe o repositório na sua máquina e abra o terminal no diretório.  Crie o ambiente .venv de desenvolvimento:

<code>py -3 -m venv .venv</code>

Depois, ative o ambiente com o seguinte comando:
<code>py -3 -m venv .venv</code>

Instale o Flask com o ambiente ativado:
<code>pip install Flask</code>

No diretório raiz do projeto, crie um arquivo .env e adicione a API key do Gemini, que pode ser gerada <a href="https://aistudio.google.com/app/apikey">aqui</a> (você deve ter uma conta do google para isso):
<code>GOOGLE_API_KEY="sua_chave_aqui"</code>

Inicialize o projeto:
<code>python -m flask run</code>

Divirta-se :)

<strong>ps:</strong> se quiser mais informações sobre o funcionamento da API, acesse https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br&lang=python