import time
import argparse
from naoqi import ALProxy
import sys, math, time
import socket, struct, threading
from vicon import ViconStreamer

motion = ALProxy('ALMotion', "maecy.local", 9559)
sensors = ALProxy('ALSensors', "maecy.local", 9559)
mem = ALProxy("ALMemory", "maecy.local", 9559)
speech = ALProxy("ALTextToSpeech", "maecy.local", 9559)
posture = ALProxy("ALRobotPosture", "maecy.local", 9559)
touch = ALProxy("ALTouch", "maecy.local", 9559)

#motion = ALProxy('ALMotion', "127.0.0.1", 53167)
#sensors = ALProxy('ALSensors', "127.0.0.1", 53167)
#mem = ALProxy("ALMemory", "127.0.0.1", 53167)
#speech = ALProxy("ALTextToSpeech", "127.0.0.1", 53167)
#posture = ALProxy("ALRobotPosture", "127.0.0.1", 53167)
#touch = ALProxy("ALTouch", "127.0.0.1", 53167)

motion2 = ALProxy('ALMotion', "maeby.local", 9559)
sensors2 = ALProxy('ALSensors', "maeby.local", 9559)
mem2 = ALProxy("ALMemory", "maeby.local", 9559)
speech2 = ALProxy("ALTextToSpeech", "maeby.local", 9559)
posture2 = ALProxy("ALRobotPosture", "maeby.local", 9559)
touch2 = ALProxy("ALTouch", "maeby.local", 9559)
audio2 = ALProxy("ALAudioDevice", "maeby.local", 9559)

#motion2 = ALProxy('ALMotion', "127.0.0.1", 52812)
#sensors2 = ALProxy('ALSensors', "127.0.0.1", 52812)
#mem2 = ALProxy("ALMemory", "127.0.0.1", 52812)
#speech2 = ALProxy("ALTextToSpeech", "127.0.0.1", 52812)
#posture2 = ALProxy("ALRobotPosture", "127.0.0.1", 52812)
#touch2 = ALProxy("ALTouch", "127.0.0.1", 52812)
##############################################################################################################################

#if any of the left hand sensors are touched, set arm position
#MAECY
while True:
	var_Maecy = touch.getStatus()
	time.sleep(2.5)
	print var_Maecy
	LHandL_MC = var_Maecy[14] #LeftHandLeft
	LHandB_MC = var_Maecy[15] #LeftHandBack
	LHandR_MC = var_Maecy[16] #LeftHandRight
	if LHandL_MC[1] == True or LHandB_MC[1] == True or LHandR_MC[1] == True:

		LeftArm  = ["LShoulderPitch", "LShoulderRoll"]
		RightArm = ["RShoulderPitch", "RShoulderRoll"]

		LeftElbow = ["LElbowYaw", "LElbowRoll"]
		RightElbow = ["RElbowYaw", "RElbowRoll"]

		LeftArma  = [0.0, 0.0]
		RightArma =[0.0, 0.0]
		LeftElbowa = [0.0, 0.0]
		RightElbowa = [0.0, 0.0]
		fractionMaxSpeed  = 0.2

		motion.setAngles(LeftArm, LeftArma, fractionMaxSpeed)
		motion.setAngles(RightArm, RightArma, fractionMaxSpeed)
		motion.setAngles(LeftElbow, LeftElbowa, fractionMaxSpeed)
		motion.setAngles(RightElbow, RightElbowa, fractionMaxSpeed)
		break
	#time.sleep(5)

#check arms MAECY
sensorAngles = motion.getAngles("RShoulderPitch", True) 
if sensorAngles > 50:
	print ('yay') 
	speech.post.say("Ready! Give me the box.")


