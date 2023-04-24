# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4, 6, 8 ]
# 0 survivors                4 survivors
# return true
# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4 ]
# 2 survivors  (16 damage)   2 survivors (6 damage)
# return false
# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4, 0, 8 ]
# 1 survivors                3 survivors
# return true
 

import unittest

from Pokemon import Pokemon

class TestPokemon(unittest.TestCase):
    
    def test_make_instance(self):
        self.assertEqual(Pokemon('sean').name, 'sean')

    def test_call_poke_api_good_request(self):
        pokemon = Pokemon('psyduck')
        self.assertEqual(pokemon.abilites, ['damp', 'cloud-nine', 'swift-swim'])
        self.assertEqual(pokemon.types, ['water'])
        self.assertEqual(pokemon.weight, 196)
        

if __name__ == '__main__':
    unittest.main()