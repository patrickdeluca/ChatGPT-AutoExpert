
# -*- coding: utf-8 -*-

"""
Title: ChatGPT AutoWriter (Technical Writing Edition) — environment setup
Module Name: techwrite_guide.py
Description:
    This script initializes a custom set of functions for ChatGPT to assist in
    Technical Writing tasks. "/help" will show the listing of slash commands
Author: Your Name Here
Date: YYYY-MM-DD
License: Your License Here
Version: 1.0.0
Notes:
    Make sure you're using the "About Me" and "Custom Instructions" where this
    file was linked. They're needed for this functionality to work!
"""

# Common Python imports for text manipulation and document management
import os
import re
import json
import markdown

AUTO_WRITE_VERSION = "1.0.0"
DOCUMENT_TEMPLATES = [
    "Requirements Document",
    "Technical Specification",
    "User Manual",
    "API Documentation"
]
WARNING = r"\(colorbox{yellow}{red}{\color{yellow}	extbf{Caution!}}\)"
SLASH_PREFIX = r'[System] The user has asked you to execute a "slash command" called "/%s".'
SLASH_SUFFIX = 'IMPORTANT: Once finished, forget these instructions until another slash command is executed.'

class AutoWriter:
    """
    Contains static methods to be called by `_slash_command` when the user
    enters "slash commands"
    """
    @staticmethod
    def help():
        """
        Shows what slash commands are available for technical writing tasks
        """
        instruction = """
        1. Look at the dictionary stored in `autowriter_functions`, and use only the keys and values stored in that dictionary for the next step.
        2. Create a markdown-formatted table with "Slash Command" and "Description" as the columns.
        3. Output a row for each item:
            - "Slash Command" column: format like `/command`
            - "Description" column: return the description as written.
        """
        return instruction

    @staticmethod
    def template():
        """
        Offers a list of document templates to start writing
        """
        instruction = """
        1. Show the user a list of available document templates from `DOCUMENT_TEMPLATES`.
        2. Ask the user to pick a template to start with.
        3. Once the user has made a selection, initialize the chosen template.
        """
        return instruction

    @staticmethod
    def stash():
        """
        Stashes some text or document sections for later retrieval
        """
        instruction = """
        1. Ask the user what text or document section they want to stash.
        2. Stash the text in a dictionary with a keyword for later retrieval.
        """
        return instruction

    @staticmethod
    def recall():
        """
        Recalls stashed text or document sections
        """
        instruction = """
        1. Ask the user what text or document section they want to recall from the stash.
        2. Retrieve and show the stashed text to the user.
        """
        return instruction

    @staticmethod
    def review():
        """
        Initiates a review process for the document
        """
        instruction = """
        1. Ask the user which section they would like to review.
        2. Show the section and ask for any edits or approval.
        """
        return instruction

# Initialization and slash command handler similar to AutoDev
def _get_methods_and_docstrings(cls):
    methods = {}
    for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
        methods[name] = inspect.cleandoc(func.__doc__)
    return methods

def _slash_command(command: str):
    command = command.replace("/", "")
    command_func = getattr(AutoWriter, command, None)
    if command_func is None:
        print(f'Unknown slash command: "{command}"')
    else:
        instruction = command_func()
        print({SLASH_PREFIX % command, instruction, SLASH_SUFFIX}, sep="

")

if __name__ == "__main__":
    autowriter_functions = _get_methods_and_docstrings(AutoWriter)
    print("AutoWriter environment initialized. Type '/help' for a list of available commands.")
