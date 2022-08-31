# Mental Health check-in Chat Bot


Submitted by:
|              Name              |   Sec. | B.N.|
|:------------------------------:|:------:|:---:|
| Aya Mohamed Abdulrazzaq        |    1   | 20
| Khloud AbdelAzem               |    1   | 29
| Rania Atef Omar                |    1   | 31 
| Salma Haytham                  |    1   | 37
| Meeran Ahmed                   |    2   | 34
| Nouran Khaled                  |    2   | 41


# **Overview**
- The project is a chatbot for mental health check-in , It is a TCP/IP Server-Client application implemented using socket library in Python
- It is a simple chatbot application that helps diagnose depression


# Demo Link
[Project demo link](https://drive.google.com/file/d/1fVvNNT90Ass-n86qjjO8_EJ6MnNfYje_/view)

# **Features**
- Multiple client can run the application
- Security implementation : Messages between client and server is encrpted using symmetric encryption by Advanced Encryption Standard (AES) CTR Mode with predefined key and random Initialization Vector (IV) implemented using pycryptodome library in python
- Client disconnects automatically if the user is not using the app for an amount of time (timeout)
- The server saves the user's data in a database, and can retrieve the previous scores for the users



## **DEPENDENCIES**
### Packages: 
- pycryptodome 
- PyQt5  
``` 
pip install pycryptodome 
pip install PyQt5
```
*It is recommended to use conda for managing and installing the modules*
<br>

### [requirements.txt](requirements.txt)

## **HOW TO USE**
### 
1. Install dependencies
1. Open server
```
python server.py
```
2. Open Client(s) in a different terminal(s)
```
python client.py
```

