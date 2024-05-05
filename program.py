import driveStateDataGrabber as drive
import mailSender

def Run():
    firstDriveState = drive.GetDriveState('/dev/sda1')
    secondDriveState = drive.GetDriveState('/dev/sdb1')
    mailSender.sendNotificationMail(firstDriveState +'\n\n' + secondDriveState)
    
Run()