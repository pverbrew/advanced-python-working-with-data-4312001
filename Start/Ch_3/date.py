import datetime


print("\nget current date and time")
t = datetime.datetime.now()
print("datetime.datetime.now() =", t, "\n")


t = t.date()
print("get date only")
print("t.date =", t,"\n")

print("restore current date/time")
t = datetime.datetime.now()
print("t =", t, "\n")

print("get an integer number of ms for current date/time")
ms = int(t.timestamp() * 1000)
print("ms = int(t.timestamp() * 1000) =", ms, "\n")

print("convert ms back to date/time")
t = datetime.datetime.fromtimestamp(ms/1000)
print("t = datetime.datetime.fromtimestamp(ms/1000) =",t, "\n")
t1 = datetime.date.fromtimestamp(ms/1000)
print("t1 = datetime.datetime.fromtimestamp(ms/1000) =",t1, "\n")


t = t.date()
print("get date having started with ms")
print("t.date() =", t, "\n")
