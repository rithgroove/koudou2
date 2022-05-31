class TimeStamp:
	"""
	[Class] TimeStamp
	the timestamp class using stepcount for the simulation
	
	Attribute:
		- step_count : the current step count in seconds
	"""
	def __init__(self, step_count=0):
		"""
		[Constructor]
		Initialize a TimeStamp Object.

		Parameter:
			- step_count : [int] the current step count. (default = 0)
		"""
		self.step_count = step_count

	def get_hour(self):
		"""
		[Method] get_hour
		get the current hour in 24 hours format. 
		
		Return:[int] the current hour (0-23)
		"""
		return int(int(self.step_count/3600) % 24)

	def get_day(self):
		"""
		[Method] get_day
		Get the current day. eg: 0 = day 0, 12 = day 12th
		
		Return:[int] the current day
		"""
		return int((self.step_count/(24*3600)))

	def get_day_of_week(self):
		"""
		[Method] get_day_of_week
		Get the current day of the week.
		0 = Mon
		1 = Tue
		2 = Wed
		3 = Thu
		4 = Fri
		5 = Sat
		6 = Sun

		Return:[int] the current day of the week
		"""
		return int(int(self.step_count/(24*3600)) % 7)

	def get_second(self):
		"""
		[Method] get_second

		Return:[int] current seconds
		"""
		return self.step_count % 60

	def get_day_of_week_str(self):
		"""
		[Method] get_day_of_week_str
		Get the current day of the week in string format. (Mon,Tue,...)

		Return:[string] the current day of the week in string format
		"""
		temp = self.get_day_of_week()
		if (temp == 0):
			return "Mon"
		if (temp == 1):
			return "Tue"
		if (temp == 2):
			return "Wed"
		if (temp == 3):
			return "Thu"
		if (temp == 4):
			return "Fri"
		if (temp == 5):
			return "Sat"
		if (temp == 6):
			return "Sun"

	def get_minute(self):
		"""
		[Method] get_minute

		Return:[int] current minutes
		"""
		return int(int(self.step_count/60) % 60)

	def get_week(self):
		"""
		[Method] get_week

		Return:[int] current week
		"""
		return int(self.step_count/(7*24*3600))

	def clone(self):
		"""
		[Method] clone
		a method to create a clone of this object

		Return:[TimeStamp] clone of this time stamp
		"""
		return TimeStamp(self.step_count)

	def step(self, step_length = 1):
		"""
		[Method] step
		step method to increase the current step length

		Parameter:
			- step_length = [int] The duration of time that elapsed in seconds format.
		"""
		self.step_count += step_length

	def __str__(self):
		"""
		[Method] __str__
		String method to print the object

		Return : [string] ready to print string
		"""
		tempString = "{}, Week = {} Day = {}\n".format(
			self.get_day_of_week_str(), self.get_week(), self.get_day())
		tempString += "Current Time = {:02d}:{:02d}:{:02d}".format(
			self.get_hour(), self.get_minute(), self.get_second())
		return tempString

	def get_time_only(self):
		"""
		[Method] get_time_only
		Method to return the current elapsed seconds since 00:00 of the current day.

		Return:[int] elapsed seconds since 00:00
		"""
		return self.step_count % (24*60*60)

	def get_hour_min_str(self):
		"""
		[Method] get_hour_min_str
		get string of the current hour-minutes

		Return:[string] return hh:mm
		"""
		h = self.get_hour()
		m = self.get_minute()
		return "{:02d}:{:02d}".format.(h,m)

	def is_after(self, target_time_stamp):
		"""
		[Method] is_after
		Compare this TimeStamp object with another TimeStamp object.

		Example: 
			- time_stamp_a.is_after(time_stamp_b) -> True
			  This means that A is after B

		Parameters:
			- target_time_stamp = [TimeStamp] The targetted time stamp

		Return : [bool] Returns true if this timestamp is bigger than the target timestamp
		""" 
	   return self.step_count > target_time_stamp.step_count