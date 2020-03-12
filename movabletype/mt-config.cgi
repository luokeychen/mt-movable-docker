## Movable Type Configuration File
##
## This file defines system-wide
## settings for Movable Type. In 
## total, there are over a hundred 
## options, but only those 
## critical for everyone are listed 
## below.
##
## Information on all others can be 
## found at:
##  https://www.movabletype.org/documentation/config

#======== REQUIRED SETTINGS ==========

CGIPath        /cgi-bin/mt/
StaticWebPath  /mt-static/
StaticFilePath /usr/local/apache2/cgi-bin/mt/mt-static

#======== DATABASE SETTINGS ==========

ObjectDriver DBI::mysql
Database mt
DBUser root
DBPassword pass
DBHost mysql

#======== MAIL =======================
EmailAddressMain roger.luo@cn.msols.com
MailTransfer smtp
SMTPServer mailhog
SMTPPort 1025
    
DefaultLanguage en-us

ImageDriver ImageMagick
