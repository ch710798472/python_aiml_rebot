import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
# kernel = aiml.Kernel()
# kernel.learn("std-startup.xml")
# kernel.respond("load aiml b")

print "hello, you can talk to me! Just tell me ~"
while True:
    message = raw_input("I say: ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        print "robot say: %s" % bot_response
