import drive_state_data_grabber as drive
import mail_sender

def run():
    firstDriveState = drive.get_drive_state('/dev/sda1')
    secondDriveState = drive.get_drive_state('/dev/sdb1')

    data = '/dev/sda1:<br>'+ firstDriveState
    data +='<br><br>/dev/sdb1:<br>' + secondDriveState
    
    mail_sender.send_notification_mail(data)
    
run()