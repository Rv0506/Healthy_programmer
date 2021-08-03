import pygame
import datetime
import time


n = datetime.datetime.now()
curr_time = int(n.strftime("%H"))

while (curr_time >= 9 and curr_time <= 17):
    time.sleep(10)
    print("The time is:", n.strftime("%H:%M:%S"))
    pygame.mixer.init()
    pygame.mixer.music.load("fearless2.ogg")
    pygame.mixer.music.play(-1)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(30)
        print("\nYou have been using the screen for long time, please do the excercise\n")
        value = input(
            "Please enter Done after completing to stop the music:\n")
        if(value == "Done"):
            pygame.mixer.music.stop()
            with open("Eyes_log.txt", "a") as eyes:
                eyes.write(str(n)[0:19] + "\n")
        else:
            print("Enter proper value to stop the music\n")
    time.sleep(10)

    pygame.mixer.init()
    pygame.mixer.music.load("ncs_invincible.ogg")
    pygame.mixer.music.play(-1)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(30)
        print("\nYou have been sitting for long time, please do the excercise\n")
        value = input(
            "Please enter Done after completing to stop the music:\n")
        if(value == "Done"):
            pygame.mixer.music.stop()
            with open("Excercise_log.txt", "a") as ex:
                ex.write(str(n)[0:19] + "\n")
        else:
            print("Enter proper value to stop the music\n")
    time.sleep(10)

    pygame.mixer.init()
    pygame.mixer.music.load("ncs_mortal.ogg")
    pygame.mixer.music.play(-1)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(30)
        print("\nYou have not taken the water in a while, please take the water\n")
        value = input(
            "Please enter Drank after drinking to stop the music:\n")
        if(value == "Drank"):
            litres = input(
                "Please enter the quantity of water consumed in litres:\n")
            pygame.mixer.music.stop()
            with open("Water_log.txt", "a") as w:
                w.write(
                    f"Quantity of water taken{litres}litres at {str(n)[0:19]}\n")
                # w.write(f"Quantity of water taken" {}
                #         litres + "litres" + "at" + " " + str(n)[0:19] + "\n")
        else:
            print("Enter proper value to stop the music\n")
    time.sleep(10)

print(litres)
if(int(litres) < 3.5):
    print("You have not taken enough water, take more water to stay hydrated!")
print("Your Working hour is over, please go home and take rest!!")
