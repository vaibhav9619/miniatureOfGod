
try:
    i=0/0
    f=open("abc.txt")
    for line in f:
        print(line)

# except:
#     print("why with me")
except Exception as e:
    print(e)

# except FileNotFoundError:
#     print("file not found")
# except ZeroDivisionError:
#     print("divided by 0 bro")
# except (FileNotFoundError,ZeroDivisionError):
#     print("File not Found adsdsxdas")


# We added it here just for fun
