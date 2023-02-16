#note to professor: hi there! so i worked for 6 hours straight on the while loop because i could not get the formula to come out right. in an effort to keep my sanity i added my own flair of it being cat themed. please overlook it if you hate it alot (T-T) im so sorry
                                                        
def main():
  print(
      'This program will determine how long your interest rate will take to double :)'
    )
  ans = input("                                  START? (y/n): ")
  while ans == "y":
    print()
    print('                                      ^ ^')
    print('                                     =0.0=')
    print('                                       ^')
    print('                                   Hi there!')
    print('')
    
    print()
    print()
    interest_rate = float(
      input(
        'First, please input the annualized interest rate. ~Be sure to add your input as decimal~  '
      ))
    print()
    print('                                   Purrfect!')
    print()
    initial_investment = float(
      input(
        'Next, please enter your initial investment amount. ~Do not add any commas~   '
      ))
    print()
    print('                                    Pawsome!')
    earned_int_1 = (interest_rate * initial_investment)
    investment_total_1 = float((earned_int_1 + initial_investment))
    print()
    print(
      f"The investment amount for the first year is {investment_total_1:.2f}, cool lets see how long it would take for your original investment to double itself:"
    )
    print()
    nyears = 0
    target = initial_investment * 2
    while initial_investment * (1 + interest_rate)**nyears <= target:
      nyears += 1
    print(f"               You'll have to wait {nyears} years to see your payout")

    ans = input("                       Do another calculation? (y/n):  ")
   


main()
print('                               See mew next time!')


#todo:output number of years the investment will take to double
#todo: figure out where to put while loop and hwo to break it
