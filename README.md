NASPi State Email Notifier

This project monitors the state of two USB drives connected to a Raspberry Pi using smartctl and sends a summary email with their status.

Features

- Runs smartctl on two drives (e.g., /dev/sda1 and /dev/sdb1)
- Collects and formats the output
- Sends an HTML email notification with the drive status

Requirements

- Python 3.6+
- smartmontools (for smartctl)
- Internet connection for sending emails

Setup

1. Install Dependencies

   Make sure smartctl is installed:
   sudo apt-get install smartmontools

   (No external Python packages required for the current code.)

2. Configure Email Settings

   Edit config.py and fill in your email credentials and recipient information:
   mailSettings = dict(
       sender_mail = "your_email@gmail.com",
       app_password = "your_app_password",
       port = 587,
       smtp_address = "smtp.gmail.com",
       destination_mail = "recipient@example.com",
       default_subject = "NASPi Drive State Update",
       default_from = "NASPi",
       default_to = "Recipient Name"
   )
   Tip: For Gmail, you may need to use an App Password.

3. Customize Email Template (Optional)

   Edit resources/mailTemplate.html to change the look of the email.

Usage

Run the main program:
python program.py

This will:
- Collect the state of /dev/sda1 and /dev/sdb1
- Send an email with the results

File Structure

- program.py: Main entry point
- drive_state_data_grabber.py: Gets drive state using smartctl
- mail_sender.py: Sends formatted email notifications
- config.py: Email configuration
- resources/mailTemplate.html: HTML email template

License

MIT License (add your license here