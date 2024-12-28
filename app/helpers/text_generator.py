def generate_response(data):
    if len(data) < 2:
        return "Not enough data to compare growth rates."

    comparisons = [f"{row['city']} has a growth rate of {row['growth_rate']}." for row in data]
    return " ".join(comparisons)
