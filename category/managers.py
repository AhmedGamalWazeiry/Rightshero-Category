from django.db import models, transaction
from category.utils import generate_subcategories_names
from rest_framework import status

class CategoryManager(models.Manager):
    # Custom manager for the Category model
    
    def create_category(self, name, parent=None):
        # Create a new category with the given name and optional parent
        category = self.create(name=name, parent=parent)
        return category

    @transaction.atomic
    def get_or_create_subcategories(self, parent):
        # Check if the parent category already has children
        if parent.category_set.exists():
            # If children already exist, return them
            children = parent.category_set.all()
            return children[0],children[1],status.HTTP_200_OK
        
        # Generate names for subcategories based on the parent's name
        parent_name = parent.name
        child1_name, child2_name = generate_subcategories_names(parent_name)
        
        # Create two subcategories and associate them with the parent
        child1 = self.create_category(child1_name, parent)
        child2 = self.create_category(child2_name, parent)
        
        return child1, child2,status.HTTP_201_CREATED
    
    def get_top_level_categories(self):
        # Retrieve top-level categories (categories without a parent)
        return self.filter(parent=None)
    
    def get_children(self, id):
        # Retrieve child categories based on the parent category's ID
        return self.filter(parent=id)
