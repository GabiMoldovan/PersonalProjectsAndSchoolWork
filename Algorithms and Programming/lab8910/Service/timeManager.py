def checkValidHour(oraData) -> bool:
    '''
    Functie care valideaza timpul
    :param oraData: ora
    :return: True daca ora este valida, altfel False
    '''
    hour = oraData[0] + oraData[1]
    if hour >= "24" or hour < "00":
        return False
    if oraData[2] != ":":
        return False
    mins = oraData[3] + oraData[4]
    if mins >= "60" or mins < "00":
        return False
    return True


def seAflaInIntervalCalendaristic(dataUnu, dataDoi, data) -> bool:
    '''
    Verifica daca data se afla in intervalul dintre datele dataUnu si dataDoi
    :param dataUnu: Data unu
    :param dataDoi: Data doi
    :param data: Data de verificat
    :return: True daca se afla, altfel False
    '''
    anDataUnu = dataUnu[6] + dataUnu[7] + dataUnu[8] + dataUnu[9]
    anDataUnu = int(anDataUnu)
    lunaDataUnu = dataUnu[3] + dataUnu[4]
    lunaDataUnu = int(lunaDataUnu)
    ziDataUnu = dataUnu[0] + dataUnu[1]
    ziDataUnu = int(ziDataUnu)

    anDataDoi = dataDoi[6] + dataDoi[7] + dataDoi[8] + dataDoi[9]
    anDataDoi = int(anDataDoi)
    lunaDataDoi = dataDoi[3] + dataDoi[4]
    lunaDataDoi = int(lunaDataDoi)
    ziDataDoi = dataDoi[0] + dataDoi[1]
    ziDataDoi = int(ziDataDoi)

    anData = data[6] + data[7] + data[8] + data[9]
    anData = int(anData)
    lunaData = data[3] + data[4]
    lunaData = int(lunaData)
    ziData = data[0] + data[1]
    ziData = int(ziData)

    if anData < anDataUnu or anData > anDataDoi:
        return False

    if anData == anDataUnu or anData == anDataDoi:
        if lunaData < lunaDataUnu or lunaData > lunaDataDoi:
            return False

    if anData == anDataUnu or anData == anDataDoi:
        if lunaData < lunaDataUnu or lunaData > lunaDataDoi:
            if ziData < ziDataUnu or ziData > ziDataDoi:
                return False

    return True
