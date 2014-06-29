import sys
import cwiid
import gdata.spreadsheet.service
import gdata.service
import gdata.spreadsheet
import string
import time

#total_readings = 0
user = 'mark.routledge@gmail.com'
pw = 'oqfjcxuxbtofylcv'
key = ''

class SimpleCRUD:
  def __init__(self, email, password):
    self.gd_client = gdata.spreadsheet.service.SpreadsheetsService()
    self.gd_client.email = email
    self.gd_client.password = password
    self.gd_client.source = 'Spreadsheets GData Sample'
    self.gd_client.ProgrammaticLogin()
    self.curr_key = '1VKZSW_a9O84t02gOKvcoCC1rNtxjgkgtErMWguHnUKc'
    self.curr_wksht_id = 'od6'
    self.list_feed = None

  def _InsertRowAction(self,weight):
    # Prepare the dictionary to write
    dictx = {}
    dictx['date'] = time.strftime('%m/%d/%Y')
    dictx['time'] = time.strftime('%H:%M:%S')
    dictx['weight'] = str(weight)
    entry = self.gd_client.InsertRow(dictx, self.curr_key, self.curr_wksht_id)
    if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
      print 'Inserted!'
  
def main():
	#Put the balance board in detect mode.
	print 'Put Wiimote in discoverable mode now (press 1+2)...'
	global wiimote
	if len(sys.argv) > 1:
		wiimote = cwiid.Wiimote(sys.argv[1])
	else:
		wiimote = cwiid.Wiimote()

	wiimote.rpt_mode = cwiid.RPT_BALANCE | cwiid.RPT_BTN
	wiimote.request_status()

	balance_calibration = wiimote.get_balance_cal()
	named_calibration = { 'right_top': balance_calibration[0],
						  'right_bottom': balance_calibration[1],
						  'left_top': balance_calibration[2],
						  'left_bottom': balance_calibration[3],
						}

	exit = False
	total_readings = 0
        sample = SimpleCRUD(user, pw)

	x=0
	#Do this test 5 times!
	while x<5:
		print ("Recording Your weight! ")
		wiimote.request_status()
		#Test the weight fromt the board, if it returns zero not balanced enough.
		recorded_weight = calcweight(wiimote.state['balance'], named_calibration)
		if recorded_weight != 0:
			total_readings = total_readings + (recorded_weight / 100.0, )[0]
			x=x+1
		else:
			print 'Centre yourself on the board!'
		print (total_readings)
		time.sleep(1)

	#Take a decent average from the 5 readings.
	average_reading=(total_readings)/5
	print (average_reading)	
	
	#Insert the value into the spreadsheet!
	sample._InsertRowAction(average_reading)
	return 0

def calcweight( readings, calibrations ):
	"""
	Determine the weight of the user on the board in hundredths of a kilogram
	"""
	weight = 0
	for sensor in ('right_top', 'right_bottom', 'left_top', 'left_bottom'):
		reading = readings[sensor]
		calibration = calibrations[sensor]
		if reading > calibration[2]:
			print "Warning, %s reading above upper calibration value" % sensor
		# 1700 appears to be the step the calibrations are against.
		# 17kg per sensor is 68kg, 1/2 of the advertised Japanese weight limit.
		if reading < calibration[1]:
			weight += 1700 * (reading - calibration[0]) / (calibration[1] - calibration[0])
		else:
			weight += 1700 * (reading - calibration[1]) / (calibration[2] - calibration[1]) + 1700

	return weight

if __name__ == "__main__":
	sys.exit(main())