#MAEBY
#if (mem2.getData('FrontTactilTouched', 0) or mem2.getData('MiddleTactilTouched', 0) or mem2.getData('RearTactilTouched', 0)):
while True:
	var_Maeby = touch2.getStatus()
	time.sleep(2.5)
	print('GETTING MAEBY')
	print var_Maeby
	LHandL_MB = var_Maeby[14] #LeftHandLeft
	LHandB_MB = var_Maeby[15] #LeftHandBack
	LHandR_MB = var_Maeby[16] #LeftHandRight
	if LHandL_MB[1] == True or LHandB_MB[1] == True or LHandR_MB[1] == True:
		LeftArm  = ["LShoulderPitch", "LShoulderRoll"]
		RightArm = ["RShoulderPitch", "RShoulderRoll"]

		LeftElbow = ["LElbowYaw", "LElbowRoll"]
		RightElbow = ["RElbowYaw", "RElbowRoll"]

		LeftArma  = [0.0, 0.0]
		RightArma =[0.0, 0.0]
		LeftElbowa = [0.0, 0.0]
		RightElbowa = [0.0, 0.0]
		fractionMaxSpeed  = 0.2

		motion2.setAngles(LeftArm, LeftArma, fractionMaxSpeed)
		motion2.setAngles(RightArm, RightArma, fractionMaxSpeed)
		motion2.setAngles(LeftElbow, LeftElbowa, fractionMaxSpeed)
		motion2.setAngles(RightElbow, RightElbowa, fractionMaxSpeed)
		break

#check arms MAEBY
sensorAngles2 = motion2.getAngles("RShoulderPitch", True) 
if sensorAngles2 > 50:
	print ('yay') 
	speech2.post.say("Ready! Give me the box.")


#give box MAECY
while True:
	var_Maecy = touch.getStatus()
	print var_Maecy
	time.sleep(2.5)
	print('GETTING MAECY CLOSE')
	HandRL_MC = var_Maecy[17] #HandRightLeft
	HandRB_MC = var_Maecy[18] #HandRightBack
	HandRR_MC = var_Maecy[19] #HandRightRight
	if HandRL_MC[1] == True or HandRB_MC[1] == True or HandRR_MC[1] == True:
		motion.post.openHand('RHand')
		motion.post.openHand('LHand')
		time.sleep(6)
		motion.post.closeHand('RHand')
		motion.post.closeHand('LHand')
		var = 1
		time.sleep(2.5)
		print('closed')
		break
		

if var == 1:
	speech.say("I have the box. Target acquired.")


#Give box to MAEBY
while True:
	var_Maeby = touch2.getStatus()
	time.sleep(2.5)
	print('GETTING MAEBY CLOSE')
	print var_Maeby
	HandRL_MB = var_Maeby[17] #HandRightLeft
	HandRB_MB = var_Maeby[18] #HandRightBack
	HandRR_MB = var_Maeby[19] #HandRightRight
	RArm_MB = var_Maeby[5]
	if HandRL_MB[1] == True or HandRB_MB[1] == True or HandRR_MB[1] == True or RArm_MB == True:
		motion2.post.openHand('RHand')
		motion2.post.openHand('LHand')
		time.sleep(6)
		motion2.post.closeHand('RHand')
		motion2.post.closeHand('LHand')
		var2 = 1
		print('closed')
		break
	
if var2 == 1:
	speech2.say("I have the box. Target acquired.")
time.sleep(10)

