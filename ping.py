import os


ipv4 = input("Insira o IP alvo: ")
print("-" * 60)
response_list = os.system("ping -n 4 {}".format(ipv4, verbose=True))
print("-" * 60)
