from bottle import run, route,template
import redis, re
r=redis.Redis(host='localhost',port=6379,db=0)
stringList=[]
listList=[]
setList=[]
hashList=[]
sortedList=[]


r1=redis.Redis(host='localhost',port=6379,db=1)
stringList1=[]
listList1=[]
setList1=[]
hashList1=[]
sortedList1=[]




@route('/info')
def getSize():
	return 'Redis contains %d information.'%(r.dbsize())

@route('/keys')
def getKeys():
	str1='['
	for elem in r.keys():
		str1=str1+elem+' ,'
	str1=str1+']'		
	
	return'Redis contains keys:\n',str1

@route('/match')
def getMatch():

	for elem in r.keys():
		if elem.startswith("String"):
			stringList.append(elem)
		elif elem.startswith("List"):
			listList.append(elem)
		elif elem.startswith("Hash"):
                        hashList.append(elem)
                elif elem.startswith("Set"):
                        setList.append(elem)
		elif elem.startswith("SortedSet"):
			sortedList.append(elem);
	return "String:", str(len(stringList)), ", List:",str(len(listList)),", Hash:", str(len(hashList)), ", Set:",str(len(setList)),", SortedList:",str(len(sortedList))

@route('/match/string')
def getString():
	tmp=''
	for elem in stringList:
		tmp=tmp+elem+' '+(str (r.get(elem)))+', '
	return tmp

@route('/match/list')
def getList():
        tmp=''
        for elem in listList:
                tmp=tmp+elem+' '+(str (r.get(elem)))+', '
        return tmp

@route('/match/hash')
def getHash():
        tmp=''
        for elem in hashList:
                tmp=tmp+elem+' '+(str (r.get(elem)))+', '
        return tmp

@route('/keys/<key>')
def getKeyValue(key):
	return template('<b>key = {{key}}, value = {{value}}</b>',value =r.get(key),key=key)
	


if __name__=='__main__':
	r.flushdb()
	r1.flushdb()
	
	r.set('String:1','11')
	r.set('String:2','22')
	r.set('String:3','33')
	r.set('String:4','44')
	r.set('String:5','55')
	r.set('String:6','11')
	r.set('String:7','22')
	r.set('String:8','33')
	r.set('String:9','44')
	r.set('String:10','55')
	r.set('String:11','11')
	r.set('String:12','22')
	r.set('String:13','33')
	r.set('String:14','44')
	r.set('String:15','55')
	r.set('String:16','11')
	r.set('String:17','22')
	r.set('String:18','33')
	r.set('String:19','44')
	r.set('String:20','55')
	r.set('String:21','11')
	r.set('String:22','22')
	r.set('String:33','33')
	r.set('String:44','44')
	r.set('String:55','55')
	r.set('List:1',['11','22','33'])
	r.set('List:2',['111','222','333'])
	r.set('List:3',['1q','2q','3q'])
	r.set('List:4',['r1','r2','r3'])
	r.set('Hash:1',{'name':'yikang'})
	r.set('Hash:2',{'name':'yikang'})
	r.set('Hash:3',{'name':'yikang'})
	r.set('Set:1',{'name':'yikang'})
        r.set('Set:2',{'name':'yikang'})
       	r.set('SortedSet:1',{'name':'yikang'})


	r1.set('String:1','1')
	r1.set('String:2','2')
	r1.set('List:1',['1','2','3'])
	r1.set('List:2',['1','2','3'])
	r1.set('Hash:1',{'name':'yikang'})
	r1.set('Hash:2',{'name':'yikang'})
	r1.set('Set:1',{'name':'yikang'})
        r1.set('Set:2',{'name':'yikang'})
       	r1.set('SortedSet:1',{'name':'yikang'})



	run(host='localhost', port=8080, debug=True)
 
