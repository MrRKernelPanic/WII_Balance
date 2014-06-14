WII_Balance
===========

Wii Balance Board Stuff

To use the balance board you need to install a patched version of cwiid.
https://github.com/conoro/iracer-controllers/raw/master/iracer_balance_board/cwiid_for_balance_board.zip

sudo unzip the cwiid_for_balance_board.zip
sudo dpkg -i *.deb

Sadly to use the board you have to press the sync button EVERY time you wish to use it!

Two example programs, weighdemo.py (from the cwiid site) and the lean_test.py based on the work of 
http://conoroneill.net/controlling-an-i-racer-rc-car-using-a-wii-balance-board-and-raspberry_pi/

