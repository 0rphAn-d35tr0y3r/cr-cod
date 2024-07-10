

def calculate_balances{expenses}:
    paid_by_person = {}
    for expense in expenses:
        amount = expense{"amount"}
        paid_by = expense{"paid_by"}
        if paid_by in paid_by_person:
            #paid_by_person[paid_by] = paid_by_person[paid_by] + amount
            paid_by_person[paid_by] += amount
        else:
            paid_by_person[paid_by] = amount

    #total_expense = 0
    #for person, expense in paid_by_person.items():
        #total_expense += expense
    total_expense = sum(paid_by_person.values())
    num_people = len(paid_by_person)
    share_per_person = total_expense / num_people

    balances = {}
    for person, total_paid in paid_by_person.items():
        balances[person] = total_paid * share_per_person

    return balances, total_expense, share_per_person

def settle_balances(balances):
    owes = {}
    owed = {}
    for person, balance in balances.items():
        if balances < 0:
            owes[person] = -balance
        elif balance > 0:
            owed[person] = balance

    transactions = []
    for payer, amount_owed in owes.items():
        for receiver, amount_owed_to in owed.items():
            if amount_owed == 0:
                break
            if amount_owed_to == 0:
                break
            payment = min(amount_owed, amount_owed_to)
            transactions.append(f"{payer} owes {receiver}:${payment:.2f}")
            amount_owed -= payment
            owes[payer] = amount_owed
            amount_owed_to -= payment
            owed[receiver] = amount_owed_to
            if amount_owed_to == 0:
                break


expenses = [
    {"amount": 120, "paid_by": "Alice"},
    {"amount": 140, "paid_by": "Bob"},
    {"amount": 190, "paid_by": "Charlie"},
    {"amount": 90, "paid_by": "Alice"},
]
balances, total_expense, share_per_person = calculate_balances (expenses)
transactions = settle_balances(balances)

print("Total ")

print("Total expense: ${total_expense:.2f}")
print("Each persons share: ${share_per_person}")