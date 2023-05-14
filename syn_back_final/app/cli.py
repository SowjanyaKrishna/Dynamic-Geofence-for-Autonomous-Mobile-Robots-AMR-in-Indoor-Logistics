""" 
CLI extensions for flask can be added here
example:
flask data dummy # this might create some dummy data for testing
flask data builtin # this might create some builtin data
"""


def register(app):
    @app.cli.group()  # establishes the high level data cli group
    def data():
        """Adding Data to the DB automatically"""
        pass

    @data.command()  # defines what happens when flask data builtin is run
    def builtin():
        """Adding Builtin data to the database"""

        print("Ran builtin command")

    @data.command()
    def dummy():
        """Adding Test data to the database"""

        print("Ran dummy command")
