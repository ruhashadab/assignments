import json

with open('superheroes.json', 'r') as f:
    squad = json.load(f)
    

powers = []

members = squad['members']
for member in members:

	powers.append(member["powers"])

print(powers)
