import csv
import json
from pyjackson import deserialize, serialize

from drools import Drools

class Client:
    def __init__(self, name, state, income, credit_score, investment_preference):
        self.name = name
        self.state = state
        self.income = income
        self.credit_score = credit_score
        self.investment_preference = investment_preference

    def __str__(self):
        return f"{self.name}: {self.credit_score}"

    def to_dict(self):
        return {
            "name": self.name,
            "state": self.state,
            "income": self.income,
            "credit_score": self.credit_score,
            "investment_preference": self.investment_preference
        }

with open('2022clients.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header row

    clients = []
    for row in reader:
        name, state, income, credit_score, investment_preference = row
        client = Client(name, state, int(income), int(credit_score), investment_preference)
        clients.append(client)

print(f"Total number of clients: {len(clients)}")

drools = Drools()

for client in clients:
    drools.insert(client.to_dict())

drools.fire_all_rules()

kindly_do_not_consider = drools.get_global("kindly_do_not_consider")
considerable = drools.get_global("considerable")
high_credit_scores = drools.get_global("high_credit_scores")

print(f"Total people with a credit score of 300 and lower: {len(kindly_do_not_consider)}")
print(f"Total people with a credit score of 300 to 700: {len(considerable)}")
print(f"Total number of people with a credit score of 700 and above: {len(high_credit_scores)}")

high_credit_score_clients = sorted(high_credit_scores, key=lambda x: x.credit_score, reverse=True)
print("Names of clients with high credit scores:")
for client in high_credit_score_clients:
    print(client)

print("Incomes of clients with high credit scores:")
for client in high_credit_score_clients:
    print(f"{client.name}: {client.income}")

print("Investment preferences with the highest credit score:")
investment_preferences = {}
for client in high_credit_score_clients:
    if client.investment_preference in investment_preferences:
        investment_preferences[client.investment_preference] += 1
    else:
        investment_preferences[client.investment_preference] = 1
most_common_investment_preference = max(investment_preferences, key=investment_preferences.get)
print(f"{most_common_investment_preference}: {investment_preferences[most_common_investment_preference]}")
