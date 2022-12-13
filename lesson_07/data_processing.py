def get_data_from_console():
    fn = input("Enter first name: ")
    ln = input("Enter last name: ")
    ph = input("Enter phone number: ")
    co = input("Enter comment: ")
    return {"first_name": fn, "last_name": ln, "phone": ph, "comment": co}