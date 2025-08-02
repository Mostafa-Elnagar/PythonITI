class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate
    
    def sleep(self, hours):
        """Sleep method: 7 hours → happy, <7 hours → tired, >7 hours → Lazy"""
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:  # hours > 7
            self.mood = "Lazy"
        print(f"{self.name} slept for {hours} hours and is now {self.mood}")
    
    def eat(self, meals):
        """Eat method: 3 meals → 100% health, 2 meals → 75%, 1 meal → 50%"""
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
        else:
            print("Invalid number of meals")
            return
        print(f"{self.name} ate {meals} meals and health rate is now {self.healthRate}%")
    
    def buy(self, items):
        """Buy method: 1 item → decrease money 10L.E"""
        cost = items * 10
        if self.money >= cost:
            self.money -= cost
            print(f"{self.name} bought {items} item(s) for {cost}L.E. Remaining money: {self.money}L.E")
        else:
            print(f"{self.name} doesn't have enough money to buy {items} item(s)")
    
    def __str__(self):
        return f"Person: {self.name}, Money: {self.money}L.E, Mood: {self.mood}, Health: {self.healthRate}%" 