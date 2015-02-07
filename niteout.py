import os
import sys
from traitify import Traitify

TRAITIFY_PUBLIC_KEY = os.environ['TRAITIFY_PUBLIC_KEY']
TRAITIFY_SECRET_KEY = os.environ['TRAITIFY_SECRET_KEY']

secret_key = os.environ["TRAITIFY_SECRET_KEY"]
niteout = Traitify(secret_key)

<<<<<<< HEAD
decks = traitify.get_decks()

niteout.deck_id = decks[0].id

assessment = traitify.create_assessment()
        
print decks
=======
    def setUp(self, assessment_id):
        self.assessment = self.traitify.create_assessment('assessment_id')
        traitify.deck_id = decks[0].id
	        
    def assessment_decks(self):
        decks = self.traitify.get_decks()
        self.assertTrue(len(decks) > 0)

	def get_assessment(self):
		self.assertTrue(self.traitify.get_assessment(self.assessment.id).id != None)
>>>>>>> f6c5571325cd251cfefdca9b0ab3bbc424d4fed3

	def get_slides(self):
    	slides = self.traitify.get_slides(self.assessment.id)
    	self.assertTrue(len(slides) > 0)

    def complete_assessment(self):
	    slides = self.traitify.get_slides(self.assessment.id)
	    for slide in slides:
	    	slide.response = True
	    slides = self.traitify.update_slides(self.assessment.id, slides)
	    return self

	def get_personality_types(self):
		self.complete_assessment()
		results = self.traitify.get_personality_types(self.assessment.id)

		self.assertTrue(results["personality_types"][0].personality_type.name != None)

	def default_results(self):
	    self.complete_assessment()
	    results = self.traitify.results(self.assessment.id)

	    self.assertTrue(results.id != None)
	    self.assertTrue(results.personality_types == None)
