import pandas as pd
from datetime import datetime

def __date_picker_response(text):
    return ("date", text)


def book_appointment(user_data):
    # Placeholder code
    return __date_picker_response("""To book an appointment please visit <link> ,
    Is there anything else?""")

def cancel_appointment(user_data):
    # Placeholder code
    return """to cancel an appointment please visit <link> ,
    Is there anything else?"""

def reschedule_appointment(user_data):
    # Placeholder code
    return """to reschedule an appointment please visit <link>
    Is there anything else?"""

def view_upcoming_appointments(user_data):
    file_number = user_data["file_number"]
    file_path = f"databases/patient_files/{file_number}.csv"
    patient_data = pd.read_csv(file_path)
    
    # convert the 'date' column to datetime format
    patient_data['date'] = pd.to_datetime(patient_data['date'], format='%d/%m/%Y')

    # today's date
    today = pd.to_datetime(datetime.today().strftime('%Y-%m-%d'))

    # filter the appointments later than today
    upcoming_appointments = patient_data[patient_data['date'] > today]

    if upcoming_appointments.empty:
        return "It shows that you don't have any upcoming appointments."
    else:
        response_text = "You have the following upcoming appointments:\n"
        for index, appointment in upcoming_appointments.iterrows():
            response_text += f"{appointment['date'].strftime('%Y-%m-%d')}, {appointment['day']} at {appointment['time']} with {appointment['doctor']} for {appointment['purpose_(note)']}\n"
        return response_text

def view_appointment_history(user_data):
    file_number = user_data["file_number"]
    file_path = f"databases/patient_files/{file_number}.csv"
    patient_data = pd.read_csv(file_path)
    
    # convert the 'date' column to datetime format
    patient_data['date'] = pd.to_datetime(patient_data['date'], format='%d/%m/%Y')

    # today's date
    today = pd.to_datetime(datetime.today().strftime('%Y-%m-%d'))

    # filter the appointments earlier than or on today
    past_appointments = patient_data[patient_data['date'] <= today]

    if past_appointments.empty:
        return "It shows that you don't have any past appointments."
    else:
        response_text = "You have the following past appointments:\n"
        for index, appointment in past_appointments.iterrows():
            response_text += f"{appointment['date'].strftime('%Y-%m-%d')}, {appointment['day']} at {appointment['time']} with {appointment['doctor']} for {appointment['purpose_(note)']} which you {appointment['status']} \n"
        return response_text


def medication_refill(user_data):
    # Placeholder code
    print("to request a medication refill, please visit the following link <link>")
    return "Is there anything else?"

def __load_medication_data(file_number):
    file_path = f"databases/patient_medication/{file_number}_medication.csv"
    df = pd.read_csv(file_path)
    return df

def current_medication(user_data):
    file_number = user_data["file_number"]
    df = __load_medication_data(file_number)
    current_med_df = df[df['status'] == 'current']
    
    result_text = "Your current medications are:\n"
    print("current_med_df: ", current_med_df)
    for i, row in current_med_df.iterrows():
        print("row: ", row)
        result_text += row['medication_name'] + "\n"
    return result_text

def medication_dose(user_data):
    file_number = user_data["file_number"]
    df = __load_medication_data(file_number)
    current_med_df = df[df['status'] == 'current']
    
    result_text = "The medication doses are as follows:\n"
    for i, row in current_med_df.iterrows():
        result_text += f"{row['medication_name']} : {row['dose']}\n"
    return result_text

def medication_start_end(user_data):
    file_number = user_data["file_number"]
    df = __load_medication_data(file_number)
    current_med_df = df[df['status'] == 'current']
    
    result_text = "You have the following medications:\n"
    for i, row in current_med_df.iterrows():
        print("row", row)
        result_text += f"{row['medication_name']} which started at {row['start_date']} and ends at {row['end_date']}\n"
    return result_text

def medication_refill_date(user_data):
    print("medication_refill_date called")
    file_number = user_data["file_number"]
    df = __load_medication_data(file_number)
    current_med_df = df[df['status'] == 'current']

    print("current_med_df: ", current_med_df)
    result_text = "Here is the medication refill list:\n"
    for i, row in current_med_df.iterrows():
        if pd.notna(row['refill_date']):
            result_text += f"{row['medication_name']}: {row['refill_date']}\n"
        else:
            result_text += f"{row['medication_name']}: there is no refill date provided\n"
    return result_text

