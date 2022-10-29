from datetime import date


def user_details():
    """
    Prompt user input
    """
    first_name = input('Insert your first name\n')
    while True:
        if first_name.isalpha() or '-' in first_name or '~' in first_name:
            break
        else:
            print("Invalid first name")
            first_name = input("Insert your first name\n")

    last_name = input("Insert your last name\n")
    while True:
        if last_name.isalpha():

            break
        else:
            print("Invalid last name")
            last_name = input("Insert your last name\n")

    cohort = input("Insert your cohort\n")
    while True:
        if cohort >= str(date.today().year):
            if len(cohort) == 4:
                break
        else:
            print("Invalid cohort")
            cohort = input("Insert your cohort\n")

    campus = input("Insert the campus you will be attending in\n")
    while True:
        valid_campus = ['johannesburg', 'phokeng', 'capetown', 'cape town', 'durban']
        i = campus.lower()
        if campus.isalpha():
            if i in valid_campus:
                campus = i

                break
            else:
                print("Invalid campus")
                campus = input("Insert the campus you will be attending in\n")

    return first_name, last_name, cohort, campus


def create_user_name(first_name, last_name, cohort, campus):
    """
        Create and return a valid username
       """
    if len(first_name) == 2:
        first_name = first_name + "o"
    if len(first_name) == 1:
        first_name = first_name + "oo"

    if len(last_name) == 2:
        last_name = last_name + "o"
    if len(last_name) == 1:
        last_name = last_name + "oo"

    username = (first_name.lower()[-3:]) + (last_name.lower()[:3]) + campus + cohort

    return username


def user_campus(campus):
    final_campus = campus.lower()

    if final_campus == 'johannesburg':
        final_campus = 'JHB'

    elif final_campus == 'capetown' or final_campus == 'cape town':
        final_campus = 'CPT'

    elif final_campus == 'durban':
        final_campus = 'DBN'

    elif final_campus == 'phokeng':
        final_campus = 'PHO'

    return final_campus


if __name__ == '__main__':
    first_name, last_name, cohort, final_campus = user_details()
    campus = user_campus(final_campus)
    username = create_user_name(first_name, last_name, cohort, campus)

print(f"First name: {first_name}\n")
print(f"Last name: {last_name}\n")
print(f"Cohort year: {cohort}\n")
print(f"Final campus: {final_campus}\n")
print(f"Final username: {username}\n")
