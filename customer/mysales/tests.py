from django.test import TestCase

# Create your tests here.
from mysales.models import product

class MyTest(TestCase):
	def test_record(self):
		try:
			obj = product(name="test3",
			    description="test3",
	            costitem=28,
	            stockquantity=56)
			obj.save()
			self.assertEquals(obj.stockquantity,56,"quantity mismatch")
			self.assertEquals(obj.costitem,28,"product cost mismatch")
			self.assertEquals(obj.volume,1568.00,"volume mismatch")
		except Exception as e:
			print('unable to insert the record')

