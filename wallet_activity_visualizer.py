import random
from datetime import datetime, timedelta

def generate_mock_activity(days=30):
    return [
        {
            "date": (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d"),
            "tx_count": random.randint(0, 10),
            "eth_spent": round(random.uniform(0.01, 0.5), 4)
        }
        for i in range(days)
    ]

def main():
    activity = generate_mock_activity()
    for entry in activity:
        print(f"{entry['date']}: {entry['tx_count']} txs, {entry['eth_spent']} ETH")

if __name__ == "__main__":
    main()
