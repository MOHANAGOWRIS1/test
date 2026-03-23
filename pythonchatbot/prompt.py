from langchain_core.prompts import ChatPromptTemplate
 
# Define template with roles
template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "Explain {concept} in simple terms."),
])
 
# Invoke with variables
prompt_value = template.invoke({"concept": "AI computing"})
print(prompt_value)