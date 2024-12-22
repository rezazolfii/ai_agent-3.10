from llama_index.llms.ollama import Ollama


llm = Ollama(model = "mistral", request_timeout = 60.0)
result = llm.complete("i want to buy sunscreen where can i buy it?")
print(result)
