def generate_subcategories_names(name):
    # Generate subcategory names based on the given name
    if not name.startswith("SUB "):
        # If the name does not start with "SUB ", add "SUB " prefix and append numerical suffixes
        return f"SUB {name}1", f"SUB {name}2"
    else:
        # If the name already starts with "SUB ", append numerical suffixes with a hyphen
        return f"SUB {name}-1", f"SUB {name}-2"
