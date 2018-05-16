## zox cloud management script
------
These are the details of what this code includes 

 1. I just had gcloud account, I have some problem with my aws account, so this code is for gcloud.
 2. You will be asked to select cloud, later code can be added to respective function.
 3. You will be asked to select the option, to create vm, to delete vm, to see the compute engine details.
 4. VM delettion is not enabled for now, you can create a vm or check the details of compute engine.
 5. If vm creation is the selected option then you will be asked to select the configuration of the vm, os is by default centos.
 6. After providing the details, it will take some time to create vm.
 7. Once vm is created, wget will be installed, telegraf rpm file will be downloaded, telegraf will be installed, telegraf conf file will be copied from gcloud storage and telegraf will be started.
 8. Telegraf is configured to put the data into influxdb running on other server.
 9. Once everything is done, open the ip where grafan is running, there you can add the graph. This part can be automated.
  
  > Due to some problem, I had lack of time so this is what I did. Rest of the improvements can be done.
  Code was written and tested on gcloud instance as my personal laptop is not working. I will provide the access when needed by mail.
