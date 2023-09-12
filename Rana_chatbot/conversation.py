import pandas as pd

reqs = {
    "national_id": "Please provide your national ID",
    "last_name": "Please provide your last name",
    "phone_number": "Please provide your phone number"
}

def validate_credentials(national_id, last_name, phone_number):
    patients_data = pd.read_csv('databases/general_databases/patients_data.csv', 
                                dtype={'phone_number': str, 'national_ID': str})
    # Remove hyphens from phone numbers in the CSV file
    patients_data['phone_number'] = patients_data['phone_number'].str.replace('-', '')

    # Remove hyphens from the input phone number
    phone_number = phone_number.replace('-', '')

    matching_patient = patients_data[
        (patients_data['national_ID'] == national_id) &
        (patients_data['last_name'].str.lower() == last_name.lower()) &
        (patients_data['phone_number'] == phone_number)
    ]

    if matching_patient.empty:
        return False, None
    else:
        return True, matching_patient['File_number'].values[0]


def continue_conversation(user_data, message):
    for k in reqs.keys():
        if k not in user_data:
            user_data[k] = None
            return "text", reqs[k]
        elif user_data[k] is None:
            user_data[k] = message
    
    if "tries" not in user_data:
        user_data["tries"] = 1
    is_valid, file_number = validate_credentials(
        user_data["national_id"], user_data["last_name"], user_data["phone_number"]
    )
    if is_valid:
        if "file_number" not in user_data:
            user_data["file_number"] = file_number
            return "text", "Thank you for providing your details."
        else:
            return None, None
    else:
        for k in reqs.keys():
            del user_data[k]
        if "tries" not in user_data:
            user_data["tries"] = 1
        else:
            user_data["tries"] += 1
        if user_data["tries"] > 3:
            return "text", "Your details still doesn't match our data, you may not be registered at our hospital. If you think there is something wrong, please contact our IT team at 0555555553."
        return "text", "I'm afraid your details doesn't match our data, please make sure you're using the correct details then try again."

