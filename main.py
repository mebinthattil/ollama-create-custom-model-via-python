import ollama
import subprocess

#getting user input
if input("\n\nBase model is llama3.1, do you want to change it? [y/n]: ") == 'y':
    base_model = input("Enter base model: ")
else:
    base_model = 'llama3.1'
sys_prompt = input('Enter system prompt: ')
model_name = input('Enter model name: ')

#creating model
modelfile =f'''
FROM {base_model}
SYSTEM {sys_prompt}
''' 
ollama.create(model=model_name, modelfile=modelfile)

#confirming if model is created
command = "ollama list"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
output = result.stdout

if model_name in output:
    print(f"\n\nModel {model_name} created successfully!")
else:
    print(f"\n\nModel {model_name} might not have been created")
