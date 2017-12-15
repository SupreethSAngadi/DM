import pandas as pd
data = pd.read_csv('10_Property_stolen_and_recovered.csv')
data=data[['Area_Name', 'Year', 'Cases_Property_Recovered','Cases_Property_Stolen']]
cases_in_2001=pd.DataFrame(columns=['Area_Name','Year','Cases_Property_recovered','Cases_Property_stolen'])
cases_in_2002=pd.DataFrame(columns=['Area_Name','Year','Cases_Property_recovered','Cases_Property_stolen'])
cases_in_2003=pd.DataFrame(columns=['Area_Name','Year','Cases_Property_recovered','Cases_Property_stolen'])
cases_in_2004=pd.DataFrame(columns=['Area_Name','Year','Cases_Property_recovered','Cases_Property_stolen'])
cases_in_2005=pd.DataFrame(columns=['Area_Name','Year','Cases_Property_recovered','Cases_Property_stolen'])
cases_in_2006=pd.DataFrame(columns=['Area_Name','Year','Cases_Property_recovered','Cases_Property_stolen'])
cases_in_2007=pd.DataFrame(columns=['Area_Name','Year','Cases_Property_recovered','Cases_Property_stolen'])
cases_in_2008=pd.DataFrame(columns=['Area_Name','Year','Cases_Property_recovered','Cases_Property_stolen'])
cases_in_2009=pd.DataFrame(columns=['Area_Name','Year','Cases_Property_recovered','Cases_Property_stolen'])
cases_in_2010=pd.DataFrame(columns=['Area_Name','Year','Cases_Property_recovered','Cases_Property_stolen'])

for i in range(data.shape[0]):
    new_tuple=[data.get_values()[i][0],data.get_values()[i][1],data.get_values()[i][2],data.get_values()[i][3]]
    test_name,test_year,test_recovered,test_stolen=new_tuple[0],new_tuple[1],new_tuple[2],new_tuple[3]
    if test_year==2001:
        cases_in_2001.loc[len(cases_in_2001)]=[test_name,test_year,test_recovered,test_stolen]
    elif test_year==2002:
        cases_in_2002.loc[len(cases_in_2002)]=[test_name,test_year,test_recovered,test_stolen]
    elif test_year==2003:
        cases_in_2003.loc[len(cases_in_2003)]=[test_name,test_year,test_recovered,test_stolen]
    elif test_year==2004:
        cases_in_2004.loc[len(cases_in_2004)]=[test_name,test_year,test_recovered,test_stolen]
    elif test_year==2005:
        cases_in_2005.loc[len(cases_in_2005)]=[test_name,test_year,test_recovered,test_stolen]
    elif test_year==2006:
        cases_in_2006.loc[len(cases_in_2006)]=[test_name,test_year,test_recovered,test_stolen]
    elif test_year==2007:
        cases_in_2007.loc[len(cases_in_2007)]=[test_name,test_year,test_recovered,test_stolen]
    elif test_year==2008:
        cases_in_2008.loc[len(cases_in_2008)]=[test_name,test_year,test_recovered,test_stolen]
    elif test_year==2009:
        cases_in_2009.loc[len(cases_in_2009)]=[test_name,test_year,test_recovered,test_stolen]
    else:
        cases_in_2010.loc[len(cases_in_2010)]=[test_name,test_year,test_recovered,test_stolen]

list_of_crime_stolen_cases=[]
list_of_crime_recovered_cases=[]
stolen,recovered=0,0
for i in range(cases_in_2001.shape[0]):
    stolen+=cases_in_2001.get_values()[i][3]
    recovered+=cases_in_2001.get_values()[i][2]
total_crimes_in_2001=stolen
total_recovers_in_2001=recovered
list_of_crime_stolen_cases.append(['2001',total_crimes_in_2001])
list_of_crime_recovered_cases.append(['2001',total_recovers_in_2001])
stolen,recovered=0,0
for i in range(cases_in_2002.shape[0]):
    stolen+=cases_in_2002.get_values()[i][3]
    recovered+=cases_in_2002.get_values()[i][2]
