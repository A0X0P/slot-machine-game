
import unittest, os
import slot_machine_game_module as smf

class TestSlotMachineGame(unittest.TestCase):


    def setUp(self):
        with open(smf.balance_file(),'w') as f:
            f.write('10.00')
    

    def tearDown(self):
      if os.path.exists(smf.balance_file()):
           os.remove(smf.balance_file())


    def test_get_symbols_returns_list(self):
        self.assertEqual(len(smf.get_symbols()),4)


    def test_get_spin_valid_output(self):
        smf.random.seed(0)
        spin = smf.get_spin()
        self.assertIsInstance(spin,list)
        self.assertEqual(len(spin),3)
        for symbols in spin:
            self.assertIn(symbols,smf.get_symbols())
    

    def test_getbalance(self):
        bal = smf.get_balance()
        with open(smf.balance_file()) as f:
            balcontent = f.read()
        self.assertEqual(bal,float(balcontent))

    def test_get_balance(self):
        balance = smf.get_balance()
        with open(smf.balance_file()) as f:
            saved = float(f.read())
        self.assertEqual(saved,balance)

    def test_updatebalance(self):
        balance = 10.00    
        smf.update_balance(balance)
        with open(smf.balance_file()) as f:
           saved = float(f.read())
        self.assertEqual(balance,saved) 


if __name__ == '__main__':
    unittest.main()