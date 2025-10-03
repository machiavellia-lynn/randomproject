import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

num_players = 1_000_000 # total of players

# Datasets
age_range = (10, 50)

gender = ["male", "female", "rather not say"]
gender_weights = [0.5, 0.2, 0.3]

rank = ["Bronze I", "Bronze II", "Bronze III", "Silver I", "Silver II", "Silver III",
        "Gold I", "Gold II", "Gold III", "Diamond I", "Diamond II", "Diamond III",
        "Platinum", "Immortal"]
rank_weights = [0.15, 0.13, 0.1, 0.1, 0.1, 0.2, 0.08, 0.05, 0.04, 0.02, 0.02, 0.02, 0.01, 0.01]

main_role = ["Assassin", "Mage", "Archer", "Necromancer", "Tank", "Healer", "Fighter"]
main_role_weights = [0.22, 0.15, 0.13, 0.05, 0.15, 0.1, 0.2]

server = ["Asia", "Europe", "America", "SEA"]
server_weights = [0.4, 0.2, 0.1, 0.3]  # Lebih banyak pemain di Asia & SEA

diamond_range = [0, 1, 2, 3, 4, 5]
diamond_weights = [0.5, 0.2, 0.15, 0.08, 0.05, 0.02]  # Mayoritas pemain punya 0-2 diamond

countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan",
             "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Malaysia", "Bolivia",
             "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada",
             "Cape Verde", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia",
             "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
             "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
             "Indonesia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti"]

nations = ["Pyrralis", "Aquenara", "Terranova", "Aetherion", "Noctharys"]
nation_weights = [0.3, 0.25, 0.22, 0.17, 0.05]

# Pembobotan level
level_ranges = list(range(1, 101))  # Level dari 1 sampai 100
level_weights = [0.5 if 1 <= x <= 30 else 0.35 if 31 <= x <= 70 else 0.15 for x in level_ranges]

# Function to generate a random date within a range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Function to generate a player's active status over the years
def generate_active_status(join_date):
    years = range(2015, 2026)
    status_options = ["Active", "Not Active", "Banned"]
    active_status = {}

    for year in years:
        if year < join_date.year:
            active_status[f"Status_{year}"] = "Not Joined Yet"
        else:
            active_status[f"Status_{year}"] = random.choice(status_options)

    return active_status

# Function to generate player data
def generate_data():
    data = {
        "ID": list(range(1, num_players + 1)),
        "Username": [fake.user_name() for _ in range(num_players)],
        "Gender" : random.choices(gender, weights=gender_weights, k=num_players),
        "Nationality": random.choices(countries, k=num_players),
        "Age": [random.randint(age_range[0], age_range[1]) for _ in range(num_players)],
        "Rank": random.choices(rank, weights=rank_weights, k=num_players),
        "Main Role": random.choices(main_role, weights=main_role_weights, k=num_players),
        "KDA": [round(random.uniform(1.0, 4.0), 2) for _ in range(num_players)],
        "Account Level": random.choices(level_ranges, weights=level_weights, k=num_players),
        "Server": random.choices(server, weights=server_weights, k=num_players),
        "Diamond": random.choices(diamond_range, weights=diamond_weights, k=num_players),
    }

    # Generate join dates
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2025, 12, 31)
    join_dates = [random_date(start_date, end_date) for _ in range(num_players)]
    data["Join Date"] = [date.strftime("%Y-%m-%d") for date in join_dates]

    # Topup status
    data["Topup"] = ["yes" if diamonds > 0 else "no" for diamonds in data["Diamond"]]

    # Coins based on level
    data["Coins"] = [random.randint(5000, 50000) if lvl < 30 else
                     random.randint(50000, 200000) if lvl < 70 else
                     random.randint(200000, 6000000)
                     for lvl in data["Account Level"]]

    # Player's current nation
    data["Current Nation"] = random.choices(nations, weights=nation_weights, k=num_players)

    # Generate active status per year
    active_status_data = [generate_active_status(join_date) for join_date in join_dates]
    for year in range(2015, 2026):
        data[f"Status_{year}"] = [status[f"Status_{year}"] for status in active_status_data]

    return pd.DataFrame(data)

# Write Data to CSV
file_name = "playerdata.csv"
df = generate_data()
df.to_csv(file_name, index=False)

print(f"Successfully saved {num_players} rows to {file_name}!")
