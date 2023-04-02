import csv
from python_drools_sdk.commands.insert_object_command import InsertObjectCommand
from python_drools_sdk.kie.drools import Drools
from drools import Client, RuleUnit

# Set configuration variables for your Drools server
Drools.KIE_SERVER_CONTAINER_PACKAGE = 'com.sample'
Drools.KIE_SERVER_USERNAME = 'your_kie_server_username'
Drools.KIE_SERVER_PASSWORD = 'your_kie_server_password'
Drools.KIE_SERVER_ROOT_URL = 'your_kie_server_url'
Drools.KIE_SERVER_CONTAINER_ID = 'your_kie_container_id'
Drools.KIE_SESSION_NAME = 'your_kie_session_name'

# Load client data from CSV file
with open('2022clients.csv', 'r') as file:
    reader = csv.DictReader(file)
    clients = [Client(**row) for row in reader]


# Create a RuleUnit object to run rules on the client data
@ruleunit(RuleUnit)
class ClientRules:
    def __init__(self, clients):
        self.clients = clients

    def execute(self, results):
        for client in self.clients:
            command = InsertObjectCommand(object=client, out_identifier=str(client.id))
            Drools.add_command(command)

        response = Drools.execute_commands()

        for client in self.clients:
            response_client = response[str(client.id)]
            client.is_eligible = response_client['is_eligible']
            client.reason = response_client['reason']


# Run the rules on the client data
rules = ClientRules(clients)
rules.execute(None)

# Print the updated client data
for client in clients:
    print(client)
