#Python Libraries
import sys
import os
import commands


#Depending on which cloud was selected, actions will be taken
def cloud_selector():
    print "Please enter the value:\n1 for G cloud\n2 for AWS\n3 for Azure"
    selector = input("\nEnter the value : ")

    if selector == 1:
        print "Selected cloud is G cloud\n"
        gcloud_creator()

    elif selector == 2:
        print "Selected cloud is AWS\nAWS Configuration is not available for now\n"
    elif selector == 3:
        print "Selected cloud is Azure\nAzure Configuration is not available for now\n"
    else:
        print "Please select a value between 1 to 3"
        exit()

def gcloud_creator():
    cpu = raw_input("\nEnter number of Cores\n")
    ram = raw_input("Enter RAM size in MB\n")
    vm_name = raw_input("Enter the name of instance\n")
    gcloud_command = "gcloud compute instances create " + str(vm_name) + " --custom-cpu " + str(cpu) + " --custom-memory " + str(ram) + "MB"
    external_ip = "gcloud compute instances list --filter='name=(\'" + str(vm_name) + "\')' | awk 'NR==2 {print $9}'"
    print external_ip
    #os.system(gcloud_command)
    print "Machine succesfully created : " + str(cpu) + " core " + str(ram) + " MB RAM"
    print "Please wait while telegraf is getting installed and configured\n"
    IP = commands.getoutput(external_ip)
    print IP
    login_command = "ssh " + str(IP) + " ls"
    print login_command
    os.system()


if __name__=="__main__":
    cloud_selector()
