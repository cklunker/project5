import matplotlib.pyplot as plt
asdf = open("something.csv")
def something(asdf):
    plt.xlabel("Date")
    plt.ylabel("Number of car seats installed")
    for i in asdf:
        i = i.strip()
        i = i.split()
        plt.hist(i)
        print(i)
print(something(asdf))
asdf.close
"""
test = 4,2,2,2,5,7,8,9,8,7,6,5,4,3,1
plt.hist(test)
plt.show()"""