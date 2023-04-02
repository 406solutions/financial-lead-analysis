from drools.ruleunit import RuleUnit
from drools.ruleunit import ruleunit
from drools import Client

@ruleunit(RuleUnit)
class ClientRules:
    def __init__(self, clients):
        self.clients = clients

    def execute(self, results):
        for client in self.clients:
            if client.age >= 18 and client.income >= 50000:
                client.is_eligible = True
                client.reason = 'Age and income meet eligibility criteria'
            elif client.age >= 18 and client.income < 50000:
                client.is_eligible = False
                client.reason = 'Income does not meet eligibility criteria'
            elif client.age < 18 and client.income >= 50000:
                client.is_eligible = False
                client.reason =
