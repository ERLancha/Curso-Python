email = input("Introduce email: ")

for i in email:
    if i == "@":
        arroba=True
        break;
else:
    arroba=False

print("Dirección correcta: " + str(arroba))