urlForm = "https://docs.google.com/forms/d/e/1FAIpQLSdd7at5g61dv5YXodoY8cQNzo0vkG-HDSTZvW3UW7NAdVoEjA/viewform?usp=sharing&ouid=101325639485412864700"
urlCSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQXEoqzReWW9VbEur-g53NwCR895XgKPFng-tJQ53H7krH6Fg1S692ISDewxzPzLco6t2EUFmYLvkAc/pub?output=csv"

import pandas as pd
df = pd.read_csv(urlCSV, usecols=range(1,20))

print(df)

df.set_index(df.columns[0], inplace=True)

print(df)




newrows = []

#From df we create the peopleSim score table
for index, row in df.iterrows():
    print(row)
    normrow = sum([x**2 for x in row] )**0.5
    newrow = [x/normrow for x in row]
    newrows.append(newrow)


Adf = pd.DataFrame(newrows)
ATdf = Adf.transpose()
peopleSim = Adf @ ATdf
peopleSim.index = df.index
peopleSim.columns = df.index

print(peopleSim)



#From df we create the musicSim score table
newrows = []
for index, row in df.transpose().iterrows():
    print(row)
    normrow = sum([x**2 for x in row] )**0.5
    newrow = [x/normrow for x in row]
    newrows.append(newrow)

Bdf = pd.DataFrame(newrows)
print(Bdf)
BTdf = Bdf.transpose()
musicSim = Bdf @ BTdf
musicSim.index = df.columns
musicSim.columns = df.columns

print(musicSim)



import seaborn as sns
ax = sns.heatmap(peopleSim, annot=True)
fig = ax.get_figure()
fig.show()
fig.savefig("musicpeople.png")



ax = sns.heatmap(musicSim, annot=True)
fig = ax.get_figure()
fig.show()
fig.savefig("music.png")

