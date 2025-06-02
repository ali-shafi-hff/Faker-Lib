import mysql.connector
from faker import Faker

# Use German locale for region-specific names
# Setup
fake = Faker('de_DE')
Faker.seed(42)

#fake = Faker()
#Faker.seed(0)  # Optional: ensures repeatability

# Connect to your MySQL DB
conn = mysql.connector.connect(
    host='localhost',
    user='externteam',
    password='externteamdb12!',
    database='ExternLta'
)
cursor = conn.cursor()

# Fetch all person IDs
cursor.execute("SELECT Id FROM Persons")
ids = [row[0] for row in cursor.fetchall()]

# Loop through all IDs and anonymize
for person_id in ids:
    data = {
        'FirstName': fake.first_name(),
        'LastName': fake.last_name(),
        'NickName': fake.user_name(),
        'BirthName': fake.name(),
        'EmailPvt': fake.email(),
        'EmailWork': fake.company_email(),
        'EmailOther': fake.email(),
        'PhoneNum1': fake.phone_number(),
        'PhoneNum2': fake.phone_number(),
        'PhoneNumPvt1': fake.phone_number(),
        'PhoneNumPvt2': fake.phone_number(),
        'PhoneNumWork1': fake.phone_number(),
        'PhoneNumWork2': fake.phone_number(),
        'PhoneNumCompany': fake.phone_number(),
        'FaxNumWork': fake.phone_number(),
        'FaxNumPvt': fake.phone_number(),
        'StreetPvt': fake.street_address(),
        'PostCodePvt': fake.postcode(),
        'CityPvt': fake.city(),
        'StatePvt': fake.state(),
        'CountryPvt': fake.country(),
        'StreetWork': fake.street_address(),
        'PostCodeWork': fake.postcode(),
        'CityWork': fake.city(),
        'StateWork': fake.state(),
        'CountryWork': fake.country(),
        'StreetOther': fake.street_address(),
        'PostCodeOther': fake.postcode(),
        'CityOther': fake.city(),
        'StateOther': fake.state(),
        'CountryOther': fake.country(),
        'Company': fake.company(),
        'Website': fake.url(),
        'Note': fake.text(max_nb_chars=200)
    }

    query = """
    UPDATE Persons SET
        FirstName = %s,
        LastName = %s,
        NickName = %s,
        BirthName = %s,
        EmailPvt = %s,
        EmailWork = %s,
        EmailOther = %s,
        PhoneNum1 = %s,
        PhoneNum2 = %s,
        PhoneNumPvt1 = %s,
        PhoneNumPvt2 = %s,
        PhoneNumWork1 = %s,
        PhoneNumWork2 = %s,
        PhoneNumCompany = %s,
        FaxNumWork = %s,
        FaxNumPvt = %s,
        StreetPvt = %s,
        PostCodePvt = %s,
        CityPvt = %s,
        StatePvt = %s,
        CountryPvt = %s,
        StreetWork = %s,
        PostCodeWork = %s,
        CityWork = %s,
        StateWork = %s,
        CountryWork = %s,
        StreetOther = %s,
        PostCodeOther = %s,
        CityOther = %s,
        StateOther = %s,
        CountryOther = %s,
        Company = %s,
        Website = %s,
        Note = %s
    WHERE Id = %s
"""

# Arrange values in the same order as placeholders
values = (
    data['FirstName'], data['LastName'], data['NickName'], data['BirthName'],
    data['EmailPvt'], data['EmailWork'], data['EmailOther'],
    data['PhoneNum1'], data['PhoneNum2'], data['PhoneNumPvt1'], data['PhoneNumPvt2'],
    data['PhoneNumWork1'], data['PhoneNumWork2'], data['PhoneNumCompany'],
    data['FaxNumWork'], data['FaxNumPvt'],
    data['StreetPvt'], data['PostCodePvt'], data['CityPvt'], data['StatePvt'], data['CountryPvt'],
    data['StreetWork'], data['PostCodeWork'], data['CityWork'], data['StateWork'], data['CountryWork'],
    data['StreetOther'], data['PostCodeOther'], data['CityOther'], data['StateOther'], data['CountryOther'],
    data['Company'], data['Website'], data['Note'],
    person_id  # Final value is the ID for WHERE clause
)

cursor.execute(query, values)

# Commit changes
conn.commit()
cursor.close()
conn.close()
print("Anonymization completed.")