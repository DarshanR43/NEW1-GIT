def event_details(*args, **kwargs):
    event_info = {
        'name': kwargs.get('name', 'Unnamed Event'),
        'type': kwargs.get('type', 'General'),
        'date': kwargs.get('date', 'N/A'),
        'location': kwargs.get('location', 'N/A')
    }
    return event_info


def guest_list(*args, **kwargs):
    guests = args
    male_count = sum(1 for guest in guests if 'Male' in guest)
    female_count = sum(1 for guest in guests if 'Female' in guest)
    return male_count, female_count


def resource_allocation(*args, **kwargs):
    resource_rates = {'Chairs': 5, 'Tables': 10, 'Projectors': 100, 'Microphones': 15}
    resources = dict(item.split(', ') for item in args)
    total_expense = sum(int(resources.get(resource, 0)) * resource_rates.get(resource, 0) for resource in resources)
    return total_expense


def special_requests_handler(*args, **kwargs):
    special_requests = args[0]
    return special_requests != 'None'


def event_summary(*args, **kwargs):
    event_details_result = event_details(**kwargs)
    male_count, female_count = guest_list(*args)
    total_expense = resource_allocation(*args)
    special_requests = special_requests_handler(*args)

    print(f"Event: {event_details_result['name']}")
    print(f"Male Guests: {male_count}")
    print(f"Female Guests: {female_count}")
    print(f"Total Resource Expense: ${total_expense}")
    print(f"Special Requests: {special_requests}")


# # Sample Input 1
# event_summary(
#     "John Doe, Male, john@example.com; Jane Smith, Female, jane@example.com",
#     "Chairs, 150; Projectors, 2; Microphones, 5",
#     "Vegan Menu, Wheelchair Access",
#     name="Tech Conference", type="Conference", date="2023-09-15", location="Silicon Valley"
# )

# # Sample Input 2
# event_summary(
#     "John Doe, Male, john@example.com; Jane Smith, Female, jane@example.com; Alice Mathew, Female, alice@example.com",
#     "Chairs, 200; Tables, 5; Projectors, 2; Microphones, 3",
#     "None",
#     name="Tech Conference", date="2023-09-15"
# )