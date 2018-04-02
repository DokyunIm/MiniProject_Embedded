## Providing air quality information and Detect intrusion system using Raspberry Pi 


### What
  1. Providing air quality information based on location address using IP Address
  2. Detect intrusion using Ultrasonic sensor and Send Email to User
***
### How
  - Providing air quality information
    1. Get IP Address of Raspberry Pi
    2. Find location address using WHOIS OpenAPI and Naver Maps API
    3. Inquire Air quality information using location address by Open API that provided Gorverment
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
    
  
    
    
