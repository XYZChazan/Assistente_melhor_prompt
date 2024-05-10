import google.generativeai as genai  
import os  
from termcolor import colored  

# Configura a API do Gemini com a chave de API obtida do ambiente
genai.configure(api_key=os.environ["API_KEY"])

# Define as instruções para o modelo de IA, explicando seu papel como melhorador de prompts
system_instructions = """
Você é um engenheiro de prompt especializado em auxiliar usuários a criar prompts eficazes para modelos de IA. 
Seus objetivos são:
* Aprimorar a clareza e o contexto dos prompts.
* Utilizar técnicas como Few-Shot Prompting, Chain-of-Thought Prompting, Prompt Decomposition, Instruções de Sistema, dentre outros.
* Dar exemplos de melhorias que podem ser implementadas.
"""

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", system_instruction=system_instructions)

print('Bem-vindo ao seu assistente de aprimoramento de prompt :)')

# Lista para armazenar as mensagens da conversa
mensagens = []

# Função para gerar texto usando a API do Gemini e colorir as mensagens
def geracao_texto(mensagens_chat):
    historico = ""  # String para armazenar o histórico da conversa
    for mensagem in mensagens_chat:
        # Define a cor da mensagem com base no papel (usuário ou assistente)
        cor = 'blue' if mensagem['role'] == 'user' else 'green' 
        # Adiciona a mensagem colorida ao histórico
        historico += colored(f"{mensagem['role']}: {mensagem['content']}\n", cor)
    # Gera texto com o modelo do Gemini usando o histórico da conversa
    response = model.generate_content(historico)
    # Adiciona a resposta do assistente à lista de mensagens
    mensagens_chat.append({'role': 'assistant', 'content': response.text})
    # Retorna a lista de mensagens atualizada
    return mensagens_chat

# Loop principal do chatbot
while True:
    # Obtém a entrada do usuário e colore o prompt
    input_usuario = input(colored('User: ', 'blue'))
    # Verifica se o usuário digitou "fim" para encerrar a conversa
    if input_usuario.lower() == "fim":
        break
    # Adiciona a mensagem do usuário à lista de mensagens
    mensagens.append({'role': 'user', 'content': input_usuario})
    # Gera a resposta do assistente e atualiza a lista de mensagens
    mensagens = geracao_texto(mensagens)
    # Imprime a resposta do assistente com a cor verde
    print(colored(f"Assistant: {mensagens[-1]['content']}", 'green'))

print("Chatbot finalizado.")