from faker import Faker
import time
import random
from dataclasses import dataclass
fake = Faker()

@dataclass()
class Random_user:
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name}_{last_name}_{time.time()}@{fake.domain_name()}"
    gender = random.choice(["male", "female"])
    status = random.choice(["active", "inactive"])
    random_title = fake.paragraph(nb_sentences=1)
    random_body = fake.paragraph(nb_sentences=5)
