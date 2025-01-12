from faker import Faker
import random


class DataGenerator:
    """Генератор данных для тестов"""
    
    @staticmethod
    def generate_random_data():
        """Генерация случайных валидных данных для тестов"""
        fake = Faker()
        return {
            "email": fake.email(),
            "names": fake.name(),
            "message_text": fake.text(),
        }

    @staticmethod
    def generate_invalid_email_rejected():
        """Генерация невалидных email-адресов, которые ожидаемо вызывают валидацию"""
        fake = Faker()
        invalid_formats = [
            "plainaddress",
            "missingatsign.com",
            "@missingusername.com",
            "missingdomain@.com",
            f"{fake.user_name()}@{fake.domain_word()}.",  # Пропущен TLD (например, ".com")
        ]
        
        return random.choice(invalid_formats)

    @staticmethod
    def generate_invalid_email_accepted_by_bug():
        """Генерация невалидных email-адресов, которые сайт ошибочно принимает"""
        fake = Faker()
        invalid_but_accepted_formats = [
            f"{fake.user_name()}@{fake.domain_word()}com",  # Пропущена точка перед TLD
            f"{fake.user_name()}@нафаня.ку",  # Кириллический домен
            f"{fake.user_name()}@пример.рф",  # Еще один кириллический домен
            f"{fake.user_name()}@{fake.domain_name()} ",  # Лишний пробел в конце
            f" {fake.user_name()}@{fake.domain_name()}",  # Лишний пробел в начале
            f" {fake.user_name()}@{fake.domain_name()} ",  # Лишние пробелы с двух сторон
        ]

        return random.choice(invalid_but_accepted_formats)
