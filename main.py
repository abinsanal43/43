from src.db_helpers import add_provider, get_providers

# Add a new provider
add_provider(
    name="Fresh Foods",
    type_="Grocery",
    address="123 Market Street",
    city="Bangalore",
    contact="9876543210"
)

# Fetch all providers
providers = get_providers()
for p in providers:
    print(p)
