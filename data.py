import gspread

gs = gspread.service_account(filename='credentials.json')

sh = gs.open_by_key('1O6AviSLAZx7KHmQ922DB-eUEZF-JlfwpLa5m9x3GLyE')

worksheet = sh.sheet1

records = worksheet.get_all_records()

def dataBase():
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

        if  crimR != 'NA' and crimR > crimMax:
            crimMax = crimR
        elif crimR != 'NA' and crimR < crimMin:
            crimMin = crimR
        
        if znR != 'NA' and znR > znMax:
            znMax = znR
        elif znR != 'NA' and znR < znMin:
            znMin = znR
        
        if indusR != 'NA' and indusR > indusMax:
            indusMax = indusR
        elif indusR != 'NA' and indusR < indusMin:
            indusMin = indusR
        
        if chasR != 'NA' and chasR > chasMax:
            chasMax = chasR
        elif chasR != 'NA' and chasR < chasMin:
            chasMin = chasR
        
        if noxR != 'NA' and noxR > noxMax:
            noxMax = noxR
        elif noxR != 'NA' and noxR < noxMin:
            noxMin = noxR
        
        if rmR != 'NA' and rmR > rmMax:
            rmMax = rmR
        elif rmR != 'NA' and rmR < rmMin:
            rmMin = rmR
        
        if ageR != 'NA' and ageR > ageMax:
            ageMax = ageR
        elif ageR != 'NA' and ageR < ageMin:
            ageMin = ageR
        
        if disR != 'NA' and disR > disMax:
            disMax = disR
        elif disR != 'NA' and disR < disMin:
            disMin = disR
        
        if radR != 'NA' and radR > radMax:
            radMax = radR
        elif radR != 'NA' and radR < radMin:
            radMin = radR
        
        if taxR != 'NA' and taxR > taxMax:
            taxMax = taxR
        elif taxR != 'NA' and taxR < taxMin:
            taxMin = taxR
        
        if ptratioR != 'NA' and ptratioR > ptratioMax:
            ptratioMax = ptratioR
        elif ptratioR != 'NA' and ptratioR < ptratioMin:
            ptratioMin = ptratioR
        
        if lstatR != 'NA' and lstatR > lstatMax:
            lstatMax = lstatR
        elif lstatR != 'NA' and lstatR < lstatMin:
            lstatMin = lstatR
        
        if medvR != 'NA' and medvR > medvMax:
            medvMax = medvR
        elif medvR != 'NA' and medvR < medvMin:
            medvMin = medvR
    
    crimArr = []
    znArr =  []
    indusArr =  []
    chasArr =  []
    noxArr = [] 
    rmArr =  []
    ageArr =  []
    disArr = [] 
    radArr =  []
    taxArr =  []
    ptratioArr = [] 
    lstatArr =  []
    medvArr = []

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
            crimArr.append(crimR)

        if znR != 'NA':
            znArr.append(znR)
        
        if indusR != 'NA':
            indusArr.append(indusR)
        
        if chasR != 'NA':
            chasArr.append(chasR)
        
        if noxR != 'NA':
            noxArr.append(noxR)
        

        if rmR != 'NA':
            rmArr.append(rmR)
        
        if ageR != 'NA':
            ageArr.append(ageR)

        if disR != 'NA':
            disArr.append(disR)
        
        if radR != 'NA':
            radArr.append(radR)
        
        if taxR != 'NA':
            taxArr.append(taxR)
        
        if ptratioR != 'NA':
            ptratioArr.append(ptratioR )
        
        if lstatR != 'NA':
            lstatArr.append(lstatR)
         
        if medvR != 'NA':
            medvArr.append(medvR)
        
    medvCrim = []
    medvPtratio = []
    medvAge = []
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

        if crimR != 'NA' and medvR != 'NA':
            medvCrim.append((medvR, crimR))
        
        if ptratioR != 'NA' and medvR != 'NA':
            medvPtratio.append((medvR, ptratioR))

        if ageR != 'NA' and medvR != 'NA':
            medvAge.append((medvR, ageR))

        


    data = {
        'CRIM':{
            'AVG': crim / lentCrim,
            'MAX': crimMax,
            'MIN': crimMin,
            'RECORDS': crimArr
            },
        'ZN':{
            'AVG': zn / lentZn,
            'MAX': znMax,
            'MIN': znMin,
            'RECORDS': znArr
            },
        'INDUS':{
            'AVG': indus / lentIndus,
            'MAX': indusMax,
            'MIN': indusMin,
            'RECORDS': indusArr
            },
        'CHAS':{
            'AVG': chas / lentChas,
            'MAX': chasMax,
            'MIN': chasMin,
            'RECORDS': chasArr
            },
        'NOX':{
            'AVG': nox / lentNox,
            'MAX': noxMax,
            'MIN': noxMin,
            'RECORDS': noxArr
            },
        'RM':{
            'AVG': rm / lentRm,
            'MAX': rmMax,
            'MIN': rmMin,
            'RECORDS': rmArr
            },
        'AGE':{
            'AVG': age / lentAge,
            'MAX': ageMax,
            'MIN': ageMin,
            'RECORDS': ageArr
            },
        'DIS':{
            'AVG': dis / lentDis,
            'MAX': disMax,
            'MIN': disMin,
            'RECORDS': disArr
            },
        'RAD':{
            'AVG': rad / lentRad,
            'MAX': radMax,
            'MIN': radMin,
            'RECORDS': radArr
            },
        'TAX':{
            'AVG': tax / lentTax,
            'MAX': taxMax,
            'MIN': taxMin,
            'RECORDS': taxArr
            },
        'PTRATIO':{
            'AVG': ptratio / lentPtratio,
            'MAX': ptratioMax,
            'MIN': ptratioMin,
            'RECORDS': ptratioArr
            },
        'LSTAT':{
            'AVG': lstat / lentLstat,
            'MAX': lstatMax,
            'MIN': lstatMin,
            'RECORDS': lstatArr
            },
        'MEDV':{
            'AVG': medv / lentMedv,
            'MAX': medvMax,
            'MIN': medvMin,
            'RECORDS': medvArr
            },
        'ZYMEDVCRIM': medvCrim,
        'ZYMEDVPTRATIO': medvPtratio,
        'ZYMEDVAGE': medvAge
    }

    return data

# b = dataBase()

# print(b)