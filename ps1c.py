

starting_salary = float(input("Enter the starting salary: "))
house_cost = 1000000
down_payment = house_cost * 0.25
annual_return = 0.04
semi_annual_raise = 0.07
months = 36

low = 0
high = 10000
steps = 0

current_savings = 0
annual_salary = starting_salary

for month in range(1, months + 1):
    current_savings += current_savings * (annual_return / 12)
    current_savings += (annual_salary / 12)
    if month % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    while True:
        steps += 1
        mid = (low + high) // 2


        current_savings = 0
        annual_salary = starting_salary

        for month in range(1, months + 1):
            current_savings += current_savings * (annual_return / 12)
            current_savings += (annual_salary / 12) * (mid / 10000)
            if month % 6 == 0:
                annual_salary += annual_salary * semi_annual_raise

        if abs(current_savings - down_payment) <= 100:
            print("Best savings rate:", round(mid / 10000, 4))
            print("Steps in bisection search:", steps)
            break
        elif current_savings < down_payment:
            low = mid
        else:
            high = mid
