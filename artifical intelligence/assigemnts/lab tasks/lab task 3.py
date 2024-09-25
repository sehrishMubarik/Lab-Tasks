class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.heater_status = {} 
            
    def perceive(self, room, current_temperature):
        return current_temperature
    
    def act(self, room, current_temperature):
        previous_action = self.heater_status.get(room, "Turn off heater")

        if current_temperature < self.desired_temperature:
            if previous_action != "Turn on heater":
                action = "Turn on heater"
                self.heater_status[room] = action 
            else:
                action = "Heater is already on" 
        else:
            if previous_action != "Turn off heater":
                action = "Turn off heater"
                self.heater_status[room] = action 
            else:
                action = "Heater is already off"  

        return action
rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

desired_temperature = 22
agent = ModelBasedReflexAgent(desired_temperature)
for room, temperature in rooms.items():
    action = agent.act(room, temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")
