
def div(a,b):
    c=-1
    try:
        print("open resources")
        c = a/b
        print("close resources")
    except ZeroDivisionError as e:
        print("cannot divide by 0 --> ",e)
    except TypeError as e:
        print("use only integer type ",e )
    except Exception:
        print("exception occured")

    return c

c = div(5,"0")
print(c)

