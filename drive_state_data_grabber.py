import subprocess

def get_drive_state(drivePath):
    argument = '-a ' + drivePath
    result = subprocess.run('smartctl '+ argument, capture_output=True, shell=True)
    return result.stdout.decode('utf-8')