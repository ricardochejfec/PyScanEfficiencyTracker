import sys
import os
import platform 
from pprint import pprint
import PyScanEfficiencyTracker


#directory = "C:/Users/rchejf/Documents/Scanned Documents/"
directory_in = "G:/PROVOST/Share/OAP/BR/Professional Development Fund/CRC Scanning July 2018/"
#directory = "/Users/ricardochejfec/Documents/School/Anthropology/ANTH 540/Readings/"

directory_out = "C:/Users/rchejf/Documents/Scanned Documents/"

def main():
	master_dict = PyScanEfficiencyTracker.track_pages(directory_in)
	PyScanEfficiencyTracker.make_report(directory_out, master_dict, "Scanning as of )  

if __name__ == '__main__':
    sys.exit(main())