from typing import List, Dict

# Define the type for a single tag dictionary
TagEntry = Dict[str, List[str]]

# Define the type for the collection of tag dictionaries
TAGS = List[TagEntry]

def is_valid_tag_entry(tag_entry: TagEntry, tags: TAGS) -> bool:
    """
    Check if the provided tag_entry matches one of the items in TAGS.
    Only one entry in the tag_entry should match the valid entries.

    :param tag_entry: A dictionary to be checked against TAGS.
    :param tags: A list of dictionaries representing valid tag entries.
    :return: True if tag_entry matches one of the items in tags, otherwise False.
    """
    # Iterate over each valid tag entry
    for valid_tag in tags:
        # Check if at least one valid entry matches
        if all(tag_entry.get(key) in value for key, value in valid_tag.items()):
            return True
    return False

TAGS = {
    [
        {
            "cost_center": ["csa"],
            "env": ["dev", "staging", "prod"],
            "owner": ["csa_owner"],
            "application": ["app1"],
        },
        {
            "cost_center": ["csb"],
            "env": ["dev", "staging", "prod"],
            "owner": ["csb_owner"],
            "application": ["app2"],
        },
        {
            "cost_center": ["csc"],
            "env": ["dev", "staging", "prod"],
            "owner": ["csc_owner"],
            "application": ["app3"],
        },
    ]
}
