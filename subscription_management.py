class Users:
    def __init__(self, name, email, location):
        self.name = name
        self.email = email
        self.location = location
        self.subscription = None
        
        
class Subscriptions:
    def __init__(self, name, description, days,):
        self.name = name
        self.description = description
        self.days = days
        self.default_day = "Tuesday" # setting default day for all subscriptions 
        self.next = None
        
    def occuring_days_in_month(self):
        return self.days * 4 # with assumption that a month has 4 weeks
    
    # def __str__(self):
    #     return f"{self.name} - {self.description}, {self.days} day(s) per week"

        
class SubscriptionLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_subscription(self, subscription):
        if not self.head:
            self.head = subscription
            self.tail = subscription
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = subscription   
            
# function to get userinput and choice of subscription

def get_user_input():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    location = input("Enter your location: ")
    # return name, email, location
    
    # display subcription options
    print("Please select your subscription: ")
    print("1. Silver - One assigned day in a week")
    print("2. Gold - One assigned day and one user choice")
    print("3. Premium - One assigned day and two user choices")
    
    #Get user subscription choice
    subscription_choice = int(input("Enter your subscription choice number: "))
    
    # get user choice of days
    if subscription_choice == 2:
        user_choice_days = input("Enter the day of your choice: ")
    elif subscription_choice == 3:
        user_choice_days = input("Enter the days of your choice (comma-separated): ").split(",")    
    else:
        user_choice_days = []
        
    return Users(name, email,location), subscription_choice, user_choice_days

# assign subscription to user and display message

def assign_subscription(user, subscription, user_choice_days):
    user.subscription = subscription
    
    print(f"Selected {subscription.name} subscription")
    print(f"Your assigned day is {user_choice_days[0]  if user_choice_days else subscription.default_day}.")
    
    if user.subscription.days > 1:
        print(f"Please choose another day(s) of your choice")
        
    for i in range(1, len(user_choice_days)):
        print(f"Additional choice{i + 1}: {user_choice_days[i]}")
        
    print("Subscription details: ")
    print(f"Name: {user.name}")
    print(f"Email: {user.email}")
    print(f"Location: {user.location}")
    print('\n\n\n')
    print(f"Subscription: {user.subscription.name}")
    print(f"Subscription description: {user.subscription.description}")
    print('\n\n\n')
    print(f"Subscription day(s): {', '.join(user_choice_days) if user_choice_days else subscription.default_day}")  
    print(f"Number of times a subscription will be done in a month: {user.subscription.occuring_days_in_month}")

    
print(SubscriptionLinkedList)    
# Example usage:
subscription_list = SubscriptionLinkedList()
subscription_list.add_subscription(Subscriptions("Silver", "One assigned day in a week", 1))
subscription_list.add_subscription(Subscriptions("Gold", "One assigned day and one user choice", 2))
subscription_list.add_subscription(Subscriptions("Premium", "One assigned day and two user choices", 3))

user, subscription_choice, user_choice_days = get_user_input()
selected_subscription = subscription_list.head

for _ in range(subscription_choice - 1):
    selected_subscription = selected_subscription.next

assign_subscription(user, selected_subscription, user_choice_days)                                        




# TODO:
    # Add a prices to each subscription
    # Add a function to calculate the total number of users
    # Add a function to calculate the total number of subscriptions
    # Add a function to calculate the reduction indays after an agent has done work on agiven day of a subscription