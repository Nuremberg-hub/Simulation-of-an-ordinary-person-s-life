# РАБОТА С НЕСКОЛЬКИМИ КЛАССАМИ. РАЗРАБОТКА THE SIMS


#                   два объеденённых между собой классы которые выводять пассажиров и бренд автомобиля
# class Human:
#     def __init__(self, name="Human"):
#         self.name = name
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#     def add_passenger(self, *args):
#         for passenger in args:
#             self.passengers.append(passenger)
#     def print_passengers_names(self):
#         if self.passengers!= []:
#             print(f"Names of {self.brand} passengers:")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengers in {self.brand}")

# nick = Human("Nick")
# kate = Human("Kate")
# car = Auto("Mercedes")
# car.add_passenger(nick, kate)
# car.print_passengers_names()

# THE SIMS  
# Создание симуляций жизни человека 

import random

class Human:
    def __init__(self, name="Nika", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home        

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
        else:
            self.to_repair()

    def shopping(self, manage):
        if self.car.drive():
            if manage == "fuel":
                print("I bought fuel")
                self.money -= 100
                self.car.fuel += 100
            elif manage == "food":
                print("Bought food")
                self.money -= 50
                self.home.food += 50
            elif manage == "delicacies":
                print("Hooray! Delicious!")
                self.gladness += 10
                self.satiety += 2
                self.money -= 15
        else:
            self.to_repair()

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            print(f"{self.name} could not survive...")
            return False

        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car: {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"Got a job: {self.job.job} with salary {self.job.salary}")

        self.days_indexes(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess… So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day_info = f" Today the {day} of {self.name}'s life "
        print(f"{day_info:=^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

# Запуск симуляции
person = Human(name="Nika")
for day in range(1, 366):
    if not person.live(day):
        break
