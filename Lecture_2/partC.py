initial_deposit=float(input("The initial amount in your savings account: "))
HOUSE_COST=800000
DOWN_PAYMENT=0.25
ACTUAL_COST=HOUSE_COST*DOWN_PAYMENT
MAX_BIAS=100
MONTHS=36
rmin=0.0
rmax=1.0
r=rmin
step=0

def amount_saved(rate):
    return initial_deposit*((1+rate/12)**MONTHS)

if amount_saved(rmax)<=ACTUAL_COST-MAX_BIAS:
    r=None

elif amount_saved(rmin)>=ACTUAL_COST-MAX_BIAS:
    r=0.0

else:
    while abs(amount_saved(r)-ACTUAL_COST)>=MAX_BIAS:
        if amount_saved(r)<=ACTUAL_COST-MAX_BIAS:
            rmin=r
            r=(rmax+r)/2
        elif amount_saved(r)>=ACTUAL_COST+MAX_BIAS:
            rmax=r
            r=(rmin+r)/2
        step+=1

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {step}")