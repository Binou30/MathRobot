import math #import math library
import time #import time library
import os #import terminal control library

def pythagore(): #défine PythRobot
    print("JI am PythRobot, I execute the Pythagorean theorem")
    time.sleep(0.5)
    print("I would like to point out that we are working in a triangle ABC and that each side will be expressed in CAPITALS.")
    time.sleep(0.5)
    while True:
        actionpyt = input("Enter the action number you want to perform:\n1. Find the length of a side\n2. Find if a triangle is right angled\n3. Quit Pythrobot\n")
        while actionpyt != "1" and actionpyt != "2" and actionpyt != "3":
            print("Incorrect entry")
            time.sleep(1.5)
            actionpyt = input("Enter the action number you want to perform:\n1. Find the length of a side\n2. Find if a triangle is right angled\n3. Quit Pythrobot\n")
        if actionpyt == "1": #lines 17 to 218 = the function find the length of a side
            angledroit1 = input("Enter the name of the right angle (in one letter)")
            while angledroit1 != "A" and angledroit1 != "B" and angledroit1 != "C":
                print("Incorrect entry")
                time.sleep(1.5)
                angledroit1 = input("Enter the name of the right angle (in one letter)")
            if angledroit1 == "A":
                longatrouver1 = input("Enter the length of the side to be found")
                while longatrouver1 != "BC" and longatrouver1 != "AC" and longatrouver1 != "AB":
                    print("Incorrect entry")
                    time.sleep(1.5)
                    longatrouver1 = input("Enter the length of the side to be found")
                if longatrouver1 == "BC":
                    while True:
                        entrée = input("Enter the length of AC")
                        try:
                            AC1 = float(entrée)
                            break
                        except ValueError:
                            print("Incorrect entry")
                            time.sleep(1.5)
                    while True:
                        entrée = input("Enter the length of AB")
                        try:
                            AB1 = float(entrée)
                            break
                        except ValueError:
                            print("Incorrect entry")
                            time.sleep(1.5)
                    BC1 = math.sqrt(AC1*AC1 + AB1*AB1)
                    print("BC = ", BC1, "cm")
                else:
                    if longatrouver1 == "AC":
                        while True:
                            entrée = input("Enter the length of BC")
                            try:
                                BC2 = float(entrée)
                                break
                            except ValueError:
                                print("Incorrect entry")
                                time.sleep(1.5)   
                        while True:
                            entrée = input("Enter the length of AB")
                            try:
                                AB2 = float(entrée)
                                break
                            except ValueError:
                                print("Incorrect entry")
                                time.sleep(1.5)
                        AC2 = math.sqrt(BC2*BC2 - AB2*AB2)
                        print("AC = ", AC2, "cm")
                    else:
                        if longatrouver1 == "AB":
                            while True:
                                entrée = input("Enter the length of AC")
                                try:
                                    AC3 = float(entrée)
                                    break
                                except ValueError:
                                    print("Incorrect entry")
                                    time.sleep(1.5)
                            while True:
                                entrée = input("Enter the length of BC")
                                try:
                                    BC3 = float(entrée)
                                    break
                                except ValueError:
                                    print("Incorrect entry")
                                    time.sleep(1.5)
                            AB3 = math.sqrt(BC3*BC3 - AC3*AC3)
                            print("AB = ", AB3, "cm")
            else:
                if angledroit1 == "B":
                    longatrouver2 = input('Enter the length of the side to be found')
                    while longatrouver2 != "BC" and longatrouver2 != "AC" and longatrouver2 != "AB":
                        print("Incorrect entry")
                        time.sleep(1.5)
                        longatrouver2 = input("Enter the length of the side to be found")
                    if longatrouver2 == "BC":
                        while True:
                            entrée = input("Enter the length of AC")
                            try:
                                AC4 = float(entrée)
                                break
                            except ValueError:
                                print("Incorrect entry")
                                time.sleep(1.5)
                        while True:
                            entrée = input("Enter the length of AB")
                            try:
                                AB4 = float(entrée)
                                break
                            except ValueError:
                                print("Incorrect entry")
                                time.sleep(1.5)
                        BC4 = math.sqrt(AC4*AC4 - AB4*AB4)
                        print("BC = ", BC4, "cm")
                    else:
                        if longatrouver2 == "AC":
                            while True:
                                entrée = input("Enter the length of BC")
                                try:
                                    BC5 = float(entrée)
                                    break
                                except ValueError:
                                    print("Incorrect entry")
                                    time.sleep(1.5)
                            while True:
                                entrée = input("Enter the length of AB")
                                try:
                                    AB5 = float(entrée)
                                    break
                                except ValueError:
                                    print("Incorrect entry")
                                    time.sleep(1.5)
                            AC5 = math.sqrt(BC5*BC5 + AB5*AB5)
                            print("AC", AC5, "cm")
                        else:
                            if longatrouver2 == "AB":
                                while True:
                                    entrée = input("Enter the length of AC")
                                    try:
                                        AC6 = float(entrée)
                                        break
                                    except ValueError:
                                        print("Incorrect entry")
                                        time.sleep(1.5)
                                while True:
                                    entrée = input("Enter the length of BC")
                                    try:
                                        BC6 = float(entrée)
                                        break
                                    except ValueError:
                                        print("Incorrect entry")
                                        time.sleep(1.5)
                                AB6 = math.sqrt(AC6*AC6 - BC6*BC6)
                                print("AB = ", AB6, "cm")
                else:
                    if angledroit1 == "C":
                        longatrouver3 = input('Enter the length of the side to be found')
                        while longatrouver3 != "BC" and longatrouver3 != "AC" and longatrouver3 != "AB":
                            print("Incorrect entry")
                            time.sleep(1.5)
                            longatrouver3 = input("Enter the length of the side to be found")
                        if longatrouver3 == "BC":
                            while True:
                                entrée = input("Enter the length of AC")
                                try:
                                    AC7 = float(entrée)
                                    break
                                except ValueError:
                                    print("Incorrect entry")
                                    time.sleep(1.5)
                            while True:
                                entrée = input("Enter the length of AB")
                                try:
                                    AB7 = float(entrée)
                                    break
                                except ValueError:
                                    print("Incorrect entry")
                                    time.sleep(1.5)
                            BC7 = math.sqrt(AB7*AB7 - AC7*AC7)
                            print("BC = ", BC7, "cm")
                        else:
                            if longatrouver3 == "AC":
                                while True:
                                    entrée = input("Enter the length of BC")
                                    try:
                                        BC8 = float(entrée)
                                        break
                                    except ValueError:
                                        print("Incorrect entry")
                                        time.sleep(1.5)
                                while True:
                                    entrée = input("Enter the length of AB")
                                    try:
                                        AB8 = float(entrée)
                                        break
                                    except ValueError:
                                        print("Incorrect entry")
                                        time.sleep(1.5)
                                AC8 = math.sqrt(AB8*AB8 - BC8*BC8)
                                print("AC = ", AC8, "cm")
                            else:
                                if longatrouver3 == "AB":
                                    while True:
                                        entrée = input("Enter the length of AC")
                                        try:
                                            AC9 = float(entrée)
                                            break
                                        except ValueError:
                                            print("Incorrect entry")
                                            time.sleep(1.5)
                                    while True:
                                        entrée = input("Enter the length of BC")
                                        try:
                                            BC9 = float(entrée)
                                            break
                                        except ValueError:
                                            print("Incorrect entry")
                                            time.sleep(1.5)
                                    AB9 = math.sqrt(AC9*AC9 + BC9*BC9)
                                    print("AB = ", AB9, "cm")
        else:
            if actionpyt == "2": #lines 221 to 266 = the converse and the contrapositive of the theorem
                while True:
                    entrée = input("Enter the length of AB")
                    try:
                        AB10 = float(entrée)
                        break
                    except ValueError:
                        print("Incorrect entry")
                        time.sleep(1.5)
                while True:
                    entrée = input("Enter the length of AC")
                    try:
                        AC10 = float(entrée)
                        break
                    except ValueError:
                        print("Incorrect entry")
                        time.sleep(1.5)
                while True:
                    entrée = input("Enter the length of BC")
                    try:
                        BC10 = float(entrée)
                        break
                    except ValueError:
                        print("Incorrect entry")
                        time.sleep(1.5)
                listecôté = [AB10, AC10, BC10]
                listetri = sorted(listecôté)
                plusgrandcôté = max(AB10, AC10, BC10)
                if plusgrandcôté == AB10:
                    angle = "C"
                else:
                    if plusgrandcôté == AC10:
                        angle = "B"
                    else:
                        if plusgrandcôté == BC10:
                            angle = "A" 
                deuxautrescôtés = listetri[:2]
                carréplusgdcôté = round(plusgrandcôté**2, 2)
                carréautrecôté1 = deuxautrescôtés[0]**2
                carréautrecôté2 = deuxautrescôtés[1]**2
                sommecarrésautrescôtésavecarrondi = round(carréautrecôté1 + carréautrecôté2, 2)
                sommecarrésautrescôtéssansarrondi = carréautrecôté1 + carréautrecôté2
                if int(carréplusgdcôté * 1000) / 1000 == int(sommecarrésautrescôtésavecarrondi * 1000) / 1000 or int(carréplusgdcôté * 1000) / 1000 == int(sommecarrésautrescôtéssansarrondi * 1000) / 1000: #on vérifie si "AB2 = AC2+BC2"
                    print("Triangle ABC is right-angled in", angle)
                else:
                    if plusgrandcôté*plusgrandcôté != deuxautrescôtés[0]*deuxautrescôtés[0] + deuxautrescôtés[1]*deuxautrescôtés[1]:
                        print("Triangle ABC is not a right triangle")
            else:
                if actionpyt == "3":
                    print("Bye !")
                    time.sleep(1.5)
                    break

