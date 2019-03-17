para = input("Enter string: ")

n = int(input("Enter int: "))

reverse_n = para[:-1*(n+1):-1]  #reverse string till nth index

print(reverse_n)
