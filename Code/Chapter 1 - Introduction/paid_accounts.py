from dump_data import salaries_and_tenures


def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


for salaries, tenures in salaries_and_tenures:
    print(str(tenures) + " " + str(predict_paid_or_unpaid(tenures)))
