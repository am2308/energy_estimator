#!/usr/bin/python3
import sys
import logging
import re

##This function will calculate the energy estimate

class EnergyCalculator:
    def EnergyCalculator(self,UniqueConsumption):
        LedUsage = 0
        LedUsageFull = 5
        logging.info("Removing duplicate and random entries")
        for i in range(0,len(UniqueConsumption)):
            if "TurnOff" not in UniqueConsumption[i]:
                TimeTaken = (int(UniqueConsumption[i+1].split(' ')[0]) - int(UniqueConsumption[i].split(' ')[0]))/3600
                if UniqueConsumption[i].split(' ')[2].startswith('+'):
                    if i == 1:
                        LedUsage = LedUsage + 5 * float(UniqueConsumption[i].split(' ')[2].split('+')[1]) * TimeTaken
                    else:
                        OldEneryUnits = abs(float(re.split(r'[+-]', UniqueConsumption[i-1].split(' ')[2])[1]))
                        EnergyUnitDiffOverTime = float(UniqueConsumption[i].split(' ')[2].split('+')[1]) + OldEneryUnits
                        LedUsage = LedUsage + 5 * EnergyUnitDiffOverTime * TimeTaken
                elif UniqueConsumption[i].split(' ')[2].startswith('-'):
                    OldEneryUnits = float(re.split(r'[+-]', UniqueConsumption[i-1].split(' ')[2])[1])
                    EnergyUnitDiffOverTime = abs(float(UniqueConsumption[i].split(' ')[2].split('-')[1]) - OldEneryUnits)
                    LedUsage = LedUsage + 5 * EnergyUnitDiffOverTime * TimeTaken

        return LedUsage

    ##This function will remove the duplicate entries from consumption massages along with sort them
    def DuplicacyRandonHandler(self,EnergyConsumption):
        logging.info("Removing duplicate and random entries")
        EnergyConsumption = sorted(EnergyConsumption)
        UniqueConsumption = []
        #This will remove new line characters and also will remove duplicates
        [UniqueConsumption.append(x.rstrip()) for x in EnergyConsumption if x.rstrip() not in UniqueConsumption]
        return UniqueConsumption

    ##This function will take the user input as consumption messages  
    def InputEnergyUsage(self):
        logging.info("Please input your energy consumption!")
        print("Please input your energy consumption!, Once input provided press ctrl+d to log the input")
        EnergyConsumption = sys.stdin.readlines()

        return EnergyConsumption

def main():
    calculator = EnergyCalculator()
    logging.info("Welcome to Energy Estimater Tool!")
    print("Welcome to Energy Estimater Tool!")
    EnergyConsumption = calculator.InputEnergyUsage()
    UniqueConsumption = calculator.DuplicacyRandonHandler(EnergyConsumption)
    LedUsage = calculator.EnergyCalculator(UniqueConsumption)
    logging.info("Your energy consumption has beem calculated!")
    print("Your energy consumption has beem calculated as " + str(LedUsage) + " " + "Wh")

if __name__ == "__main__":
  main()
