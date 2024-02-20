from category.models import Category

def get_all_children(id):
    # Function to retrieve all children of a category using Breadth-First Search (BFS) algorithm
    all_children = []
    
    # Use a queue to keep track of category IDs during BFS
    tracking = []
    tracking.append(id)
    
    while len(tracking):
        # Pop the first ID from the queue
        id = tracking.pop(0)
        
        # Get immediate children of the current category
        get_next_level = Category.objects.get_children(id)
        
        # Add each child's ID to the queue for further exploration
        for i in get_next_level:
            tracking.append(i.id)
            # Append the child's ID to the result list
            all_children.append(i.id)
        
    return all_children
