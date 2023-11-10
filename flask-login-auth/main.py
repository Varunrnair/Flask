"""
This is a brief description of what this module does.

You can provide more detailed information here if necessary.
"""

# Rest of your code goes here

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    