import sklearn

print(f"SKLearn version: {sklearn.__version__} \n")

if sklearn.__version__ == "0.21.3":
    print(f"We're executing this code because sklearn version is < 0.22.")
else:
    print(f"We're NOT executing this code because sklearn version is < 0.22.")

if sklearn.__version__ == "0.23.1":
    print(f"We're executing this code because sklearn version is >= 0.22.")
else:
    print(f"We're NOT executing this code because sklearn version is >= 0.22.")