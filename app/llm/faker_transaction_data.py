import json
import random
from datetime import datetime, timedelta

from faker import Faker

fake = Faker("nl_NL")  # Use Dutch locale


def generate_persona():
    return {
        "name": fake.name(),
        "age": random.randint(25, 75),
        "occupation": fake.job(),
        "familyStatus": random.choice(["Single", "Married", "Divorced", "Widowed"]),
        "background": fake.text(max_nb_chars=200),
        "previouslyFlagged": random.choice([True, False]),
    }


def generate_financial_profile():
    monthly_income = random.randint(2000, 10000)
    return {
        "monthlyIncome": monthly_income,
        "savingsBalance": random.randint(1000, 100000),
        "investmentPortfolio": {
            "hasInvestments": random.choice([True, False]),
            "investmentAmount": random.randint(5000, 500000)
            if random.random() > 0.5
            else None,
        },
    }


def generate_transaction(start_date, end_date):
    transaction_date = fake.date_between(start_date=start_date, end_date=end_date)
    is_incoming = random.random() < 0.3  # 30% chance of incoming transaction
    amount = random.uniform(1, 5000) if is_incoming else -random.uniform(1, 100)

    dutch_stores = [
        "Albert Heijn",
        "Jumbo",
        "Lidl",
        "Aldi",
        "HEMA",
        "Blokker",
        "Kruidvat",
        "Action",
        "MediaMarkt",
    ]
    dutch_banks = ["ING", "Rabobank", "ABN AMRO", "SNS Bank", "Triodos Bank"]

    if random.random() < 0.95:  # 95% chance of domestic transaction
        country = "Netherlands"
        if is_incoming:
            merchant = random.choice(dutch_banks)
        else:
            merchant = random.choice(dutch_stores)
    else:
        country = fake.country()
        merchant = fake.company()

    return {
        "date": transaction_date.strftime("%Y-%m-%d"),
        "description": fake.bs(),
        "amount": round(amount, 2),
        "country": country,
        "merchant": merchant,
        "type": "incoming" if is_incoming else "outgoing",
    }


def generate_suspicious_activity():
    return {
        "types": [
            "Frequent transactions with entities in high-risk countries",
            "Large international transfers",
            "Varying transaction amounts to avoid detection",
        ],
        "amounts": [random.randint(5000, 30000) for _ in range(3)],
        "frequencies": [random.randint(1, 5) for _ in range(3)],
        "timing": [fake.month_name() + " " + str(fake.year()) for _ in range(3)],
        "pattern": "Multiple large transactions with entities in countries known for financial risks. The varying transaction amounts seem designed to avoid detection.",
    }


def generate_analyst_decision():
    return {
        "action": random.choice(["escalate", "close"]),
        "keyFactors": [
            "Repeated transactions with high-risk countries",
            "Transaction amounts disproportionate to monthly income",
            "Suspicious pattern of inconsistent amounts to avoid detection",
            "Lack of clear business justification for large international transfers",
        ],
    }


def generate_auxiliary_data():
    return {
        "dailyExpenses": random.randint(1000, 2000),
        "housing": random.randint(1000, 2000),
        "transportation": random.randint(200, 500),
        "healthcare": random.randint(100, 300),
        "entertainment": random.randint(300, 800),
        "savingsInvestments": random.randint(500, 2000),
        "internationalTransfers": random.randint(5000, 15000),
        "cashWithdrawalsDeposits": random.randint(500, 1000),
    }


def generate_kyc_test_scenario():
    persona = generate_persona()
    financial_profile = generate_financial_profile()

    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)  # 6 months of data

    transactions = [
        generate_transaction(start_date, end_date) for _ in range(60)
    ]  # Generate 60 transactions

    suspicious_activity = generate_suspicious_activity()
    analyst_decision = generate_analyst_decision()

    difficulty_level = {
        "level": random.choice(["easy", "medium", "hard"]),
        "score": random.randint(1, 10),
    }

    auxiliary_data = generate_auxiliary_data()

    context = f"This is a {difficulty_level['level']} difficulty scenario involving a {persona['occupation']} with suspicious transaction patterns. {suspicious_activity['pattern']}"

    return {
        "persona": persona,
        "financialProfile": financial_profile,
        "transactionData": transactions,
        "suspiciousActivity": suspicious_activity,
        "context": context,
        "analystDecision": analyst_decision,
        "difficultyLevel": difficulty_level,
        "auxiliaryData": auxiliary_data,
    }


# Generate a KYC test scenario
scenario = generate_kyc_test_scenario()

# Print the generated scenario
print(json.dumps(scenario, indent=2))
