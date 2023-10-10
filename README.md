# automation testing


***
## structure

automation-testing/  
|-- api  
|-- common  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- request.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- database.py  
|-- config  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- environment.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- environment.yaml  
|-- operation  
|-- testcases  
|-- testdata  
|-- requirements.txt  
|-- .gitignore  
|-- pytest.ini  
|-- README.md  

***
## structure summary

api -> only for api call  
common -> some common package or tool, like request, database  
config -> environment, like sit, uat or production  
operation -> processing data and get ready to call api  
testcases -> execute test    
testdata -> put testdata for testcases  
pytest.ini -> pytest setting

***

## run test and view allure report
```
- pytest
- allure serve ./allure_report
```

## create requirements
```
- pip3 install pipreqs
- pipreqs . --encoding=utf8

# if requirements.txt already exists, use --forcre {path} to overwrite, like
- pipreqs --force . --encoding=utf8
```

## install requirements
```
- pip3 install -r requirements.txt
```