def trigonométrie(): #we define trigonometry
    print("I am TrigoBot, I will be performing the trigonometric functions sin, cos and tan.")
    time.sleep(0.5)
    print("I specify that the angle of the function will be written with ONLY its middle letter, that we are working in a triangle ABC and that each side will be expressed in CAPITALS")
    time.sleep(0.5)
    while True:
        actiontrig = input("Enter the action number you want to perform:\n1. Find the length of a side\n2. Find the measure of an angle\n3. Quit TrigoBot\n")
        while actiontrig != "1" and actiontrig != "2" and actiontrig!= "3":
            print("Incorrect entry")
            time.sleep(1.5)
            actiontrig = input("Enter the action number you want to perform:\n1. Find the length of a side\n2. Find the measure of an angle\n3. Quit TrigoBot\n")
        if actiontrig == "1": #lines 285 to 678 = the function find the length of a side with sin, cos and tan
            angledroittrig = input("Enter the name of the right angle")
            while angledroittrig != "A" and angledroittrig != "B" and angledroittrig != "C":
                print("Incorrect entry")
                time.sleep(1.5)
                angledroittrig = input("Enter the name of the right angle")
            côtéaveclongueurtrig = input("Enter the length of the side you have (first its name, then its length in cm)")
            while côtéaveclongueurtrig[:2] != "AB" and côtéaveclongueurtrig[:2] != "AC" and côtéaveclongueurtrig[:2] != "BC":
                print("Incorrect entry")
                time.sleep(1.5)
                côtéaveclongueurtrig = input("Enter the length of the side you have (first its name, then its length in cm)")
            while True:
                try:
                    float(côtéaveclongueurtrig[2:])
                    break
                except ValueError:
                    print("Incorrect entry")
                    time.sleep(1.5)
                    côtéaveclongueurtrig = input("Enter the length of the side you have (first its name, then its length in cm)")
            angleavecmesuretrig = input("Enter the measure of the angle you have (first its name, then its measure, the one that is not 90° and without the degree sign)")
            while angleavecmesuretrig[0] != "A" and angleavecmesuretrig[0] != "B" and angleavecmesuretrig[0] != "C":
                print("Incorrect entry")
                time.sleep(1.5)
                angleavecmesuretrig = input("Enter the measure of the angle you have (first its name, then its measure, the one that is not 90° and without the degree sign)")
            if angledroittrig == "A":
                if côtéaveclongueurtrig[:2] == "AB":
                    if angleavecmesuretrig[0] == "B":
                        côtéquoncherche1 = input("Enter the name of the side you are looking for")
                        while côtéquoncherche1 != "AC" and côtéquoncherche1 != "BC":
                            print("Incorrect entry")
                            time.sleep(1.5)
                            côtéqunocherche1 = input("Enter the name of the side you are looking for")
                        if côtéquoncherche1 == "AC":
                            angleautiliser1 = float(angleavecmesuretrig[1:])
                            longueurautiliser1 = float(côtéaveclongueurtrig[2:])
                            angleradian1 = math.radians(angleautiliser1)
                            AC1trig = math.tan(angleradian1) * longueurautiliser1
                            print("AC = ", AC1trig, "cm")
                        else:
                            if côtéquoncherche1 == "BC":
                                angleautiliser2 = float(angleavecmesuretrig[1:])
                                longueurautiliser2 = float(côtéaveclongueurtrig[2:])
                                angleradian2 = math.radians(angleautiliser2)
                                BC1trig = longueurautiliser2 / math.cos(angleradian2)
                                print("BC = ", BC1trig, "cm")
                    else:
                        if angleavecmesuretrig[0] == "C":
                            côtéquoncherche2 = input("Enter the name of the side you are looking for")
                            while côtéquoncherche2 != "AC" and côtéquoncherche2 != "BC":
                                print("Incorrect entry")
                                time.sleep(1.5)
                                côtéquoncherche2 = input("Enter the name of the side you are looking for")
                            if côtéquoncherche2 == "AC":
                                angleautiliser3 = float(angleavecmesuretrig[1:])
                                longueurautiliser3 = float(côtéaveclongueurtrig[2:])
                                angleradian3 = math.radians(angleautiliser3)
                                AC2trig = longueurautiliser3 / math.tan(angleradian3)
                                print("AC = ", AC2trig, "cm")
                            else:
                                if côtéquoncherche2 == "BC":
                                    angleautiliser4 = float(angleavecmesuretrig[1:])
                                    longueurautiliser4 = float(côtéaveclongueurtrig[2:])
                                    angleradian4 = math.radians(angleautiliser4)
                                    BC2trig = longueurautiliser4 / math.sin(angleradian4)
                                    print("BC = ", BC2trig, "cm")
                else:
                    if côtéaveclongueurtrig[:2] == "AC":
                        if angleavecmesuretrig[0] == "B":
                            côtéquoncherche3 = input("Enter the name of the side you are looking for")
                            while côtéquoncherche3 != "AB" and côtéquoncherche3 != "BC":
                                print("Incorrect entry")
                                time.sleep(1.5)
                                côtéquoncherche3 = input("Enter the name of the side you are looking for")
                            if côtéquoncherche3 == "AB":
                                angleautiliser5 = float(angleavecmesuretrig[1:])
                                longueurautiliser5 = float(côtéaveclongueurtrig[2:])
                                angleradian5 = math.radians(angleautiliser5)
                                AB1trig = longueurautiliser5 / math.tan(angleradian5)
                                print("AB : ", AB1trig, "cm")
                            else:
                                if côtéquoncherche3 == "BC":
                                    angleautiliser6 = float(angleavecmesuretrig[1:])
                                    longueurautiliser6 = float(côtéaveclongueurtrig[2:])
                                    angleradian6 = math.radians(angleautiliser6)
                                    BC3trig = longueurautiliser6 / math.sin(angleradian6)
                                    print("BC = ", BC3trig, "cm") 
                        else:
                            if angleavecmesuretrig[0] == "C":
                                côtéquoncherche4 = input("Enter the name of the side you are looking for")
                                while côtéquoncherche4 != "AB" and côtéquoncherche4 != "BC":
                                    print("Incorrect entry")
                                    time.sleep(1.5)
                                    côtéquoncherche4 = input("Enter the name of the side you are looking for")
                                if côtéquoncherche4 == "AB":
                                    angleautiliser7 = float(angleavecmesuretrig[1:])
                                    longueurautiliser7 = float(côtéaveclongueurtrig[2:])
                                    angleradian7 = math.radians(angleautiliser7)
                                    AB2trig = longueurautiliser7 * math.tan(angleradian7)
                                    print("AB = ", AB2trig, "cm")
                                else:
                                    if côtéquoncherche4 == "BC":
                                        angleautiliser8 = float(angleavecmesuretrig[1:])
                                        longueurautiliser8 = float(côtéaveclongueurtrig[2:])
                                        angleradian8 = math.radians(angleautiliser8)
                                        BC4trig = longueurautiliser8 / math.cos(angleradian8)
                                        print("BC = ", BC4trig, "cm")
                    else:
                        if côtéaveclongueurtrig[:2] == "BC":
                            if angleavecmesuretrig[0] == "B":
                                côtéquoncherche5 = input("Enter the name of the side you are looking for")
                                while côtéquoncherche5 != "AB" and côtéquoncherche5 != "AC":
                                    print("Incorrect entry")
                                    time.sleep(1.5)
                                    côtéquoncherche5 = input("Enter the name of the side you are looking for")
                                if côtéquoncherche5 == "AB":
                                    angleautiliser9 = float(angleavecmesuretrig[1:])
                                    longueurautiliser9 = float(côtéaveclongueurtrig[2:])
                                    angleradian9 = math.radians(angleautiliser9)
                                    AB3trig = longueurautiliser9 * math.cos(angleradian9)
                                    print("AB = ", AB3trig, "cm")
                                else:
                                    if côtéquoncherche5 == "AC":
                                        angleautiliser10 = float(angleavecmesuretrig[1:])
                                        longueurautiliser10 = float(côtéaveclongueurtrig[2:])
                                        angleradian10 = math.radians(angleautiliser10)
                                        AC3trig = math.sin(angleradian10) * longueurautiliser10
                                        print("AC = ", AC3trig, "cm")
                            else:
                                if angleavecmesuretrig[0] == "C":
                                    côtéquoncherche6 = input("Enter the name of the side you are looking for")
                                    while côtéquoncherche6 != "AB" and côtéquoncherche6 != "AC":
                                        print("Incorrect entry")
                                        time.sleep(1.5)
                                        côtéquoncherche6 = input("Enter the name of the side you are looking for")
                                    if côtéquoncherche6 == "AB":
                                        angleautiliser11 = float(angleavecmesuretrig[1:])
                                        longueurautiliser11 = float(côtéaveclongueurtrig[2:])
                                        angleradian11 = math.radians(angleautiliser11)
                                        AB4trig = math.sin(angleradian11) * longueurautiliser11
                                        print("AB = ", AB4trig, "cm")
                                    else:
                                        if côtéquoncherche6 == "AC":
                                            angleautiliser12 = float(angleavecmesuretrig[1:])
                                            longueurautiliser12 = float(côtéaveclongueurtrig[2:])
                                            angleradian12 = math.radians(angleautiliser12)
                                            AC4trig = math.cos(angleradian12) * longueurautiliser12
                                            print("AC = ", AC4trig, "cm")
            else:
                if angledroittrig == "B":
                    if côtéaveclongueurtrig[:2] == "AB":
                        if angleavecmesuretrig[0] == "A":
                            côtéquoncherche7 = input("Enter the name of the side you are looking for")
                            while côtéquoncherche7 != "AC" and côtéquoncherche7 != "BC":
                                print("Incorrect entry")
                                time.sleep(1.5)
                                côtéquoncherche7 = input("Enter the name of the side you are looking for")
                            if côtéquoncherche7 == "AC":
                                angleautiliser13 = float(angleavecmesuretrig[1:])
                                longueurautiliser13 = float(côtéaveclongueurtrig[2:])
                                angleradian13 = math.radians(angleautiliser13)
                                AC5trig = longueurautiliser13 / math.cos(angleradian13)
                                print("AC = ", AC5trig, 'cm')
                            else:
                                if côtéquoncherche7 == "BC":
                                    angleautiliser14 = float(angleavecmesuretrig[1:])
                                    longueurautiliser14 = float(côtéaveclongueurtrig[2:])
                                    angleradian14 = math.radians(angleautiliser14)
                                    BC5trig = math.tan(angleradian14) * longueurautiliser14
                                    print("BC = ", BC5trig, "cm")
                        else:
                            if angleavecmesuretrig[0] == "C":
                                côtéquoncherche8 = input("Enter the name of the side you are looking for")
                                while côtéquoncherche8 != "AC" and côtéquoncherche8 != "BC":
                                    print("Incorrect entry")
                                    time.sleep(1.5)
                                    côtéquoncherche8 = input("Enter the name of the side you are looking for")
                                if côtéquoncherche8 == "AC":
                                    angleautiliser15 = float(angleavecmesuretrig[1:])
                                    longueurautiliser15 = float(côtéaveclongueurtrig[2:])
                                    angleradian15 = math.radians(angleautiliser15)
                                    AC6trig = longueurautiliser15 / math.sin(angleradian15)
                                    print("AC = ", AC6trig, "cm")
                                else:
                                    if côtéquoncherche8 == "BC":
                                        angleautiliser16 = float(angleavecmesuretrig[1:])
                                        longueurautiliser16 = float(côtéaveclongueurtrig[2:])
                                        angleradian16 = math.radians(angleautiliser16)
                                        BC6trig = longueurautiliser16 / math.tan(angleradian16)
                                        print("BC = ", BC6trig, "cm")
                    else:
                        if côtéaveclongueurtrig[:2] == "AC":
                            if angleavecmesuretrig[0] == "A":
                                côtéquoncherche9 = input("Enter the name of the side you are looking for")
                                while côtéquoncherche9 != "AB" and côtéquoncherche9 != "BC":
                                    print("Incorrect entry")
                                    time.sleep(1.5)
                                    côtéquoncherche9 = input("Enter the name of the side you are looking for")
                                if côtéquoncherche9 == "AB":
                                    angleautiliser17 = float(angleavecmesuretrig[1:])
                                    longueurautiliser17 = float(côtéaveclongueurtrig[2:])
                                    angleradian17 = math.radians(angleautiliser17)
                                    AB5trig = longueurautiliser17 * math.cos(angleradian17)
                                    print("AB = ", AB5trig, "cm")
                                else:
                                    if côtéquoncherche9 == "BC":
                                        angleautiliser18 = float(angleavecmesuretrig[1:])
                                        longueurautiliser18 = float(côtéaveclongueurtrig[2:])
                                        angleradian18 = math.radians(angleautiliser18)
                                        BC6trig = longueurautiliser18 * math.sin(angleradian18)
                                        print("BC = ", BC6trig, "cm")
                            else:
                                if angleavecmesuretrig[0] == "C":
                                    côtéquoncherche10 = input("Enter the name of the side you are looking for")
                                    while côtéquoncherche10 != "AB" and côtéquoncherche10 != "BC":
                                        print("Incorrect entry")
                                        time.sleep(1.5)
                                        côtéquoncherche10 = input("Enter the name of the side you are looking for")
                                    if côtéquoncherche10 == "AB":
                                        angleautiliser19 = float(angleavecmesuretrig[1:])
                                        longueurautiliser19 = float(côtéaveclongueurtrig[2:])
                                        angleradian19 = math.radians(angleautiliser19)
                                        AB6trig = longueurautiliser19 * math.sin(angleradian19)
                                        print("AB = ", AB6trig, "cm")
                                    else:
                                        if côtéquoncherche10 == "BC":
                                            angleautiliser20 = float(angleavecmesuretrig[1:])
                                            longueurautiliser20 = float(côtéaveclongueurtrig[2:])
                                            angleradian20 = math.radians(angleautiliser20)
                                            BC7trig = longueurautiliser20 * math.cos(angleradian20)
                                            print("BC = ", BC7trig, "cm")
                        else:
                            if côtéaveclongueurtrig[:2] == "BC":
                                if angleavecmesuretrig[0] == "A":
                                    côtéquoncherche11 = input("Enter the name of the side you are looking for")
                                    while côtéquoncherche11 != "AB" and côtéquoncherche11 != "AC":
                                        print("Incorrect entry")
                                        time.sleep(1.5)
                                        côtéquoncherche11 = input("Enter the name of the side you are looking for")
                                    if côtéquoncherche11 == "AB":
                                        angleautiliser21 = float(angleavecmesuretrig[1:])
                                        longueurautiliser21 = float(côtéaveclongueurtrig[2:])
                                        angleradian21 = math.radians(angleautiliser21)
                                        AB7trig = longueurautiliser21 / math.tan(angleradian21)
                                        print("AB = ", AB7trig, "cm")
                                    else:
                                        if côtéquoncherche11 == "AC":
                                            angleautiliser22 = float(angleavecmesuretrig[1:])
                                            longueurautiliser22 = float(côtéaveclongueurtrig[2:])
                                            angleradian22 = math.radians(angleautiliser22)
                                            AC7trig = longueurautiliser22 / math.sin(angleradian22)
                                            print("AC = ", AC7trig, "cm")
                                else:
                                    if angleavecmesuretrig[0] == "C":
                                        côtéquoncherche12 = input("Enter the name of the side you are looking for")
                                        while côtéquoncherche12 != "AB" and côtéquoncherche12 != "AC":
                                            print("Incorrect entry")
                                            time.sleep(1.5)
                                            côtéquoncherche12 = input("Enter the name of the side you are looking for")
                                        if côtéquoncherche12 == "AB":
                                            angleautiliser23 = float(angleavecmesuretrig[1:])
                                            longueurautiliser23 = float(côtéaveclongueurtrig[2:])
                                            angleradian23 = math.radians(angleautiliser23)
                                            AB8trig = longueurautiliser23 * math.tan(angleradian23)
                                            print("AB = ", AB8trig, "cm")
                                        else:
                                            if côtéquoncherche12 == "AC":
                                                angleautiliser24 = float(angleavecmesuretrig[1:])
                                                longueurautiliser24 = float(côtéaveclongueurtrig[2:])
                                                angleradian24 = math.radians(angleautiliser24)
                                                AC8trig = longueurautiliser24 / math.cos(angleradian24)
                                                print("AC = ", AC8trig, "cm")
                else:
                    if angledroittrig == "C":
                        if côtéaveclongueurtrig[:2] == "AB":
                            if angleavecmesuretrig[0] == "A":
                                côtéquoncherche13 = input("Enter the name of the side you are looking for")
                                while côtéquoncherche13 != "AC" and côtéquoncherche13 != "BC":
                                    print("Incorrect entry")
                                    time.sleep(1.5)
                                    côtéquoncherche13 = input("Enter the name of the side you are looking for")
                                if côtéquoncherche13 == "AC":
                                    angleautiliser25 = float(angleavecmesuretrig[1:])
                                    longueurautiliser25 = float(côtéaveclongueurtrig[2:])
                                    angleradian25 = math.radians(angleautiliser25)
                                    AC9trig = longueurautiliser25 * math.cos(angleradian25)
                                    print("AC = ", AC9trig, "cm")
                                else:
                                    if côtéquoncherche13 == "BC":
                                        angleautiliser26 = float(angleavecmesuretrig[1:])
                                        longueurautiliser26 = float(côtéaveclongueurtrig[2:])
                                        angleradian26 = math.radians(angleautiliser26)
                                        BC8trig = longueurautiliser26 * math.sin(angleradian26)
                                        print("BC = ", BC8trig, "cm")
                            else:
                                if angleavecmesuretrig[0] == "B":
                                    côtéquoncherche14 = input("Enter the name of the side you are looking for")
                                    while côtéquoncherche14 != "AC" and côtéquoncherche14 != "BC":
                                        print("Incorrect entry")
                                        time.sleep(1.5)
                                        côtéquoncherche14 = input("Enter the name of the side you are looking for")
                                    if côtéquoncherche14 == "AC":
                                        angleautiliser27 = float(angleavecmesuretrig[1:])
                                        longueurautiliser27 = float(côtéaveclongueurtrig[2:])
                                        angleradian27 = math.radians(angleautiliser27)
                                        AC10trig = longueurautiliser27 * math.sin(angleradian27)
                                        print("AC = ", AC10trig, "cm")
                                    else:
                                        if côtéquoncherche14 == "BC":
                                            angleautiliser28 = float(angleavecmesuretrig[1:])
                                            longueurautiliser28 = float(côtéaveclongueurtrig[2:])
                                            angleradian28 = math.radians(angleautiliser28)
                                            BC9trig = longueurautiliser28 * math.cos(angleradian28)
                                            print("BC = ", BC9trig, "cm")
                        else:
                            if côtéaveclongueurtrig[:2] == "AC":
                                if angleavecmesuretrig[0] == "A":
                                    côtéquoncherche15 = input("Enter the name of the side you are looking for")
                                    while côtéquoncherche15 != "AB" and côtéquoncherche15 != "BC":
                                        print("Incorrect entry")
                                        time.sleep(1.5)
                                        côtéquoncherche15 = input("Enter the name of the side you are looking for") 
                                    if côtéquoncherche15 == "AB":
                                        angleautiliser29 = float(angleavecmesuretrig[1:])
                                        longueurautiliser29 = float(côtéaveclongueurtrig[2:])
                                        angleradian29 = math.radians(angleautiliser29)
                                        AB9trig = longueurautiliser29 / math.cos(angleradian29)
                                        print("AB = ", AB9trig, "cm")
                                    else:
                                        if côtéquoncherche15 == "BC":
                                            angleautiliser30 = float(angleavecmesuretrig[1:])
                                            longueurautiliser30 = float(côtéaveclongueurtrig[2:])
                                            angleradian30 = math.radians(angleautiliser30)
                                            BC10trig = longueurautiliser30 * math.tan(angleradian30)
                                            print("BC = ", BC10trig, "cm")
                                else:
                                    if angleavecmesuretrig[0] == "B":
                                        côtéquoncherche16 = input("Enter the name of the side you are looking for")
                                        while côtéquoncherche16 != "AB" and côtéquoncherche16 != "BC":
                                            print("Incorrect entry")
                                            time.sleep(1.5)
                                            côtéquoncherche16 = input("Enter the name of the side you are looking for")
                                        if côtéquoncherche16 == "AB":
                                            angleautiliser31 = float(angleavecmesuretrig[1:])
                                            longueurautiliser31 = float(côtéaveclongueurtrig[2:])
                                            angleradian31 = math.radians(angleautiliser31)
                                            AB10trig = longueurautiliser31 / math.sin(angleradian31)
                                            print("AB = ", AB10trig, "cm")
                                        else:
                                            if côtéquoncherche16 == "BC":
                                                angleautiliser32 = float(angleavecmesuretrig[1:])
                                                longueurautiliser32 = float(côtéaveclongueurtrig[2:])
                                                angleradian32 = math.radians(angleautiliser32)
                                                BC11trig = longueurautiliser32 / math.tan(angleradian32)
                                                print("BC = ", BC11trig, "cm")
                            else:
                                if côtéaveclongueurtrig[:2] == "BC":
                                    if angleavecmesuretrig[0] == "A":
                                        côtéquoncherche17 = input("Enter the name of the side you are looking for")
                                        while côtéquoncherche17 != "AB":
                                            print("Incorrect entry")
                                            time.sleep(1.5)
                                            côtéquoncherche17 = input("Enter the name of the side you are looking for")
                                        if côtéquoncherche17 == "AB":
                                            angleautiliser33 = float(angleavecmesuretrig[1:])
                                            longueurautiliser33 = float(côtéaveclongueurtrig[2:])
                                            angleradian33 = math.radians(angleautiliser33)
                                            AB11trig = longueurautiliser33 / math.sin(angleradian33)
                                            print("AB = ", AB11trig, "cm")
                                        else:
                                            if côtéquoncherche17 == "AC":
                                                angleautiliser34 = float(angleavecmesuretrig[1:])
                                                longueurautiliser34 = float(côtéaveclongueurtrig[2:])
                                                angleradian34 = math.radians(angleautiliser34)
                                                AC11trig = longueurautiliser34 / math.tan(angleradian34)
                                                print("AC = ", AC11trig, "cm")
                                    else:
                                        if angleavecmesuretrig[0] == "B":
                                            côtéquoncherche18 = input("Enter the name of the side you are looking for")
                                            while côtéquoncherche18 != "AB" and côtéquoncherche18 != "AC":
                                                print("Incorrect entry")
                                                time.sleep(1.5)
                                                côtéquoncherche18 = input("Enter the name of the side you are looking for")
                                            if côtéquoncherche18 == "AB":
                                                angleautiliser35 = float(angleavecmesuretrig[1:])
                                                longueurautiliser35 = float(côtéaveclongueurtrig[2:])
                                                angleradian35 = math.radians(angleautiliser35)
                                                AB12trig = longueurautiliser35 / math.cos(angleradian35)
                                                print("AB = ", AB12trig, "cm")
                                            else:
                                                if côtéquoncherche18 == "AC":
                                                    angleautiliser36 = float(angleavecmesuretrig[1:])
                                                    longueurautiliser36 = float(côtéaveclongueurtrig[2:])
                                                    angleradian36 = math.radians(angleautiliser36)
                                                    AC12trig = longueurautiliser36 * math.tan(angleradian36)
                                                    print("AC = ", AC12trig, "cm")
        else:
            if actiontrig == "2": #lines 681 to 918 = the function find the measure of an angle with asin, acos and atan
                angledroittrigangle = input("Enter the right angle of the triangle")
                while angledroittrigangle != "A" and angledroittrigangle != "B" and angledroittrigangle != "C":
                    print("Incorrect entry")
                    time.sleep(1.5)
                    angledroittrigangle = input("Enter the right angle of the triangle")
                côtéquona1 = input("Enter the name of the first side you have (first its name, then its length in cm)")
                while côtéquona1[:2] != "AB" and côtéquona1[:2] != "AC" and côtéquona1[:2] != "BC":
                    print("Incorrect entry")
                    time.sleep(1.5)
                    côtéquona1 = input("Enter the name of the first side you have (first its name, then its length in cm)")
                while True:
                    try:
                        float(côtéquona1[2:])
                        break
                    except ValueError:
                        print("Incorrect entry")
                        time.sleep(1.5)
                        côtéquona1 = input("Enter the name of the first side you have (first its name, then its length in cm)")
                côtéquona2 = input("Enter the name of the second side you have (first its name, then its length in cm)")
                while côtéquona2[:2] != "AB" and côtéquona2[:2] != "AC" and côtéquona2[:2] != "BC":
                    print("Incorrect entry")
                    time.sleep(1.5)
                    côtéquona2 = input("Enter the name of the second side you have (first its name, then its length in cm)")
                while True:
                    try:
                        float(côtéquona2[2:])
                        break
                    except ValueError:
                        print("Incorrect entry")
                        time.sleep(1.5)
                        côtéquona2 = input("Enter the name of the second side you have (first its name, then its length in cm)")
                anglequoncherche = input("Enter the name of the angle you are looking for")
                while anglequoncherche != "A" and anglequoncherche != "B" and anglequoncherche != "C":
                    print("Incorrect entry")
                    time.sleep(1.5)
                    anglequoncherche = input("Enter the name of the angle you are looking for")
                côtéquonamesure1 = float(côtéquona1[2:])
                côtéquonamesure2 = float(côtéquona2[2:])
                if angledroittrigangle == "A":
                    if côtéquona1[:2] == "AB" and côtéquona2[:2] == "AC":
                        if anglequoncherche == "B":
                            angletrouvé1 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                            angletrouvé1degré = math.degrees(angletrouvé1)
                            print("The angle B = ", angletrouvé1degré, "°")
                        else:
                            if anglequoncherche == "C":
                                angletrouvé2 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                                angletrouvé2degré = math.degrees(angletrouvé2)
                                print("The angle C = ", angletrouvé2degré, "°")
                    else:
                        if côtéquona1[:2] == "AB" and côtéquona2[:2] == "BC":
                            if anglequoncherche == "B":
                                angletrouvé3 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                                angletrouvé3degré = math.degrees(angletrouvé3)
                                print("The angle B = ", angletrouvé3degré, "°")
                            else:
                                if anglequoncherche == "C":
                                    angletrouvé4 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                                    angletrouvé4degré = math.degrees(angletrouvé4)
                                    print("The angle C =", angletrouvé4degré, "°")
                        else:
                            if côtéquona1[:2] == "AC" and côtéquona2[:2] == "BC":
                                if anglequoncherche == "B":
                                    angletrouvé5 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                                    angletrouvé5degré = math.degrees(angletrouvé5)
                                    print("The angle B =", angletrouvé5degré, "°")
                                else:
                                    if anglequoncherche == "C":
                                        angletrouvé6 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                                        angletrouvé6degré = math.degrees(angletrouvé6)
                                        print("The angle C =", angletrouvé6degré, "°")
                            else:
                                if côtéquona1[:2] == "AC" and côtéquona2[:2] == "AB":
                                    if anglequoncherche == "B":
                                        angletrouvé7 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                                        angletrouvé7degré = math.degrees(angletrouvé7)
                                        print("The angle B = ", angletrouvé7degré, "°")
                                    else:
                                        if anglequoncherche == "C":
                                            angletrouvé8 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                                            angletrouvé8degré = math.degrees(angletrouvé8)
                                            print("The angle C = ", angletrouvé8degré, "°")
                                else:
                                    if côtéquona1[:2] == "BC" and côtéquona2[:2] == "AB":
                                        if anglequoncherche == "B":
                                            angletrouvé9 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                                            angletrouvé9degré = math.degrees(angletrouvé9)
                                            print("The angle B = ", angletrouvé9degré, "°")
                                        else:
                                            if anglequoncherche == "C":
                                                angletrouvé10 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                                                angletrouvé10degré = math.degrees(angletrouvé10)
                                                print("The angle C =", angletrouvé10degré, "°")
                                    else:
                                        if côtéquona1[:2] == "BC" and côtéquona2[:2] == "AC":
                                            if anglequoncherche == "B":
                                                angletrouvé11 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                                                angletrouvé11degré = math.degrees(angletrouvé11)
                                                print("The angle B =", angletrouvé11degré, "°")
                                            else:
                                                if anglequoncherche == "C":
                                                    angletrouvé12 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                                                    angletrouvé12degré = math.degrees(angletrouvé12)
                                                    print("The angle C =", angletrouvé12degré, "°")
                else:
                    if angledroittrigangle == "B":
                        if côtéquona1[:2] == "AB" and côtéquona2[:2] == "AC":
                            if anglequoncherche == "A":
                                angletrouvé13 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                                angletrouvé13degré = math.degrees(angletrouvé13)
                                print("The angle A = ", angletrouvé13degré, "°")
                            else:
                                if anglequoncherche == "C":
                                    angletrouvé14 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                                    angletrouvé14degré = math.degrees(angletrouvé14)
                                    print("The angle C = ", angletrouvé14degré, "°")
                        else:
                            if côtéquona1[:2] == "AB" and côtéquona2[:2] == "BC":
                                if anglequoncherche == "A":
                                    angletrouvé15 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                                    angletrouvé15degré = math.degrees(angletrouvé15)
                                    print("The angle A = ", angletrouvé15degré, "°")
                                else:
                                    if anglequoncherche == "C":
                                        angletrouvé16 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                                        angletrouvé16degré = math.degrees(angletrouvé16)
                                        print("The angle C =", angletrouvé16degré, "°")
                            else:
                                if côtéquona1[:2] == "AC" and côtéquona2[:2] == "BC":
                                    if anglequoncherche == "A":
                                        angletrouvé17 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                                        angletrouvé17degré = math.degrees(angletrouvé17)
                                        print("The angle A =", angletrouvé17degré, "°")
                                    else:
                                        if anglequoncherche == "C":
                                            angletrouvé18 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                                            angletrouvé18degré = math.degrees(angletrouvé18)
                                            print("The angle C =", angletrouvé18degré, "°")
                                else:
                                    if côtéquona1[:2] == "AC" and côtéquona2[:2] == "AB":
                                        if anglequoncherche == "A":
                                            angletrouvé19 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                                            angletrouvé19degré = math.degrees(angletrouvé19)
                                            print("The angle A = ", angletrouvé19degré, "°")
                                        else:
                                            if anglequoncherche == "C":
                                                angletrouvé20 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                                                angletrouvé20degré = math.degrees(angletrouvé20)
                                                print("The angle C = ", angletrouvé20degré, "°")
                                    else:
                                        if côtéquona1[:2] == "BC" and côtéquona2[:2] == "AB":
                                            if anglequoncherche == "A":
                                                angletrouvé21 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                                                angletrouvé21degré = math.degrees(angletrouvé21)
                                                print("The angle A = ", angletrouvé21degré, "°")
                                            else:
                                                if anglequoncherche == "C":
                                                    angletrouvé22 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                                                    angletrouvé22degré = math.degrees(angletrouvé22)
                                                    print("The angle C =", angletrouvé22degré, "°")
                                        else:
                                            if côtéquona1[:2] == "BC" and côtéquona2[:2] == "AC":
                                                if anglequoncherche == "A":
                                                    angletrouvé23 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                                                    angletrouvé23degré = math.degrees(angletrouvé23)
                                                    print("The angle A =", angletrouvé23degré, "°")
                                                else:
                                                    if anglequoncherche == "C":
                                                        angletrouvé24 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                                                        angletrouvé24degré = math.degrees(angletrouvé24)
                                                        print("The angle C =", angletrouvé24degré, "°")
                    else:
                        if angledroittrigangle == "C":
                            if côtéquona1[:2] == "AB" and côtéquona2[:2] == "AC":
                                if anglequoncherche == "A":
                                    angletrouvé25 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                                    angletrouvé25degré = math.degrees(angletrouvé25)
                                    print("The angle A = ", angletrouvé25degré, "°")
                                else:
                                    if anglequoncherche == "B":
                                        angletrouvé26 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                                        angletrouvé26degré = math.degrees(angletrouvé26)
                                        print("The angle B = ", angletrouvé26degré, "°")
                            else:
                                if côtéquona1[:2] == "AB" and côtéquona2[:2] == "BC":
                                    if anglequoncherche == "A":
                                        angletrouvé27 = math.asin(côtéquonamesure2 / côtéquonamesure1)
                                        angletrouvé27degré = math.degrees(angletrouvé27)
                                        print("The angle A = ", angletrouvé27degré, "°")
                                    else:
                                        if anglequoncherche == "B":
                                            angletrouvé28 = math.acos(côtéquonamesure2 / côtéquonamesure1)
                                            angletrouvé28degré = math.degrees(angletrouvé28)
                                            print("The angle B =", angletrouvé28degré, "°")
                                else:
                                    if côtéquona1[:2] == "AC" and côtéquona2[:2] == "BC":
                                        if anglequoncherche == "A":
                                            angletrouvé29 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                                            angletrouvé29degré = math.degrees(angletrouvé29)
                                            print("The angle A =", angletrouvé29degré, "°")
                                        else:
                                            if anglequoncherche == "B":
                                                angletrouvé30 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                                                angletrouvé30degré = math.degrees(angletrouvé30)
                                                print("The angle B =", angletrouvé30degré, "°")
                                    else:
                                        if côtéquona1[:2] == "AC" and côtéquona2[:2] == "AB":
                                            if anglequoncherche == "A":
                                                angletrouvé31 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                                                angletrouvé31degré = math.degrees(angletrouvé31)
                                                print("The angle A = ", angletrouvé31degré, "°")
                                            else:
                                                if anglequoncherche == "B":
                                                    angletrouvé32 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                                                    angletrouvé32degré = math.degrees(angletrouvé32)
                                                    print("The angle B = ", angletrouvé32degré, "°")
                                        else:
                                            if côtéquona1[:2] == "BC" and côtéquona2[:2] == "AB":
                                                if anglequoncherche == "A":
                                                    angletrouvé33 = math.asin(côtéquonamesure1 / côtéquonamesure2)
                                                    angletrouvé33degré = math.degrees(angletrouvé33)
                                                    print("The angle A = ", angletrouvé33degré, "°")
                                                else:
                                                    if anglequoncherche == "B":
                                                        angletrouvé34 = math.acos(côtéquonamesure1 / côtéquonamesure2)
                                                        angletrouvé34degré = math.degrees(angletrouvé34)
                                                        print("The angle B =", angletrouvé34degré, "°")
                                            else:
                                                if côtéquona1[:2] == "BC" and côtéquona2[:2] == "AC":
                                                    if anglequoncherche == "A":
                                                        angletrouvé35 = math.atan(côtéquonamesure1 / côtéquonamesure2)
                                                        angletrouvé35degré = math.degrees(angletrouvé35)
                                                        print("The angle A =", angletrouvé35degré, "°")
                                                    else:
                                                        if anglequoncherche == "B":
                                                            angletrouvé36 = math.atan(côtéquonamesure2 / côtéquonamesure1)
                                                            angletrouvé36degré = math.degrees(angletrouvé36)
                                                            print("The angle B =", angletrouvé36degré, "°")  
            else:
                if actiontrig == "3":
                    print("Bye !")
                    time.sleep(1.5)
                    break
def quitter(): #we define "quit"
    print("Thank you for using MathRobot!")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()

print("Bonjour")
time.sleep(0.5)
print("JI'm MathRobot, I do a lot of math stuff")
time.sleep(0.5)
while True:
    quoifaire = input("Enter the number of what you want me to do:\n1. Pythagoras\n2. Trigonometry\n3. Quit MathRobot\n") #we ask the robot what to do
    while quoifaire != "1" and quoifaire != "2" and quoifaire != "3":
        print("Incorrect entry")
        time.sleep(1.5)
        quoifaire = input("Enter the number of what you want me to do:\n1. Pythagoras\n2. Trigonometry\n3. Quit MathRobot\n")
    if quoifaire == "1":
        pythagore()
    else:
        if quoifaire == "2":
            trigonométrie()
        else:
            if quoifaire == "3":
                quitter()
#END