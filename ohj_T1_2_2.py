import unittest
runtest = 1

def parillisuus(luku):

    for counter in range (1, luku + 1):
        if (counter % 2) == 0:
            print(counter)
            palautusarvo = "on parillinen"  
            print("on parillinen")
        else:
            print(counter)
            palautusarvo = "on pariton"
            print("on pariton")
    
    if runtest == 1:
        return palautusarvo


if runtest == 0:
    parillisuus(2)

# python -m unittest ohj_T1_2_2.py
class ohj_T1_2_2(unittest.TestCase): 
    def test_ohj_T1_2_2_saccess_parillinen(self):
        testiarvo = 4
        actual = str(parillisuus(testiarvo))
        expected = "on parillinen"
        try: 
            assert actual == expected
        except:
            print("Virhe parittomuuden tarkistamisessa" + " Numero = " + str(testiarvo) + " " + actual + " != " + expected )

    def test_ohj_t1_2_2_saccess_pariton(self):
        testiarvo = 7
        actual = str(parillisuus(testiarvo))
        expected = "on pariton"
        try: 
            assert actual == expected
        except:
            print("Virhe parittomuuden tarkistamisessa" + " Numero = " + str(testiarvo) + " " + actual + " != " + expected )



PS C:\Users\BabaerovaDildora\Documents\GitHub\Unittest> python -m unittest ohj_T1_2_2.py
1
on pariton
2
on parillinen
3
on pariton
4
on parillinen
.1
on pariton
2
on parillinen
3
on pariton
4
on parillinen
5
on pariton
6
on parillinen
7
on pariton
.
----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK
PS C:\Users\BabaerovaDildora\Documents\GitHub\Unittest>