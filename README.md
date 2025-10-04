**##AWS Devops Project##**

![1](https://github.com/user-attachments/assets/d2e26e09-efe0-410c-98f4-bebf83a27dbf)



![2](https://github.com/user-attachments/assets/13e7b6a1-ecd4-4302-87b3-76c29012be0e)


![3](https://github.com/user-attachments/assets/95d050c1-51a0-4d9f-851e-0a2df3027a40)




**Please find all the steps to be performed on AWS console.**

Note-
1-I used SCM as a GitHub repository,  not CodeCommit.
2- Need to create an S3 bucket to store the Build Artifact 
3- Also need to create 2 service role, 1 for attaching EC2 and 1 for CodeDeploy (please refer to snips) in advance 

Steps to be followed .

1- Create github repository and place the code (refer my repo) ==> then launch the service code build and integrate github repository with the code build, also S3(refer steps in snips ) ==> then launch EC2 Instance and attach the policy(refer to snip) and install Agent and restart agent service ==> then launch code deploy and attach the policy (refer snips for steps and policies )==> then launch code pipeline(refer snips as well).



I've included for you below the snips for the launch service code build.

<img width="429" height="167" alt="image" src="https://github.com/user-attachments/assets/62cf3405-1b46-4d22-8987-b6eef5cc9875" />

<img width="472" height="422" alt="image" src="https://github.com/user-attachments/assets/5e1c0c57-1954-4c60-84fd-af497e71acdd" />

<img width="473" height="427" alt="image" src="https://github.com/user-attachments/assets/b12dfa81-e1e5-4a43-87e1-40f59ef92127" />

<img width="490" height="452" alt="image" src="https://github.com/user-attachments/assets/4171d968-e31f-46b0-b9e5-db8b2c16c8cc" />

<img width="479" height="430" alt="image" src="https://github.com/user-attachments/assets/8c4e70cd-b9fd-4124-a601-5033c608b591" />

<img width="805" height="766" alt="image" src="https://github.com/user-attachments/assets/3d1080df-77fb-4fd9-b0bc-f8d0a53e1330" />





**Please find the snips to attach service role to attach EC2.**

<img width="910" height="265" alt="image" src="https://github.com/user-attachments/assets/e426e849-a71e-4c63-85f0-b0749702814c" />

<img width="484" height="730" alt="image" src="https://github.com/user-attachments/assets/d62295e3-eb4f-4eba-a75a-f41697db9e2a" />

**##Agent installation commands and restart on EC2 ##**

sudo apt install ruby-full
sudo apt install wget
wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
=sudo systemctl restart codedeploy-agent
systemctl status codedeploy-agent



**Please find below the snips for the launch service code deploy .**

<img width="720" height="153" alt="image" src="https://github.com/user-attachments/assets/8497557a-5df9-4c7f-b874-73beef9daf0c" />

<img width="488" height="314" alt="image" src="https://github.com/user-attachments/assets/a79a5e33-5463-4350-b67f-80d5aba384cf" />

<img width="1462" height="676" alt="image" src="https://github.com/user-attachments/assets/3da8c521-30ec-4451-86db-6a5d285e54c7" />

<img width="607" height="879" alt="image" src="https://github.com/user-attachments/assets/92ca7230-3dcf-4dec-9b90-d9c0c11bfbd4" />

<img width="625" height="897" alt="image" src="https://github.com/user-attachments/assets/36ddb9ca-cd5d-48bd-924b-965116e365a5" />



**Please find below the snips for the launch service code pipeline.**

<img width="885" height="125" alt="image" src="https://github.com/user-attachments/assets/fa2b00e3-09df-402e-9afd-ca6da37ee333" />

<img width="329" height="124" alt="image" src="https://github.com/user-attachments/assets/db71c4da-9808-4b3c-b291-718d85af5bd0" />

<img width="621" height="577" alt="image" src="https://github.com/user-attachments/assets/bff16cef-b6d8-414d-9cbc-6e79d63f6323" />

<img width="313" height="314" alt="image" src="https://github.com/user-attachments/assets/98ed35ba-f4df-4a9d-ae11-05c54fd1d435" />

<img width="314" height="363" alt="image" src="https://github.com/user-attachments/assets/159887c0-066e-4fbd-b487-0de666a385ef" />

<img width="341" height="297" alt="image" src="https://github.com/user-attachments/assets/c3ee325b-18d6-42f9-b749-24763ab4ae2b" />







**Note - Please refer roles along with the policies.**

<img width="224" height="403" alt="image" src="https://github.com/user-attachments/assets/f0f06a46-63ee-4da1-b487-1c14d5f097d5" /> for code deploy


<img width="214" height="365" alt="image" src="https://github.com/user-attachments/assets/345e7948-fbed-4119-839f-7b055b4153f4" /> for EC2



**Finally, the AWS code pipeline successfully executed.**



<img width="551" height="212" alt="image" src="https://github.com/user-attachments/assets/49c63818-a0e9-466b-aa91-fe8f988ad0c8" />

























