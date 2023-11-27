import pandas as pd
from django.core.management.base import BaseCommand
from accounts.models import Customer, Agent
from messaging.models import Message, Response
from faker import Faker


class Command(BaseCommand):
    help = 'Import messages from XLSX file'

    def handle(self, *args, **options):
        file_path = './GeneralistRails_Project_MessageData.xlsx'  # Update with your file path

        # Read XLSX file into a DataFrame
        df = pd.read_excel(file_path, engine='openpyxl')

        # Create an instance of Faker
        fake = Faker()

        # Iterate over rows and create Message and Response objects
        for index, row in df.iterrows():
            # Use Faker to generate a random name
            fake_name = fake.name()

            # Create a new Customer if not exists
            customer, created = Customer.objects.get_or_create(
                pk=row['user_id'],
                defaults={'name': fake_name}
            )

            # agent = Agent.objects.first()  # You need to adjust this to select the appropriate agent
            message = Message.objects.create(customer=customer, content=row['message'], timestamp=row['timestamp'])

            # You may need to adjust the response creation logic based on your data
            # In this example, a Response is not created for each message
            # You may have a separate data source for responses or adjust this logic accordingly

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

# # messaging/management/commands/import_messages.py
# import pandas as pd
# from django.core.management.base import BaseCommand
# from accounts.models import Customer, Agent
# from messaging.models import Message, Response
# from faker import Faker
#
# class Command(BaseCommand):
#     help = 'Import messages from XLSX file'
#
#     def handle(self, *args, **options):
#         file_path = './GeneralistRails_Project_MessageData.xlsx'  # Update with your file path
#
#         # Read XLSX file into a DataFrame
#         df = pd.read_excel(file_path, engine='openpyxl')
#
#         # Create an instance of Faker
#         fake = Faker()
#
#         # Iterate over rows and create Message and Response objects
#         for index, row in df.iterrows():
#             # Use Faker to generate a random name
#             fake_name = fake.name()
#
#             # Create a new Customer if not exists
#             customer, created = Customer.objects.get_or_create(
#                 pk=row['user_id'],
#                 defaults={'name': fake_name}
#             )
#
#             agent = Agent.objects.first()  # You need to adjust this to select the appropriate agent
#             message = Message.objects.create(customer=customer, content=row['message'], timestamp=row['timestamp'])
#
#             # You may need to adjust the response creation logic based on your data
#             Response.objects.create(agent=agent, message=message, content="Your response here", timestamp=row['timestamp'])
#
#         self.stdout.write(self.style.SUCCESS('Data imported successfully'))
#


# # messaging/management/commands/import_messages.py
# import pandas as pd
# from django.core.management.base import BaseCommand
# from accounts.models import Customer, Agent
# from messaging.models import Message, Response
#
# class Command(BaseCommand):
#     help = 'Import messages from XLSX file'
#
#     def handle(self, *args, **options):
#         file_path = './GeneralistRails_Project_MessageData.xlsx'  # Update with your file path
#
#         # Read XLSX file into a DataFrame
#         df = pd.read_excel(file_path, engine='openpyxl')
#
#         # Iterate over rows and create Message and Response objects
#         for index, row in df.iterrows():
#             customer = Customer.objects.get(pk=row['user_id'])  # Assuming 'user_id' is the column name in your XLSX file
#             agent = Agent.objects.first()  # You need to adjust this to select the appropriate agent
#             message = Message.objects.create(customer=customer, content=row['message'], timestamp=row['timestamp'])
#
#             # You may need to adjust the response creation logic based on your data
#             Response.objects.create(agent=agent, message=message, content="Your response here", timestamp=row['timestamp'])
#
#         self.stdout.write(self.style.SUCCESS('Data imported successfully'))
