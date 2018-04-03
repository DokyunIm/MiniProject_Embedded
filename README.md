## Providing air quality information and Detecting intrusion system using Raspberry Pi 


### What
  1. Providing air quality information based on location address using IP Address
  2. Detecting intrusion using Ultrasonic sensor and Send Email to User
***
### How
  - Providing air quality information
    1. Get IP Address of Raspberry Pi
    2. Find location address using WHOIS OpenAPI and Naver Maps API
    3. Inquire Air quality information using location address by Open API that provided government
    4. If moving is detected using Ultrasonic sensor, LED turns on according to the air quality
        - If air quality is good, LED turn on Blue
        - If air quality is normal, LED turn on Green
        - If air quality is bad, LED turn on Yellow
        - If air quality is too bad, LED turn on Red
        
  - Detect intrusion
    1. If moving id detected using Ultrasonic sensor,
    2. LED turn on Red and is blinking
    3. Send Email to user
    
  - Change mode
    + If press button during 2 sec, change the mode
    + Home mode is to provide air quality information
    + Detect mode is to detect intrusion and send Email to user
***    
### Details
  - airinfo.py
    + Get IP Address of Raspberry Pi
    + Find Location address
    + Inquire air quality information
  
  
  - notify.py
    + Send Email to User
  
  - mini.py
    + Main program
    + Control LED
    + Control Ultrasonic sensor
    + Control Button
***
### Notice
  -  If you want to test or run this code, you need key for using whois API, Naver Maps API, gmail smtp login and Open API provided government
  -  <https://xn--c79as89aj0e29b77z.xn--3e0b707e/kor/whois/openAPI_KeyCre.jsp>
  -  <https://developers.naver.com/docs/common/openapiguide/>
  -  <https://www.data.go.kr/>
  -  Save your key into key.secret file
  <pre><code>key.secret file
    { 
      "client_id": "{your key}",
      "client_secret": "{your key}",
      "auth_key": "{your key}",
      "whois_key": "{your key}",
      "openapi_key": "{your key}"
    }
  </code></pre>
  <pre><code>
    client id : Naver Maps API
    client secret : Naver Maps API
    auth key : gmail smtp login
    whois key : whois api
    openapi key : open api provided government
  </code></pre>
    
    
