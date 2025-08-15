from db_helpers import get_providers, add_provider

add_provider("Test Provider", "Restaurant", "123 Street", "Kochi", "9876543210")
print(get_providers())
