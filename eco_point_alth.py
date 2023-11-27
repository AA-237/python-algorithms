class RewardsProgram:
    def __init__(self):
        self.user_points = 0

    def earn_points(self, price):
        points = round(price)  
        
        self.user_points += points
        return points

    def check_level(self):
        if self.user_points < 100:
            return "Bronze"
        elif self.user_points < 500:
            return "Silver"
        else:
            return "Gold"

    def redeem_points(self, service, base):
        if service not in ["voice", "data", "electricity"]:
            return "Invalid service"

        if self.user_points < base:
            return "Not enough points"

        self.user_points -= base
        return f"Successfully redeemed {base} points for {service}"

# Example for testing by changing values
rewards = RewardsProgram()
rewards.earn_points(250)
print(rewards.check_level())
print(rewards.redeem_points("voice", 300))

