import sendMail, info, alarm, loacl_backups


if __name__ == '__main__':

    information_dir = info.allInfo()
    n = alarm.compare(information_dir)

    if n == 1 :
        file_content = loacl_backups.backup(information_dir)
        #sendMail.mail(file_content)
        sendMail.mail(file_content)
        #sendMail.mail(str(information_dir))
    else:
        exit
else :
    print('you are not allowed to use this script')



