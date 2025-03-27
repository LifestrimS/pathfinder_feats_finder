import numpy as np
import json
import re
from feat import Feat
from prereq import Prereq

def main():
    print('START')

    # with open('test_feat_table.json', encoding='utf8') as user_file:
    with open('feats.json', encoding='utf8') as user_file:
        content = user_file.read()

    parsed_json = json.loads(content)

    listFeats: list[Feat] = []

    for element in parsed_json:
        feat = Feat(element['Name'], 
                    getPrerequisite(element['Prerequisite']),
                    element['Description'])

        listFeats.append(feat)


    for el in listFeats:
      el.prerequisite = processPrereq(listFeats, el.prerequisite)

    print('============================================')

    for el in listFeats:
        print(el)
        print('PREREQUISITE:')
        if (el.prerequisite != []):
            # print('PREREQUISITE:')
            for pr in el.prerequisite:
                print(f'{pr}')
        else:
            print('-')
        print('\n')

    print('============================================')
    print('END\n\n')

    featId = input("Enter featId: ")
    

    while (featId != 'Exit') & (featId != 'exit'):
        displayInsideFeats(findFeatByIDd(featId = int(featId), featList = listFeats), featList = listFeats)
        featId = input("Enter featId: ")


def getPrerequisite(prer: str):
    prereqList: list[Prereq] = []

    if prer == '' or prer =='—':
        return []
    else:
        listPrereq = re.split('; |, ', prer)
        for el in listPrereq:
            el.strip('\r\n')
            prereqList.append(Prereq(False, el, None))
        return prereqList
    
def processPrereq(featList: list[Feat], prer: Prereq):
    featNameList: list[str] = []
    readyPrer: list[Prereq] = []

    for el in featList:
        featNameList.append(el.name)

    for el in prer:
        
        if el.name in featNameList:
            feat = [x for x in featList if x.name == el.name]
            
            print('\n')
            readyPrer.append(Prereq(isFeat = True, name = el.name, featId = feat[0].id))
        else:
            readyPrer.append(Prereq(False, el.name, None))

    
    return readyPrer

#Prerequisite list have feats id, should can find them
def findFeatByIDd(featId, featList: list)-> Feat:

    feat = [x for x in featList if x.id == featId]
    if feat != []:
        return feat[0]
    else:
        print ('\nFound nothing')

def displayInsideFeats(feat: Feat, featList: list, offset=''):
    offset = offset
    # print(f'\n{offset}{feat}\n')
    print('\n')
    printFeat(feat = feat, offset = offset)

    for el in feat.prerequisite:
        offset = offset + ' '
        if (el.isFeat):
            displayInsideFeats(feat = findFeatByIDd(el.featId, featList = featList), featList = featList, offset = offset)
        # else:
        #     print(f'{el}')

def printFeat(feat: Feat, offset: str):
    print(f"{offset}NAME: {feat.name}\n{offset}ID: {feat.id}\n{offset}DESCRIPTION: {feat.description}")
    print(f'{offset}PREREQUISITE:')
    if (feat.prerequisite != []):
        # print('PREREQUISITE:')
        for pr in feat.prerequisite:
            print(f'{offset}{pr}')
    else:
        print(f'{offset}-')


if __name__=="__main__":
    main()