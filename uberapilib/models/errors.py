# -*- coding: utf-8 -*-

"""
    uberapilib.models.errors
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 12/13/2016
"""
from .base_model import BaseModel

class Errors(BaseModel):

    """Implementation of the 'errors' model.

    TODO: type model description here.

    Attributes:
        code (string): TODO: type description here.
        status (int): TODO: type description here.
        title (string): TODO: type description here.

    """

    def __init__(self, 
                 code = None,
                 status = None,
                 title = None):
        """Constructor for the Errors class"""
        
        # Initialize members of the class
        self.code = code
        self.status = status
        self.title = title

        # Create a mapping from Model property names to API property names
        self.names = {
            "code" : "code",
            "status" : "status",
            "title" : "title",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            code = dictionary.get("code")
            status = dictionary.get("status")
            title = dictionary.get("title")
            # Return an object of this model
            return cls(code,
                       status,
                       title)
