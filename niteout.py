from traitify import Traitify
import os

secret_key = os.environ["TRAITIFY_SECRET_KEY"]
niteout = Traitify(secret_key)

decks = traitify.get_decks()

niteout.deck_id = decks[0].id

assessment = traitify.create_assessment()
        
print decks

traitify.deck_id = decks[0].id



def main():


