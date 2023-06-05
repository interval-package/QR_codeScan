import bottle

import cv2
import pandas as pd
import numpy as np


def scan_bar_func(tar_url):
    img=cv2.imread(tar_url)
    shp=img.shape

    zolist=[]
    #print(img)
    for pixel in img[int(shp[0]/2)]:
        print(pixel)
        if pixel[0]>=150 and pixel[1]>=150 and pixel[2]>=150:
            zolist.append(0)
        else:
            zolist.append(1)


    print(zolist)

    zoflag=True
    tmp=0
    lenth=0
    start=0
    for zo,i in zip(zolist,range(len(zolist))):
        if not zoflag and zo==0:
            lenth=tmp
            break
        if zo==1 and zoflag:
            start=i
        if zo==1:
            tmp=tmp+1
            zoflag=False

    i=start
    continueflag=True
    truelist=[]
    while i<len(zolist) and continueflag: #防抖动
        #print("i",i)
        if zolist[i]==1:
            tmp =1
            while zolist[i+1]!=0:
                tmp=tmp+1
                i=i+1
            print("1",tmp)
            if int(tmp/lenth)==0:
                truelist.append(1)
            else:
                for j in range(int(tmp/lenth)):
                    truelist.append(1)

        elif zolist[i]==0:
            tmp =1
            while zolist[i+1]!=1:
                tmp=tmp+1
                i=i+1
                if i==(len(zolist)-1):
                    continueflag=False
                    break
                if tmp>lenth*9:
                    continueflag=False
                    break
            print("0",tmp)
            if continueflag:
                if int(tmp/lenth)==0:
                    truelist.append(0)
                else:
                    for j in range(int(tmp/lenth)):
                        truelist.append(0)
        i=i+1

    print(lenth)
    print(truelist)
    print(len(truelist))

    start_flag_area=truelist[0:3]
    dataleft=truelist[3:3+42]
    middle_flag_area=truelist[3+42:3+42+5]
    dataright=truelist[3+42+5:3+42+5+42]
    end_flag_area=truelist[3+42+5+42:95]

    print(start_flag_area)
    print(dataleft)
    print(middle_flag_area)
    print(dataright)
    print(end_flag_area)

    dataleft_str=[]
    for i in range(0,len(dataleft),7):
        tmpstr=""
        for j in range(7):
            tmpstr+=str(dataleft[i+j])
        print(tmpstr)
        dataleft_str.append(tmpstr)

    print(dataleft_str)

    dataleft_str=[]
    for i in range(0,len(dataleft),7):
        tmpstr=""
        for j in range(7):
            tmpstr+=str(dataleft[i+j])
        print(tmpstr)
        dataleft_str.append(tmpstr)

    print(dataleft_str)

    dataright_str=[]
    for i in range(0,len(dataright),7):
        tmpstr=""
        for j in range(7):
            tmpstr+=str(dataright[i+j])
        print(tmpstr)
        dataright_str.append(tmpstr)

    print(dataright_str)
    eancode=pd.read_csv("./eancode.csv")
    #print(eancode)
    eancode_list=np.array(eancode).tolist()
    print(eancode_list)
    eanabc=pd.read_csv("./eanabc.csv")
    #print(eanabc)
    eanabc_list=np.array(eanabc).tolist()
    print(eanabc_list)

    print(eancode['0'][0])
    print(len(eancode_list))
    print(len(eancode_list[0]))
    ABtype=""
    left_data=""
    for data in dataleft_str:
        dataint=int(data)
        #print(dataint)
        for i in range(len(eancode_list)):
            for j in range(len(eancode_list[0])):
                if dataint==eancode_list[i][j]:
                    print(i,j)
                    left_data+=str(j-1)
                    if i==0:
                        ABtype+="A"
                    elif i==1:
                        ABtype+="B"

    print(left_data)

    right_data=""
    for data in dataright_str:
        dataint=int(data)
        #print(dataint)
        for i in range(len(eancode_list)):
            for j in range(len(eancode_list[0])):
                if dataint==eancode_list[i][j]:
                    print(i,j)
                    right_data+=str(j-1)

    print(right_data)

    start_data=""
    for i in range(len(eanabc_list)):
        if ABtype==eanabc_list[i][1]:
            #print(eanabc_list[i][0])
            start_data=str(eanabc_list[i][0])

    print(ABtype)
    print(start_data)
    result=start_data+left_data+right_data
    print("扫码结果为:"+result)

    jihe=0
    ouhe=0
    jiaoyan=0
    for text,i in zip(result,range(len(result))):
        if i==12:
            #print(ouhe)
            #print(jihe)
            jiaoyan=10-(ouhe*3+jihe)%10
            #print(jiaoyan)
            if jiaoyan==int(text):
                print("校验码正确")
        if(i%2==0):
            jihe+=int(text)
        else:
            ouhe+=int(text)

    return result


def server_main():
    import json
    from json import JSONEncoder
    from bottle import run, post, request, response

    @post('/dillusion')
    def dillusion_action():
        req_obj = json.loads(request.body.read())
        url = req_obj["tar_url"]
        print(url)
        res = {"url":"url"}
        res = json.dumps(res)
        print(res)
        return res

    run(host='localhost', port=5555, debug=True)

# server_main()