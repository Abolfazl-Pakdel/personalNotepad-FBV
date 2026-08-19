from django.core.management.base import BaseCommand
from faker import Faker
import random
from django.contrib.auth.models import User
from ...models import Note


class Command(BaseCommand):

    help = "Create 5 fake notes with random complete status"

    def handle(self, *args, **kwargs):

        fake = Faker()

        for _ in range(5):

            Note.objects.create(
                user = User.objects.create_user(username=fake.user_name(),password="test@1234567"),
                title=fake.sentence(nb_words=4),
                content=fake.sentence(nb_words=5),
                is_pinned=random.choice([True, False])
            )

        self.stdout.write(
            self.style.SUCCESS("5 fake notes created successfully!")
        )