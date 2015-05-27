from bottle import run, route,template
import redis, re
r=redis.Redis(host='localhost',port=6379,db=0)
stringList=[]
listList=[]
setList=[]
hashList=[]
sortedList=[]



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

	r.set('String:hz','tea')
	r.set('String:nb','fish')
	r.set('List:hz',['1','2','3'])
	r.set('Hash:hz',{'name':'yikang'})
	run(host='localhost', port=8080, debug=True)
 
