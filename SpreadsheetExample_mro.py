import gdata.spreadsheet.service
import gdata.service
import gdata.spreadsheet
import sys
import string
import time

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

  def _ListInsertAction(self):
    # Prepare the dictionary to write
    dictx = {}
    dictx['date'] = time.strftime('%m/%d/%Y')
    dictx['time'] = time.strftime('%H:%M:%S')
    dictx['weight'] = '180'
    entry = self.gd_client.InsertRow(dictx, self.curr_key, self.curr_wksht_id)
    if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
      print 'Inserted!'
  
  def Run(self):
    self._ListInsertAction()
  
def main():
  user = 'mark.routledge@gmail.com'
  pw = 'oqfjcxuxbtofylcv'
  key = ''

  sample = SimpleCRUD(user, pw)
  sample.Run()

if __name__ == '__main__':
  main()