total_crimes_in_2002=stolen
total_recovers_in_2002=recovered
list_of_crime_stolen_cases.append(['2002',total_crimes_in_2002])
list_of_crime_recovered_cases.append(['2002',total_recovers_in_2002])
stolen,recovered=0,0
for i in range(cases_in_2003.shape[0]):
    stolen+=cases_in_2003.get_values()[i][3]
    recovered+=cases_in_2003.get_values()[i][2]
total_crimes_in_2003=stolen
total_recovers_in_2003=recovered
list_of_crime_stolen_cases.append(['2003',total_crimes_in_2003])
list_of_crime_recovered_cases.append(['2003',total_recovers_in_2003])
stolen,recovered=0,0
for i in range(cases_in_2004.shape[0]):
    stolen+=cases_in_2004.get_values()[i][3]
    recovered+=cases_in_2004.get_values()[i][2]
total_crimes_in_2004=stolen
total_recovers_in_2004=recovered
list_of_crime_stolen_cases.append(['2004',total_crimes_in_2004])
list_of_crime_recovered_cases.append(['2004',total_recovers_in_2004])
stolen,recovered=0,0
for i in range(cases_in_2005.shape[0]):
    stolen+=cases_in_2005.get_values()[i][3]
    recovered+=cases_in_2005.get_values()[i][2]
total_crimes_in_2005=stolen
total_recovers_in_2005=recovered
list_of_crime_stolen_cases.append(['2005',total_crimes_in_2002])
list_of_crime_recovered_cases.append(['2005',total_recovers_in_2005])
stolen,recovered=0,0
for i in range(cases_in_2006.shape[0]):
    stolen+=cases_in_2006.get_values()[i][3]
    recovered+=cases_in_2006.get_values()[i][2]
total_crimes_in_2006=stolen
total_recovers_in_2006=recovered
list_of_crime_stolen_cases.append(['2006',total_crimes_in_2006])
list_of_crime_recovered_cases.append(['2006',total_recovers_in_2006])
stolen,recovered=0,0
for i in range(cases_in_2007.shape[0]):
    stolen+=cases_in_2007.get_values()[i][3]
    recovered+=cases_in_2007.get_values()[i][2]
total_crimes_in_2007=stolen
total_recovers_in_2007=recovered
list_of_crime_stolen_cases.append(['2007',total_crimes_in_2007])
list_of_crime_recovered_cases.append(['2007',total_recovers_in_2007])
stolen,recovered=0,0
for i in range(cases_in_2008.shape[0]):
    stolen+=cases_in_2008.get_values()[i][3]
    recovered+=cases_in_2008.get_values()[i][2]
total_crimes_in_2008=stolen
total_recovers_in_2008=recovered
list_of_crime_stolen_cases.append(['2008',total_crimes_in_2008])
list_of_crime_recovered_cases.append(['2008',total_recovers_in_2008])
stolen,recovered=0,0
for i in range(cases_in_2009.shape[0]):
    stolen+=cases_in_2009.get_values()[i][3]
    recovered+=cases_in_2009.get_values()[i][2]
total_crimes_in_2009=stolen
total_recovers_in_2009=recovered
list_of_crime_stolen_cases.append(['2009',total_crimes_in_2009])
list_of_crime_recovered_cases.append(['2009',total_recovers_in_2009])
stolen,recovered=0,0
for i in range(cases_in_2010.shape[0]):
    stolen+=cases_in_2010.get_values()[i][3]
    recovered+=cases_in_2010.get_values()[i][2]
