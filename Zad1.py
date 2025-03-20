import pandas as pd

# Učitavanje skupa podataka
mtcars = pd.read_csv('mtcars.csv')

# 1. Kojih 5 automobila ima najveću potrošnju?
top_5_mpg = mtcars.sort_values(by='mpg', ascending=False).head(5)
print("5 automobila s najvećom potrošnjom:")
print(top_5_mpg[['mpg', 'model']])  # pretpostavljamo da postoji kolona 'model' za ime automobila

# 2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
top_3_8cyl_mpg = mtcars[mtcars['cyl'] == 8].sort_values(by='mpg', ascending=True).head(3)
print("\n3 automobila sa 8 cilindara koja imaju najmanju potrošnju:")
print(top_3_8cyl_mpg[['mpg', 'model']])

# 3. Kolika je srednja potrošnja automobila sa 6 cilindara?
avg_mpg_6cyl = mtcars[mtcars['cyl'] == 6]['mpg'].mean()
print("\nSrednja potrošnja automobila sa 6 cilindara:", avg_mpg_6cyl)

# 4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
avg_mpg_4cyl_2000_2200 = mtcars[(mtcars['cyl'] == 4) & (mtcars['wt'] * 1000 >= 2000) & (mtcars['wt'] * 1000 <= 2200)]['mpg'].mean()
print("\nSrednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs:", avg_mpg_4cyl_2000_2200)

# 5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
transmission_counts = mtcars['am'].value_counts()
print("\nBroj automobila s različitim vrstama mjenjača:")
print("Ručni mjenjač (am = 1):", transmission_counts.get(1, 0))
print("Automatski mjenjač (am = 0):", transmission_counts.get(0, 0))

# 6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
auto_over_100hp = mtcars[(mtcars['am'] == 0) & (mtcars['hp'] > 100)]
print("\nBroj automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga:", len(auto_over_100hp))

# 7. Kolika je masa svakog automobila u kilogramima?
mtcars['wt_kg'] = mtcars['wt'] * 1000 * 0.453592  # konverzija iz lbs u kg (1 lb = 0.453592 kg)
print("\nMasa svakog automobila u kilogramima:")
print(mtcars[['model', 'wt_kg']])
