class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self._fuelRate = 0
        self._velocity = 0
        self.fuelRate = fuelRate 
        self.velocity = velocity 
    
    @property
    def fuelRate(self):
        return self._fuelRate
    
    @fuelRate.setter
    def fuelRate(self, value):
        if 0 <= value <= 100:
            self._fuelRate = value
        else:
            print(f"Fuel rate must be between 0 and 100. Setting to closest valid value.")
            self._fuelRate = max(0, min(100, value))
    
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            print(f"Velocity must be between 0 and 200. Setting to closest valid value.")
            self._velocity = max(0, min(200, value))
    
    def run(self, velocity, distance):
        """Run method: decreases fuelRate and changes velocity, invokes stop with remaining distance"""
        self.velocity = velocity
        fuel_consumption = distance / 10  # Assume 1 fuel unit per 10 distance units
        
        if fuel_consumption <= self.fuelRate:
            # Can complete the journey
            self.fuelRate -= fuel_consumption
            remaining_distance = 0
        else:
            # Cannot complete the journey
            actual_distance = self.fuelRate * 10
            self.fuelRate = 0
            remaining_distance = distance - actual_distance
        
        print(f"{self.name} is running at {self.velocity} km/h")
        self.stop(remaining_distance)
    
    def stop(self, remaining_distance=0):
        """Stop method: sets velocity to 0 and prints notification"""
        self.velocity = 0
        if remaining_distance == 0:
            print(f"{self.name} has stopped. Destination reached!")
        else:
            print(f"{self.name} has stopped. Remaining distance: {remaining_distance} km (fuel ran out)")
    
    def __str__(self):
        return f"Car: {self.name}, Fuel: {self.fuelRate}%, Velocity: {self.velocity} km/h" 