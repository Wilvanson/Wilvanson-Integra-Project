import gspread

gs = gspread.service_account(filename='credentials.json')

sh = gs.open_by_key('1O6AviSLAZx7KHmQ922DB-eUEZF-JlfwpLa5m9x3GLyE')

worksheet = sh.sheet1

records = worksheet.get_all_records()


#  Find the avage for each column 

crim = 0
lentCrim = len(records)
zn = 0
lentZn = len(records)
indus = 0
lentIndus = len(records)
chas = 0
lentChas = len(records)
nox = 0
lentNox = len(records)
rm = 0
lentRm = len(records)
age = 0
lentAge = len(records)
dis = 0
lentDis = len(records)
rad = 0
lentRad = len(records)
tax = 0
lentTax = len(records)
ptratio = 0
lentPtratio = len(records)
lstat = 0
lentLstat = len(records)
medv = 0
lentMedv = len(records)

for recs in records:
    crimR = recs['CRIM']
    znR = recs['ZN']
    indusR = recs['INDUS']
    chasR = recs['CHAS']
    noxR = recs['NOX']
    rmR = recs['RM']
    ageR = recs['AGE']
    disR = recs['DIS']
    radR = recs['RAD']
    taxR = recs['TAX']
    ptratioR = recs['PTRATIO']
    lstatR = recs['LSTAT']
    medvR = recs['MEDV']
    
    if crimR != 'NA':
        crim += crimR
    else:
        lentCrim -= 1

    if znR != 'NA':
        zn += znR
    else:
        lentZn -= 1

    if indusR != 'NA':
        indus += indusR
    else:
        lentIndus -= 1

    if chasR != 'NA':
        chas += chasR
    else:
        lentChas -= 1

    if noxR != 'NA':
        nox += noxR
    else:
        lentNox -= 1

    if rmR != 'NA':
        rm += rmR
    else:
        lentRm -= 1

    if ageR != 'NA':
        age += ageR
    else:
        lentAge -= 1

    if disR != 'NA':
        dis += disR
    else:
        lentDis -= 1

    if radR != 'NA':
        rad += radR
    else:
        lentRad -= 1

    if taxR != 'NA':
        tax += taxR
    else:
        lentTax -= 1

    if ptratioR != 'NA':
        ptratio += ptratioR 
    else:
        lentPtratio -= 1

    if lstatR != 'NA':
        lstat += lstatR
    else:
        lentLstat -= 1
    
    if medvR != 'NA':
        medv += medvR
    else:
        lentMedv -= 1

avg = {
    'CRIM': crim / lentCrim,
    'ZN': zn / lentZn,
    'INDUS': indus / lentIndus,
    'CHAS': chas / lentChas,
    'NOX': nox / lentNox,
    'RM': rm / lentRm,
    'AGE': age / lentAge,
    'DIS': dis / lentDis,
    'RAD': rad / lentRad,
    'TAX': tax / lentTax,
    'PTRATIO': ptratio / lentPtratio,
    'LSTAT': lstat / lentLstat,
    'MEDV': medv / lentMedv
}

print(avg)

# find the Min and Max for each column 

# starting Min values

crimMin = records[0]['CRIM']
znMin =  records[0]['ZN']
indusMin =  records[0]['INDUS']
chasMin =  records[0]['CHAS']
noxMin =  records[0]['NOX']
rmMin =  records[0]['RM']
ageMin =  records[0]['AGE']
disMin =  records[0]['DIS']
radMin =  records[0]['RAD']
taxMin =  records[0]['TAX']
ptratioMin =  records[0]['PTRATIO']
lstatMin =  records[0]['LSTAT']
medvMin =  records[0]['MEDV']

# starting Max values

crimMax = records[0]['CRIM']
znMax =  records[0]['ZN']
indusMax =  records[0]['INDUS']
chasMax =  records[0]['CHAS']
noxMax =  records[0]['NOX']
rmMax =  records[0]['RM']
ageMax =  records[0]['AGE']
disMax =  records[0]['DIS']
radMax =  records[0]['RAD']
taxMax =  records[0]['TAX']
ptratioMax =  records[0]['PTRATIO']
lstatMax =  records[0]['LSTAT']
medvMax =  records[0]['MEDV']


for recs in records:

    crimR = recs['CRIM']
    znR = recs['ZN']
    indusR = recs['INDUS']
    chasR = recs['CHAS']
    noxR = recs['NOX']
    rmR = recs['RM']
    ageR = recs['AGE']
    disR = recs['DIS']
    radR = recs['RAD']
    taxR = recs['TAX']
    ptratioR = recs['PTRATIO']
    lstatR = recs['LSTAT']
    medvR = recs['MEDV']

    if crimR > crimMax:
        crimMax = crimR
    elif crimR < crimMin:
        crimMin = crimR
    
    if znR > znMax:
        znMax = znR
    elif znR < znMin:
        znMin = znR
    
    if indusR > indusMax:
        indusMax = indusR
    elif indusR < indusMin:
        indusMin = indusR
    
    if chasR > chasMax:
        chasMax = chasR
    elif chasR < chasMin:
        chasMin = chasR
    
    if noxR > noxMax:
        noxMax = noxR
    elif noxR < noxMin:
        noxMin = noxR
    
    if rmR > rmMax:
        rmMax = rmR
    elif rmR < rmMin:
        rmMin = rmR
    
    if ageR > ageMax:
        ageMax = ageR
    elif ageR < ageMin:
        ageMin = ageR
    
    if disR > disMax:
        disMax = disR
    elif disR < disMin:
        disMin = disR
    
    if radR > radMax:
        radMax = radR
    elif radR < radMin:
        radMin = radR
    
    if taxR > taxMax:
        taxMax = taxR
    elif taxR < taxMin:
        taxMin = taxR
    
    if ptratioR > ptratioMax:
        ptratioMax = ptratioR
    elif ptratioR < ptratioMin:
        ptratioMin = ptratioR
    
    if lstatR > lstatMax:
        lstatMax = lstatR
    elif lstatR < lstatMin:
        lstatMin = lstatR
    
    if medvR > medvMax:
        medvMax = medvR
    elif medvR < medvMin:
        medvMin = medvR


min = {
    'CRIM': crimMin,
    'ZN': znMin,
    'INDUS': indusMin,
    'CHAS': chasMin,
    'NOX': noxMin,
    'RM': rmMin,
    'AGE': ageMin,
    'DIS': disMin,
    'RAD': radMin,
    'TAX': taxMin,
    'PTRATIO': ptratioMin,
    'LSTAT': lstatMin,
    'MEDV': medvMin
}

max = {
    'CRIM': crimMax,
    'ZN': znMax,
    'INDUS': indusMax,
    'CHAS': chasMax,
    'NOX': noxMax,
    'RM': rmMax,
    'AGE': ageMax,
    'DIS': disMax,
    'RAD': radMax,
    'TAX': taxMax,
    'PTRATIO': ptratioMax,
    'LSTAT': lstatMax,
    'MEDV': medvMax
}

print('\n')
print(min)
print('\n')
print(max)
