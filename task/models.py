from django.db import models

class Task( models.Model ):
	"""
	Model for storing `tasks`
	"""

	name = models.CharField( max_length = 100 )
	age = models.CharField( max_length = 100 )
	result = models.CharField( max_length = 100 )
