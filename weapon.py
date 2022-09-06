class Weapon(object):
	def __init__(self, hitbox, delay, animspd):
		self.hitbox = hitbox
		#hitbox is a tuple of length and width
		self.animspd = animspd
		self.delay = delay
	
	def attack(self):
		pass
		"""wait delay frames
		blit frames until very near end
		sensor = Rect((680, char_y + 20), self.hitbox)
		blit last frames and stay on final frame for a while
		change frames a speed defined by self.animspd"""
