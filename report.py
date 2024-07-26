
def generate_report(transactions):
    report = {}
    for transaction in transactions:
        if transaction.category not in report:
            report[transaction.category] = 0
        report[transaction.category] += transaction.amount
    return report

def print_report(report):
    for category, amount in report.items():
        print(f"Category: {category}, Total: {amount}")
