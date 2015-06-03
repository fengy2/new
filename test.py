#!/usr/bin/python
#-*- coding: UTF-8 -*-
from bottle import route, run, template, request,static_file
from bottle import *
import redis, json,sys

################################################################################# db 0 最外层 ############################################################################################
r=redis.Redis(host='localhost',port=6379,db=0)
#返回Json格式

listS=[]
listL=[]
listH=[]
listSet=[]
listSorted=[]

for elem in r.keys():
        if elem.startswith("String"):
                dictString={}
                dictString['pre']='String'
                dictString['key']=elem
                dictString['value']=r.get(elem)
                listS.append(dictString)

        elif elem.startswith("List"):
		dictList={}
                dictList['pre']='List'
                dictList['key']=elem
                dictList['value']=r.get(elem)
                listL.append(dictList)

        elif elem.startswith("Hash"):
		dictHash={}
                dictHash['pre']='Hash'
                dictHash['key']=elem
                dictHash['value']=r.get(elem)
                listH.append(dictHash)

        elif elem.startswith("Set"):
		dictSet={}
                dictSet['pre']='Set'
                dictSet['key']=elem
                dictSet['value']=r.get(elem)
                listSet.append(dictSet)

        elif elem.startswith("Sorted"):
		dictSorted={}
                dictSorted['pre']='Sorted'
                dictSorted['key']=elem
                dictSorted['value']=r.get(elem)
                listSorted.append(dictSorted)
            
@route('/jsonstring')
def stringQuant():
        tmp=json.dumps(listS)
        return str(tmp)
@route('/jsonlist')
def listQuant():
        tmp=json.dumps(listL)
        return str(tmp)    
@route('/jsonhash')
def hashQuant():
        tmp=json.dumps(listH)
        return str(tmp)
@route('/jsonset')
def setQuant():
        tmp=json.dumps(listSet)
        return str(tmp)
@route('/jsonsorted')
def sortedQuant():
        tmp=json.dumps(listSorted)
        return str(tmp)






@route('/info')
def getInfo():
	tmpList=[]
	tmpList.append(r.info())
	tmp=json.dumps(tmpList)
        return str(tmp)

@route('/size')
def getSize():
        return '%d'%(r.dbsize())

@route('/string')
def getString():
	return '%d'%(len(listS))

@route('/list')
def getList():
        return '%d'%(len(listL))

@route('/hash')
def getHash():
        return '%d'%(len(listH))

@route('/set')
def getSet():
        return '%d'%(len(listSet))

@route('/sorted')
def getSorted():
        return '%d'%(len(listSorted))





############################       Implementation       ###################################

@route("/index")
def index():
	return template("index")
    
@route("/indexstringdetail")
def indexStringDetail():
	return template("indexstringdetail")

@route("/indexlistdetail")
def indexListDetail():
	return template("indexlistdetail")

@route("/indexhashdetail")
def indexHashDetail():
	return template("indexhashdetail")
@route("/indexsetdetail")
def indexSetDetail():
	return template("indexsetdetail")
@route("/indexsorteddetail")
def indexSortedDetail():
	return template("indexsorteddetail")
    


#返回DB0中以各个Prefix开头key的数量
@route("/index/stringkeys")
def indexStringKeys():	
	return stringList

@route("/index/listkeys")
def indexListKeys():	
	return listList

@route("/index/hashkeys")
def indexHashKeys():	
	return hashList

@route("/index/setkeys")
def indexSetKeys():	
	return setList

@route("/index/sortedkeys")
def indexSortedKeys():	
	return sortedList

#返回DB0中以string开头的key 和 对应的value

@route("/index/stringvalues")
def indexStringValues():
	tmp=dictString.items()	
	return str (tmp)

@route("/index/listvalues")
def indexListValues():
	tmp=dictList.items()	
	return str (tmp)

@route("/index/hashvalues")
def indexHashValues():
	tmp=dictHash.items()	
	return str (tmp)

@route("/index/setvalues")
def indexSetValues():
	tmp=dictSet.items()	
	return str (tmp)

@route("/index/sortedvalues")
def indexSortedValues():
	tmp=dictSorted.items()	
	return str (tmp)



@route("/index1")
def index1():
	return template("index1")

@route("/stats.html")
def stats():
	return template("stats")

#bootstrap/css
@route('/Bootstrap-Admin-Theme/bootstrap/css/<filename>')
def stylesheetsbootstrapcss(filename):
	return static_file(filename,root='./Bootstrap-Admin-Theme/bootstrap/css')

#bootstrap/js
@route('/Bootstrap-Admin-Theme/bootstrap/js/<filename>')
def javascriptbootstrapjs(filename):
    	return static_file(filename,root='./Bootstrap-Admin-Theme/bootstrap/js')

#vendors/easypiechart/
@route('/Bootstrap-Admin-Theme/vendors/easypiechart/<filename>')
def stylesheetsvendorseasypiechart(filename):
	return static_file(filename,root='./Bootstrap-Admin-Theme/vendors/easypiechart')

#vendors/fullcalendar
@route('/Bootstrap-Admin-Theme/vendors/fullcalendar/<filename>')
def stylesheetsvendorsfullcalendar(filename):
	return static_file(filename,root='./Bootstrap-Admin-Theme/vendors/fullcalendar')

#vendors/morris/
@route('/Bootstrap-Admin-Theme/vendors/morris/<filename>')
def stylesheetsvendorsmorris(filename):
	return static_file(filename,root='./Bootstrap-Admin-Theme/vendors/morris')

#vendors/morris/flot
@route('/Bootstrap-Admin-Theme/vendors/flot/<filename>')
def stylesheetsvendorsmorris(filename):
	return static_file(filename,root='./Bootstrap-Admin-Theme/vendors/flot')

#vendors/datatables/js/
@route('/Bootstrap-Admin-Theme/vendors/datatables/js/<filename>')
def stylesheetsvendorsdatatables(filename):
	return static_file(filename,root='./Bootstrap-Admin-Theme/vendors/datatables/js')

#assets
@route('/Bootstrap-Admin-Theme/assets/<filename>')
def stylesheetsassets(filename):
	return static_file(filename,root='./Bootstrap-Admin-Theme/assets')

#vendors
@route('/Bootstrap-Admin-Theme/vendors/<filename>')
def javascriptvonders(filename): 
	return static_file(filename,root='./Bootstrap-Admin-Theme/vendors')




run(host='localhost', port=8080,debug=True)  