total_crimes_in_2010=stolen
total_recovers_in_2010=recovered
list_of_crime_stolen_cases.append(['2010',total_crimes_in_2010])
list_of_crime_recovered_cases.append(['2010',total_recovers_in_2010])
print("List of crime cases is")
print(list_of_crime_stolen_cases)
print("List of crime recovered cases is")
print(list_of_crime_recovered_cases)
three_data=pd.DataFrame(columns=['Area_Name','Year','Cases_Property_Stolen'])
for i in range(data.shape[0]):
    t=[data.get_values()[i][0],data.get_values()[i][1],data.get_values()[i][3]]
    new_year=t[1]
    if new_year==2001 or new_year==2005 or new_year==2010:
        three_data.loc[len(three_data)]=[t[0],t[1],t[2]]
karnataka=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Karnataka':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
karnataka.append(['2001',sum_of_2001])
karnataka.append(['2005',sum_of_2005])
karnataka.append(['2010',sum_of_2010])
print('Total number of crimes in karnataka in 2001,2005,2010')
print(karnataka)

andhra=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Andhra Pradesh':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
andhra.append(['2001',sum_of_2001])
andhra.append(['2005',sum_of_2005])
andhra.append(['2010',sum_of_2010])
print('Total number of crimes in andra pradesh in 2001,2005,2010')
print(andhra)

ap=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Arunachal Pradesh':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
ap.append(['2001',sum_of_2001])
ap.append(['2005',sum_of_2005])
ap.append(['2010',sum_of_2010])
print('Total number of crimes in aruna chal pradesh in 2001,2005,2010')
print(ap)

bihar=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Bihar':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
bihar.append(['2001',sum_of_2001])
bihar.append(['2005',sum_of_2005])
bihar.append(['2010',sum_of_2010])
print('Total number of crimes in bihar in 2001,2005,2010')
print(bihar)

assam=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Assam':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
assam.append(['2001',sum_of_2001])
assam.append(['2005',sum_of_2005])
assam.append(['2010',sum_of_2010])
print('Total number of crimes in assam in 2001,2005,2010')
print(assam)

chandigarh=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Chandigarh':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
chandigarh.append(['2001',sum_of_2001])
chandigarh.append(['2005',sum_of_2005])
chandigarh.append(['2010',sum_of_2010])
print('Total number of crimes in chandigarh in 2001,2005,2010')
print(chandigarh)

chatisgarh=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Chhattisgarh':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
chatisgarh.append(['2001',sum_of_2001])
chatisgarh.append(['2005',sum_of_2005])
chatisgarh.append(['2010',sum_of_2010])
print('Total number of crimes in chatisgarh in 2001,2005,2010')
print(chatisgarh)

delhi=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Delhi':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
delhi.append(['2001',sum_of_2001])
delhi.append(['2005',sum_of_2005])
delhi.append(['2010',sum_of_2010])
print('Total number of crimes in delhi in 2001,2005,2010')
print(delhi)



goa=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Goa':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
goa.append(['2001',sum_of_2001])
goa.append(['2005',sum_of_2005])
goa.append(['2010',sum_of_2010])
print('Total number of crimes in goa in 2001,2005,2010')
print(goa)


gujrat=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Gujarat':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
gujrat.append(['2001',sum_of_2001])
gujrat.append(['2005',sum_of_2005])
gujrat.append(['2010',sum_of_2010])
print('Total number of crimes in gujrat in 2001,2005,2010')
print(gujrat)


haryana=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Haryana':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
haryana.append(['2001',sum_of_2001])
haryana.append(['2005',sum_of_2005])
haryana.append(['2010',sum_of_2010])
print('Total number of crimes in haryana in 2001,2005,2010')
print(haryana)


hp=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Himachal Pradesh':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
hp.append(['2001',sum_of_2001])
hp.append(['2005',sum_of_2005])
hp.append(['2010',sum_of_2010])
print('Total number of crimes in himachal pradesh in 2001,2005,2010')
print(hp)


