yearly_salary=float(input("Your yearly salary"))
portion_saved=float(input("The portion of your salary to be saved, in decimal form"))
cost_of_dream_home=float(input("The cost of your dream home"))
portion_down_payment=0.25
amount_saved=0
r=0.05
months=0
while amount_saved<(cost_of_dream_home*portion_down_payment):
    months+=1
    amount_saved+=amount_saved*(r/12)
    amount_saved+=(yearly_salary/12)*portion_saved
print(f"Number of months: {months}")
