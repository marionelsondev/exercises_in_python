num1 = int(input("\033[0;36mDigite o primeiro valor:\033[m\n"))
num2 = int(input("\033[0;36mDigite o segundo valor:\033[m\n"))

if num1 > num2:
    print("O \033[1mPRIMEIRO\033[m valor é maior.")
elif num2 > num1:
    print("O \033[1mSEGUNDO\033[m valor é maior.")
else:
    print("Os dois valores são \033[1mIGUAIS\033[m.")
