from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Razão simples
print(fuzz.ratio("this is a test", "this is a test!"))

# Razão parcial
print(fuzz.partial_ratio("this is a test", "this is a test!"))

# Processos
    # Procura as maiores correspondências
choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
print(process.extract("new york jets", choices, limit=2))
print(process.extractOne("cowboys", choices))