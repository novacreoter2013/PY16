try:
    num1 , num2 = eval(input("PLEASE ENTER TWO NUMBERS SEPARATED BY COMMA:"))
    result = num1 / num2
    print("RESULT IS: ", result)

except ZeroDivisionError :
    print("DIVISION BY ZERO IS ERROR!!!!")

except SyntaxError:
    print("COMMA IS MISSING . ENTER NUMBERS SEPARATED BY COMMA LIKE 1,2,3")

except :
    print("WRONG INPUT!!!!")

else:
    print("NO EXCEPTION OCCURRED!!!!")

finally:
    print("THIS WILL EXECUTE NO MATTAR WHAT HAPPENS!!!!")