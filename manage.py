#Python Libraries
import sys
import os
import commands
import subprocess
from subprocess import call



#-----------------Functions-----------------
#Depending on which cloud was selected, actions will be taken
def cloud_selector():
    print ("Please enter the value:\n1 for G cloud\n2 for AWS\n3 for Azure")
    selector = input("\nEnter the value : ")

    if selector == 1:
        print ("Selected cloud is G cloud\n")
        gcloud_creator()

    elif selector == 2:
        print ("Selected cloud is AWS\nAWS Configuration is not available for now\n")
    elif selector == 3:
        print ("Selected cloud is Azure\nAzure Configuration is not available for now\n")
    else:
        print ("Please select a value between 1 to 3")
        exit()


#Google cloud vm operations will take place here, which includes creating vm, installing wget, telegraf, changing conf file and starting it.
def gcloud_creator():

    #Vm Options
    print ("Select among following : \n1.Create a vm\n2.Delete a vm\n3.Vm details\n")
    action = input("Enter the value\n")

    #Conditions based on value

    #This will create a new vm
    if action==1:
        #Enter configuration, cpu, ram (.In MB ), machine name
        cpu = raw_input("\nEnter number of Cores\n")
        ram = raw_input("Enter RAM size in MB\n")
        vm_name = raw_input("Enter the name of instance\n")

        #Command to create gcloud instance
        gcloud_command = "gcloud compute instances create " + str(vm_name) + " --custom-cpu " + str(cpu) + " --custom-memory " + str(ram) + "MB --image centos-7-v20180514 --image-project centos-cloud"

        #command that will fetch the external ip of newly created vm
        external_ip = "gcloud compute instances list --filter='name=(\'" + str(vm_name) + "\')' | awk 'NR==2 {print $9}'"
        #print external_ip

        #This will execute the gcloud command from the terminal
        os.system(gcloud_command)
        print ("Machine succesfully created : " + str(cpu) + " core " + str(ram) + " MB RAM")

        #This will execute the command which will fetch external Ip of the new vm
        IP = commands.getoutput(external_ip)

        #print IP
        #installer_and_verfier(IP)
        #Some messages
        print ("Please wait while telegraf is getting installed and configured\n")

        #This command will log in the newly created vm and wget the telegraf rpm file
        login_and_wget_command = "ssh " + str(IP) + " wget https://dl.influxdata.com/telegraf/releases/telegraf-1.6.2-1.x86_64.rpm"

        #print login_and_wget_command
        #This command will install the telegraf rpm file
        telegraf_install = "ssh " + str(IP) + " sudo yum localinstall telegraf-1.6.2-1.x86_64.rpm -y"

        #This command will install wget in the new vm
        wget_install = "ssh " + str(IP) + " sudo yum install wget -y"

        #Copying the default telegraf conf file which is directed to the influxdb running in other server from gcloud storage
        copy_command = "ssh " + str(IP) + " gsutil cp gs://shadowfiend/telegraf.conf ."

        #Moving the copied telegraf conf file to /etc/telegraf
        move_command = "ssh " + str(IP) + " sudo mv /home/saurabh/telegraf.conf /etc/telegraf/telegraf.conf"

        #Command to start telegraf service
        start_telegraf = "ssh " + str(IP) + " sudo systemctl start telegraf"

        #Subprocesses which executes linux commands from python code, they will execute and after completion destroy themselves
        subprocess.call(wget_install, shell=True)
        subprocess.call("exit 1", shell=True)
        subprocess.call(login_and_wget_command, shell=True)
        subprocess.call("exit 1", shell=True)
        subprocess.call(telegraf_install, shell=True)
        subprocess.call("exit 1", shell=True)
        subprocess.call(copy_command, shell=True)
        subprocess.call("exit 1", shell=True)
        subprocess.call(move_command, shell=True)
        subprocess.call("exit 1", shell=True)
        subprocess.call(start_telegraf, shell=True)
        subprocess.call("exit 1", shell=True)

    #This will delete the selected vm
    elif action==2:
        print ("Not added yet")

    #This will show the details of compute engine
    elif action==3:
        print ("Below are the details for compute engine\n")
        os.system('gcloud compute instances list')
    else:
        print ("Incorrect selection")

if __name__=="__main__":
    cloud_selector()
