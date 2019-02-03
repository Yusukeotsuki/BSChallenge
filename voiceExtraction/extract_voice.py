import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import time

filepath    = "data/test/"
outfilename = "data/output/******" + ".wav"
driver_path = "/Users/yusukeotsuki/Downloads/chromedriver"

driver= webdriver.Chrome(executable_path=driver_path)
driver.get("http://unetvocalsep.herokuapp.com/")
time.sleep(5)

def extract_voice(infile_path, outfile_path):
    
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
    tmp.send_keys(infile_path)
    # check the status
    status = driver.find_element_by_id("dropbox").text
    while status == "Processing, please wait...":
        time.sleep(3)
        status = driver.find_element_by_id("dropbox").text

    url = driver.find_element_by_id("audio-vocal").get_attribute("src")
    time.sleep(1)
    urllib.request.urlretrieve(url, outfile_path)
    status = driver.find_element_by_id("dropbox").text

for i in range(0,12):
    filepath = "/Users/yusukeotsuki/MyProject/BSchallenge/voiceExtraction/data/test/" + str(i) + ".wav"
    outfilename = "/Users/yusukeotsuki/MyProject/BSchallenge/voiceExtraction/data/test_output/" + str(i) + ".wav"
    extract_voice(filepath, outfilename)

