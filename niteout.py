from traitify import Traitify
import os

class TraitifyAssessment():
    secret_key = os.environ["TRAITIFY_SECRET_KEY"]
    traitify = Traitify(secret_key)
    assessment = None

    def setUp(self):
        self.assessment = self.traitify.create_assessment('core')
        
    def complete_assessment(self):
        
    def assessment_decks(self):
        decks = self.traitify.get_decks()
        
print decks

traitify.deck_id = decks[0].id



def main():


