#!/usr/bin/python
#-*- coding: UTF-8 -*-
from bottle import route, run, template, request,static_file
from bottle import *
import redis, json,sys

################################################################################# db 0 最外层 ############################################################################################
r=redis.Redis(host='localhost',port=6379,db=0)
stringList=[]
listList=[]
setList=[]
hashList=[]
sortedList=[]

dictString={} # index中 string dict
dictList={} # index中 list dict
dictHash={} # index中 hash dict
dictSet={} # index中 set dict
dictSorted={} # index中 sorted dict

#返回Json格式
jsonString={}
jsonList={}
tmp=[]
for i in r.keys():
        if i.startswith("String"):
                jsonString['pre']='String'
                jsonString['key']=i
                jsonString['value']=r.get(i)
        elif i.startswith("List"):
                jsonList['pre']='List'
                jsonList['key']=i
                jsonList['value']=r.get(i)
@route('/jsonstring')
def fun():
        encodedjson = json.dumps(jsonString)
        str='[{"pre": "String", "value": "22", "key": "String:2"}]'
        return '[{"pre": "String", "value": "22", "key": "String:2"},{"pre": "String", "value": "22", "key": "String:2"}]'
@route('/jsonlist')
def fun1():
        return jsonList     

# db0 key分类，以及分类后的(key,value)
for elem in r.keys():
        if elem.startswith("String"):
                dictString[elem]=r.get(elem)
		stringList.append(elem)

        elif elem.startswith("List"):
                dictList[elem]=r.get(elem)
                listList.append(elem)

        elif elem.startswith("Hash"):
                dictHash[elem]=r.get(elem)
                hashList.append(elem)

        elif elem.startswith("Set"):
                dictSet[elem]=r.get(elem)
                setList.append(elem)

        elif elem.startswith("SortedSet"):
                dictSorted[elem]=r.get(elem)
                sortedList.append(elem)

@route('/info')
def getInfo():
        return r.info()

@route('/size')
def getSize():
        return '%d'%(r.dbsize())

@route('/string')
def getString():
	return '%d'%(len(stringList))

@route('/list')
def getList():
        return '%d'%(len(listList))

@route('/hash')
def getHash():
        return '%d'%(len(hashList))

@route('/set')
def getSet():
        return '%d'%(len(setList))

@route('/sorted')
def getSorted():
        return '%d'%(len(sortedList))




##############################    db1   ########################################

r1=redis.Redis(host='localhost',port=6379,db=1)
stringList1=[]
listList1=[]
setList1=[]
hashList1=[]
sortedList1=[]


for elem in r1.keys():
	if elem.startswith("String"):
		stringList1.append(elem)
        elif elem.startswith("List"):
                listList1.append(elem)
        elif elem.startswith("Hash"):
                hashList1.append(elem)
        elif elem.startswith("Set"):
                setList1.append(elem)
        elif elem.startswith("SortedSet"):
                sortedList1.append(elem)

@route('/info1')
def getInfo1():
        return r1.info()

@route('/size1')
def getSize1():
        return '%d'%(r1.dbsize())

@route('/string1')
def getString1():
	return '%d'%(len(stringList1))

@route('/list1')
def getList1():
        return '%d'%(len(listList1))

@route('/hash1')
def getHash1():
        return '%d'%(len(hashList1))

@route('/set1')
def getSet1():
        return '%d'%(len(setList1))

@route('/sorted1')
def getSorted1():
        return '%d'%(len(sortedList1))


############################       Implementation       ###################################

@route("/index")
def index():
	return template("index")
    
@route("/indexstringdetail")
def indexStringDetail():
	return template("indexstringdetail")
    
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

