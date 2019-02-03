import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import time

filepath="data/test/1.wav"
outfilename = "out.wav"


driver= webdriver.Chrome(executable_path="/Users/yusukeotsuki/Downloads/chromedriver")
actions = ActionChains(driver)
driver.get("http://unetvocalsep.herokuapp.com/")
time.sleep(5)


JS_DROP_FILE = "var tgt=arguments[0],e=document.createElement('input');e.type='"+\
"file';e.addEventListener('change',function(event){var dataTrans" +\
"fer={dropEffect:'',effectAllowed:'all',files:e.files,items:{},t" +\
"ypes:[],setData:function(format,data){},getData:function(format" +\
"){}};var emit=function(event,target){var evt=document.createEve" +\
"nt('Event');evt.initEvent(event,true,false);evt.dataTransfer=da"+\
"taTransfer;target.dispatchEvent(evt);};emit('dragenter',tgt);em"+\
"it('dragover',tgt);emit('drop',tgt);document.body.removeChild(e"+\
");},false);document.body.appendChild(e);return e;"

drop_area = driver.find_element_by_id("dropbox")

tmp = driver.execute_script(JS_DROP_FILE, drop_area)
tmp.send_keys(filepath)

url = driver.find_element_by_id("audio-vocal").get_attribute("src")
urllib.request.urlretrieve(url, outfilename)
