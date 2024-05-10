import driveStateDataGrabber as drive
import mailSender

def Run():
    firstDriveState = drive.GetDriveState('/dev/sda1')
    secondDriveState = drive.GetDriveState('/dev/sdb1')

    data = '/dev/sda1:<br>'+ firstDriveState
    data +='<br><br>/dev/sdb1:<br>' + secondDriveState
    
    mailSender.sendNotificationMail(data)
    
Run()