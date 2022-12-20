def get_data_from_console():
    fn = input("Enter first name: ")
    ln = input("Enter last name: ")
    ph = input("Enter phone number: ")
    co = input("Enter comment: ")
    bd = input("Date of birth: ")
    wg_min = input('Minimum salary: ')
    wg_max = input("Maximum salary: ")
    ep = input("Employee's position: ")
    return {"first_name": fn, "last_name": ln, "phone": ph, "comment": co, 'b_date': bd,
            'wg_min': wg_min, 'wg_max': wg_max, 'ep': ep}
