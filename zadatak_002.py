"""ime = input("Kako se zoveš? ")
print("Pozdrav", ime)"""
import sys

broj1= int(input("Unesi prvi broj: "))
broj2= int (input("Unesi drugi broj: "))
print("Njihov zbroj je: ", broj1, "+", broj2, "=", broj1+broj2 )
print("Njihova razlika je: ", broj1, "-", broj2, "=", broj1-broj2 )
print("Njihov umnožak je: ", broj1, "*", broj2, "=", broj1*broj2 )
print("Njihov količnik je: ", broj1, "/", broj2, "=", broj1/broj2 )
print("Njihova potencija je: ", broj1, "**", broj2, "=", broj1**broj2 )
print("Njihov modulo je: ", broj1, "modulo", broj2, "=", broj1%broj2 )


try:
    broj1 = int(input("Unesi prvi broj: "))
except: TypeError:
        exit(1)