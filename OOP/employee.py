from person import Person

class Employee(Person):
    def __init__(self, id, name, money, mood, healthRate, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
    
    def work(self, hours):
        """Work method: 8 hours → happy, >8 hours → tired, <8 hours → Lazy"""
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:  # hours < 8
            self.mood = "Lazy"
        print(f"{self.name} worked for {hours} hours and is now {self.mood}")
    
    def drive(self, distance):
        """Drive method: gives order to car's run method with distance and velocity"""
        if self.car:
            velocity = min(distance, 200)  # Cap at max velocity
            self.car.run(velocity, distance)
        else:
            print(f"{self.name} doesn't have a car to drive")
    
    def refuel(self, gasAmount=100):
        """Refuel method: adds gasAmount to fuelRate"""
        if self.car:
            old_fuel = self.car.fuelRate
            self.car.fuelRate += gasAmount
            print(f"{self.name} refueled {self.car.name} from {old_fuel}% to {self.car.fuelRate}%")
        else:
            print(f"{self.name} doesn't have a car to refuel")
    
    def send_mail(self, to_email, subject, body):
        """Send mail method"""
        print(f"Email sent from {self.email} to {to_email}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
    
    def __str__(self):
        car_info = f", Car: {self.car.name}" if self.car else ", No car"
        return f"Employee ID: {self.id}, Name: {self.name}, Email: {self.email}, Salary: {self.salary}L.E{car_info}" 