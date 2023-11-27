def agent_performance(period, agent, requests, bookings):
    # getting  the period
    start_time, end_time = period

    #  Get all the requests related to the agent 
    agent_requests = []
    for request in requests:
        if request['agent'] == agent and start_time <= request['time'] <= end_time:
            agent_requests.append(request)

    # the number of hours for each request
    hours = 0
    for request in agent_requests:
        hours += request['hours']

    #  number of shifts
    shifts = len(set(request['shift'] for request in agent_requests))

    #  number of Bookings related to this agent
    agent_bookings = []
    for booking in bookings:
        if booking['agent'] == agent and start_time <= booking['time'] <= end_time:
            agent_bookings.append(booking)
    completed_requests = len(agent_bookings)

    punctuality = {'on_time': 0, 'late': 0, 'hours_late': 0}
    for booking in agent_bookings:
        estimated_time = booking['estimated_time']
        arrival_time = booking['arrival_time']

        # change in time (t)
        t = arrival_time - estimated_time

        # if change >= Estimated Time, No_of_hours_late + t
        if t >= estimated_time:
            punctuality['late'] += 1
            punctuality['hours_late'] += t
        else:
            punctuality['on_time'] += 1

    #  average rating
    total_rating = 0
    for request in agent_requests:
        total_rating += request['rating']
    average_rating = total_rating / len(agent_requests)

    return average_rating, hours, completed_requests, shifts, punctuality




# Define the period
from datetime import datetime, timedelta

start_time = datetime.now() - timedelta(days=7)
end_time = datetime.now()

# Define the agent
agent = 'Agent1'

# Define the requests
requests = [
    {'agent': 'Agent1', 'time': start_time + timedelta(days=1), 'hours': 8, 'shift': 'Morning', 'rating': 2},
    {'agent': 'Agent1', 'time': start_time + timedelta(days=2), 'hours': 8, 'shift': 'Morning', 'rating': 4},
    {'agent': 'Agent1', 'time': start_time + timedelta(days=3), 'hours': 8, 'shift': 'Afternoon', 'rating': 5},
    {'agent': 'Agent1', 'time': start_time + timedelta(days=4), 'hours': 8, 'shift': 'Afternoon', 'rating': 3},
    {'agent': 'Agent1', 'time': start_time + timedelta(days=5), 'hours': 8, 'shift': 'Night', 'rating': 5},
    {'agent': 'Agent1', 'time': start_time + timedelta(days=6), 'hours': 8, 'shift': 'Night', 'rating': 4},
]

# Define the bookings
bookings = [
    {'agent': 'Agent1', 'time': start_time + timedelta(days=1), 'estimated_time': 2, 'arrival_time': 3},
    {'agent': 'Agent1', 'time': start_time + timedelta(days=2), 'estimated_time': 2, 'arrival_time': 3},
    {'agent': 'Agent1', 'time': start_time + timedelta(days=3), 'estimated_time': 2, 'arrival_time': 2},
    {'agent': 'Agent1', 'time': start_time + timedelta(days=4), 'estimated_time': 2, 'arrival_time': 3},
    {'agent': 'Agent1', 'time': start_time + timedelta(days=5), 'estimated_time': 2, 'arrival_time': 4},
    {'agent': 'Agent1', 'time': start_time + timedelta(days=6), 'estimated_time': 2, 'arrival_time': 3},
]

# Call the function
average_rating, hours, completed_requests, shifts, punctuality = agent_performance((start_time, end_time), agent, requests, bookings)

# Print the results
print(f'Average Rating: {average_rating}')
print(f'Number of hours laboured: {hours}')
print(f'Number of Complete Request: {completed_requests}')
print(f'Number of Shifts: {shifts}')
print(f'Punctuality: {punctuality}')

