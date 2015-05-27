#!/usr/bin/python
#-*- coding: UTF-8 -*-
from bottle import route, run, template, request,static_file
from bottle import *
import redis

#@route('/static/<filename:re:.*\.css>')

r=redis.Redis(host='localhost',port=6379,db=0)
stringList=[]
listList=[]
setList=[]
hashList=[]
sortedList=[]

@route('/dash1')
def getSize():
        return 'Redis contains %d information.'%(r.dbsize())

 
@route("/dash")
def index():

        return template("Dashboard_Template_for_Bootstrap_files")

@route('/static/css/<filename>')
def stylesheets(filename):
    return static_file(filename,root='./static/css')

@route('/static/js/<filename>')
def javascript(filename): 
    return static_file(filename,root='./static/js')

@route('/static/images/<filename>')
def images(filename): 
    return static_file(filename,root='./static/images')

@route('/static/fonts/<filename>')
def fonts(filename):
    return static_file(filename,root='./static/fonts')



run(host='localhost', port=8080,debug=True)                    
