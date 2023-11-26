# myapp/management/commands/generate_fake_data.py
from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import CustomUser, Agent, Customer

fake = Faker()


class Command(BaseCommand):
    help = 'Generate fake data for agents and customers'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Generating fake data...'))

        # Generate 50 agents
        for _ in range(50):
            agent_name = fake.name()
            agent = Agent.objects.create(name=agent_name)
            CustomUser.objects.create(username=agent_name, name=agent_name, agent=agent)

        # Generate 100 customers
        for _ in range(100):
            customer_name = fake.name()
            customer = Customer.objects.create(name=customer_name)
            CustomUser.objects.create(username=customer_name, name=customer_name, customer=customer)

        self.stdout.write(self.style.SUCCESS('Fake data generated successfully!'))
