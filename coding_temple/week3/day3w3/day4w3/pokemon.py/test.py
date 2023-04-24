import unittest
from pokemon import Pokemon

class TestPokemon(unittest.TestCase):

# coreectly make an instance
    def test_make_instance(self:
        self.assertEqual(pokemon('sean').name, 'sean'))

    def test_call_poke_api_good_request(self):
        pokemon = Pokemon('psyduck')
        self.assertEqual(pokemon.abilities, ['damp', 'cloud-nine', 'swift-swim'])
        self.assertEqual(pokemon.types, ['water'])
        self.assertEqual(pokemon.weight, 196)

    def test_evolve(self):
          pokemon = Pokemon('1')
          evo_chain = pokemon.get_evolution_chain(
            self.assertIsInstance(evo_chain, dict)
            pokemon.evolve(evo_chain)
            self.assertEqual(pokemon.name, 'ivysaur')
            self.assertEqual(pokemon.weight, 130)

    def test_casing(self):
        self.assertEqual(Pokemon('Psyduck').abilities , ['damb', 'cloud-nine', 'swift-swim '])
        
    def test_search_by_index(self):
    

if __name__ == '__main__':
         unittest.main()