jk=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Jammu & Kashmir':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
jk.append(['2001',sum_of_2001])
jk.append(['2005',sum_of_2005])
jk.append(['2010',sum_of_2010])
print('Total number of crimes in jammu & kashmir in 2001,2005,2010')
print(jk)


jarkhand=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Jharkhand':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
jarkhand.append(['2001',sum_of_2001])
jarkhand.append(['2005',sum_of_2005])
jarkhand.append(['2010',sum_of_2010])
print('Total number of crimes in jarkhand in 2001,2005,2010')
print(jarkhand)


kerala=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Kerala':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
kerala.append(['2001',sum_of_2001])
kerala.append(['2005',sum_of_2005])
kerala.append(['2010',sum_of_2010])
print('Total number of crimes in kerala in 2001,2005,2010')
print(kerala)


mp=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Madhya Pradesh':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
mp.append(['2001',sum_of_2001])
mp.append(['2005',sum_of_2005])
mp.append(['2010',sum_of_2010])
print('Total number of crimes in madhya pradesh in 2001,2005,2010')
print(mp)


up=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Uttar Pradesh':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
up.append(['2001',sum_of_2001])
up.append(['2005',sum_of_2005])
up.append(['2010',sum_of_2010])
print('Total number of crimes in uttar pradesh in 2001,2005,2010')
print(up)


panjab=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Punjab':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
panjab.append(['2001',sum_of_2001])
panjab.append(['2005',sum_of_2005])
panjab.append(['2010',sum_of_2010])
print('Total number of crimes in panjab in 2001,2005,2010')
print(panjab)


rajastan=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Rajasthan':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
rajastan.append(['2001',sum_of_2001])
rajastan.append(['2005',sum_of_2005])
rajastan.append(['2010',sum_of_2010])
print('Total number of crimes in rajastan in 2001,2005,2010')
print(rajastan)


sikkim=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Sikkim':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
sikkim.append(['2001',sum_of_2001])
sikkim.append(['2005',sum_of_2005])
sikkim.append(['2010',sum_of_2010])
print('Total number of crimes in sikkim in 2001,2005,2010')
print(sikkim)


tn=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Tamil Nadu':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
tn.append(['2001',sum_of_2001])
tn.append(['2005',sum_of_2005])
tn.append(['2010',sum_of_2010])
print('Total number of crimes in tamil nadu in 2001,2005,2010')
print(tn)


tripura=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Tripura':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
tripura.append(['2001',sum_of_2001])
tripura.append(['2005',sum_of_2005])
tripura.append(['2010',sum_of_2010])
print('Total number of crimes in tripura in 2001,2005,2010')
print(tripura)


wb=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='West Bengal':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
wb.append(['2001',sum_of_2001])
wb.append(['2005',sum_of_2005])
wb.append(['2010',sum_of_2010])
print('Total number of crimes in west bengal in 2001,2005,2010')
print(wb)


manipur=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Manipur':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
manipur.append(['2001',sum_of_2001])
manipur.append(['2005',sum_of_2005])
manipur.append(['2010',sum_of_2010])
print('Total number of crimes in manipur in 2001,2005,2010')
print(manipur)

meghalaya=[]
sum_of_2001=0
sum_of_2005=0
sum_of_2010=0
for i in range(three_data.shape[0]):
    test_tuple=[three_data.get_values()[i][0],three_data.get_values()[i][1],three_data.get_values()[i][2]]
    if test_tuple[0]=='Meghalaya':
        if test_tuple[1]==2001:
            sum_of_2001+=test_tuple[2]
        elif test_tuple[1]==2005:
            sum_of_2005+=test_tuple[2]
        elif test_tuple[1]==2010:
            sum_of_2010+=test_tuple[2]
meghalaya.append(['2001',sum_of_2001])
meghalaya.append(['2005',sum_of_2005])
meghalaya.append(['2010',sum_of_2010])
print('Total number of crimes in meghalaya in 2001,2005,2010')
print(meghalaya)

