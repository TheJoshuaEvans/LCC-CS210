def diagnose_symptoms(has_fever: bool, has_cough: bool):
    """Perform diagnoses and suggest recommended treatment based on provided inputs

    Parameters
    ----------
    has_fever: bool
        If the patient has a fever (indicated by an oral temperature of 38°C or higher)

    has_cough: bool
        If the patient has a cough (indicated by persistent coughing over several weeks)
    """

    print("------------------------------")
    print(f"Patient Symptoms: Fever ({str(has_fever)}), Persistent Cough ({str(has_cough)})")

    diagnosis: str

    if has_fever and has_cough:
        diagnosis = "Flu - Recommend rest and hydration."
    elif has_fever and not has_cough:
        diagnosis = "Possible Infection - Recommend primary care physician visit."
    elif not has_fever and has_cough:
        diagnosis = "Cold/Allergies - Recommend over-the-counter medication."
    else:
        diagnosis = "General Check-up - Patient appears healthy."

    print(f"Diagnosis: {diagnosis}")

if __name__ == '__main__':
    # Example 1: True Fever, True Cough (Flu)
    diagnose_symptoms(True, True)
    # Example 2: False Fever, True Cough (Cold)
    diagnose_symptoms(False, True)

    diagnose_symptoms(True, False)
    diagnose_symptoms(False, False)
