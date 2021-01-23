
def parseFundamentalValue(json, index, section, dataC):

    jSection = json[index]['statementData'][section]
    for i in jSection:

        if i['dataCode'] == dataC:
            dataValue = i['value']
            return dataValue