#posture.stopMove()
while True:
	# var_Maecy = touch.getStatus()
	# LHandL_MC = var_Maecy[14] #LeftHandLeft
	# LHandB_MC = var_Maecy[15] #LeftHandBack
	# LHandR_MC = var_Maecy[16] #LeftHandRight

	# var_Maeby = touch.getStatus()
	# LHandL_MB = var_Maeby[14] #LeftHandLeft
	# LHandB_MB = var_Maeby[15] #LeftHandBack
	# LHandR_MB = var_Maeby[16] #LeftHandRight

	#if (LHandL_MC[1] == True or LHandB_MC[1] == True or LHandR_MC[1] == True):
 	#X = 0.5 
 	#Y = 0.0
 	#Theta = 0.0
 	#Frequency = 0.2 # low speed
 	#leftArmEnable  = False
 	#rightArmEnable  = False

 	#motion.setWalkArmsEnabled(leftArmEnable, rightArmEnable)
 	#motion2.setWalkArmsEnabled(leftArmEnable, rightArmEnable)

	#Make Maecy walk
	#if __name__ == "__main__":
	s = ViconStreamer()
	s.connect("128.84.189.209", 800)

	s2 = ViconStreamer()
	s2.connect("128.84.189.209", 800)

	if len(sys.argv) > 1 and sys.argv[1] in ["-l", "--list"]:
	    s.printStreamInfo()
	    sys.exit(0)


	if len(sys.argv) > 1 and sys.argv[1] in ["-l", "--list"]:
	    s2.printStreamInfo()
	    sys.exit(0)

	streams = s.selectStreams(["Time", "maecy_good:maecy <t-X>", "maecy_good:maecy <t-Y>", "maecy_good:maecy <a-Z>"])
	streams2 = s2.selectStreams(["Time", "maeby:maeby <t-X>", "maeby:maeby <t-Y>", "maeby:maeby <a-Z>"])

	s.startStreams(verbose=False)
	s2.startStreams(verbose=False)

	try:
	    # Wait for first data to come in
	    while s.getData() is None: pass

	    while True:
	        #print "  ".join(streams) maecy
	        (t, x, y, o) = s.getData()
	        data = [t/100, x/1000, y/1000, 180*o/math.pi]
	        print (data[3])
	        time.sleep(1)

	        #s2 maeby
	        #print "  ".join(streams2)
	        (t2, x2, y2, o2) = s2.getData()
	        data2 = [t2/100, x2/1000, y2/1000, 180*o2/math.pi]
	        print (data2[3])
	        time.sleep(0.1)


	        Frequency = 1 # low speed

	        motion.post.setWalkTargetVelocity(-0.5, 0, 0, Frequency)
	        #motion.post.moveTo(-1, -1, 0)


	        xd = abs((data[1] - data2[1])/(math.sqrt((data[1] - data2[1])**2 + (data[2] - data2[2])**2)))
	        yd = abs((data[2] - data2[2])/(math.sqrt((data[1] - data2[1])**2 + (data[2] - data2[2])**2)))
	        omegadot=0;
	        print 'xd'+ str((xd))
	        print 'yd' + str((yd))
	        print 'data'+ str((data))
	        print 'data2' + str((data2))
	        motion2.setWalkTargetVelocity(xd*Frequency, yd*Frequency, omegadot, Frequency)

	#walking
	        #motion2.moveTo(-data[1] + data2[1], -data[2] + data2[2], -data[3] + data2[3])
	        print math.sqrt((data2[1]-data[1])**2 + (data2[2] - data[2])**2)

	        if math.sqrt((data2[1]-data[1])**2 + (data2[2] - data[2])**2) < 0.6:
	            Frequency = 0
	            motion2.post.setWalkTargetVelocity(xd*Frequency, yd*Frequency, 0, Frequency)
	            motion.post.setWalkTargetVelocity(xd*Frequency, yd*Frequency, 0, Frequency)
	            speech2.say("Mission accomplished.")
	            #audio2.muteAudioOut(True)
	            break
	#turning          
	        if data[3]<0:
	            data[3]=data[3]+360;
	        if data2[3]<0:
	            data2[3]=data2[3]+360;

	        if abs(abs(data2[3]-data[3])-180)<=(20):
	            motion2.setWalkTargetVelocity(xd*Frequency, yd*Frequency, omegadot, Frequency)
	        if abs(abs(data2[3]-data[3])-180)>=(20):
	            motion2.setWalkTargetVelocity(xd*Frequency, yd*Frequency, -omegadot, Frequency)

	except KeyboardInterrupt:
	    Frequency = 0
	    motion.setWalkTargetVelocity(0, 0, 0, 0)
	    motion2.setWalkTargetVelocity(0, 0, 0, 0)
	s.close()