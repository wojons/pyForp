import sys
import inspect
import time
import traceback
import resource

class pyForp:
	def __init__(self):
		self.stack, self.calls, self.glob, self.callNum = dict(), list(), dict(), 0 #set some defaults
		
	def start(self): #start all the things needed for tracing
		self.rusage = resource.getrusage(resource.RUSAGE_SELF) #get a snapshot of current usage so we can use that later
		self.stack[0] = {'file' : '', 'function' : '{main}', 'usec' : 0, 'pusec' : 0, 'bytes' : sys.getsizeof(self), 'level' : 0}
		sys.setprofile(self.prof) #change pythons profiler rules :)
		
	def stop(self):
		sys.setprofile(self.void) # set to null no matter what
		rusage = resource.getrusage(resource.RUSAGE_SELF) #get the current usage
		for k in dir(rusage).__iter__(): #loop the usage stats
			if k.startswith('ru_') == True: #make sure its starts off right
				self.glob[k.replace('ru_', '')] = rusage.__getattribute__(k) - self.rusage.__getattribute__(k) #some math with a key rename
	
	def prof(self, frame, event, args):
		pusec = time.time() #grab the current time as soon as we can
		if event == 'call':			
			try: #lets try to get the class name
				class_name = frame.f_locals['self'].__class__.__name__
			except KeyError:
				class_name = None
			
			self.callNum += 1 #up the number of calls we have taken
			trace = dict(inspect.getframeinfo(frame).__dict__) #grab some trace data
			args =  dict(inspect.getargvalues(frame).__dict__) #get args for called functiuon
			self.calls.append({'file' : trace['filename'], 'class' : class_name, 'lineno' : trace['lineno'], 'function' : trace['function'], 'parent' : self.callNum, 'level' : len(inspect.getouterframes(frame))+1, 'args' : args['locals'], 'bytes' : resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024, 'usec' : time.time(), 'pusec' : time.time()-pusec})
			
		elif event == 'return':
			if len(self.calls) > 0:
				call = self.calls.pop()
				call['usec'] = (pusec-call['usec'])*1000000 #get time without profile overhead
				self.stack[call['parent']] = call
				self.stack[call['parent']]['pusec'] += (time.time() - pusec)*1000000 #profiling overhead
	
	def void(self, frame, event, args): #its the way we turn off the profiler :)
		pass
	
	def dump(self): #dump the trace data into a dict
		dump = self.glob.copy()
		dump['stack'] = self.stack.copy()
		return dump
