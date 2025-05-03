from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import chat_agent_executor
from langchain.tools import tool
from dotenv import load_dotenv
import yfinance as yf

load_dotenv()

# 📊 Ferramenta de consulta à ação
@tool
def consultar_preco_acao(ticker: str) -> str:
    """Retorna o preço atual de uma ação com base no código do ativo (ex: VALE3.SA, AAPL)."""
    try:
        acao = yf.Ticker(ticker)
        preco = acao.history(period="1d")["Close"].iloc[-1]
        return f"O preço atual da ação {ticker.upper()} é R$ {preco:.2f}."
    except Exception as e:
        return f"Erro ao consultar o preço da ação {ticker}: {e}"

# 🤖 Modelo
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# ✅ Executor do agente com LangGraph
agent_executor = chat_agent_executor.create_tool_calling_executor(
    tools=[consultar_preco_acao],
    model=llm
)

# Mensagens iniciais
mensagens = [
    SystemMessage(content="Você é um assistente financeiro. Quando o usuário perguntar sobre o valor de uma ação, como VALE3.SA ou AAPL, use a ferramenta 'consultar_preco_acao'.")
]

# 💬 Loop de interação
if __name__ == "__main__":
    print("📈 Bem-vindo ao Chat Financeiro com Yahoo Finance!")

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("👋 Encerrando o agente.")
            break

        mensagens.append(HumanMessage(content=pergunta))

        try:
            resposta = agent_executor.invoke({"messages": mensagens})

            # ✅ Captura corretamente a última mensagem do agente
            if "messages" in resposta and isinstance(resposta["messages"][-1], AIMessage):
                ultima_resposta = resposta["messages"][-1]
                mensagens.append(ultima_resposta)
                print("Assistant:", ultima_resposta.content)
            else:
                print("❌ Erro: Resposta inesperada do agente.")
                print("Conteúdo completo da resposta:", resposta)
        except Exception as e:
            print(f"❌ Ocorreu um erro: {e}")









