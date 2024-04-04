# automation testing


***
## structure

automation-testing/  
&nbsp;|─ api  
&nbsp;|─ common  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |─ request.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ logger.py  
&nbsp;|─ config  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |─ environment.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ environment.yaml  
&nbsp;|─ operation  
&nbsp;|─ testcases  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |─ member  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |─ test_login.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ conftest.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ conftest.py  
&nbsp;|─ testdata  
&nbsp;|─ requirements.txt  
&nbsp;|─ .gitignore  
&nbsp;|─ Dockerfile  
&nbsp;|─ pytest.ini  
└─ README.md  

***
## structure summary

api -> only for api call  
common -> some common package or tool, like request, logger  
config -> environment, like sit, uat or production  
operation -> processing data and get ready to call api  
testcases -> execute test  
member -> group by service  
testdata -> put testdata for testcases  
pytest.ini -> pytest setting

***

## run test and view allure report
```
- pytest
(defalut env is sit, run uat with 'pytest --env=uat')
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
