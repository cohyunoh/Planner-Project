"""
    This the run script for the Flask app.
"""
from argparse import ArgumentParser
from flaskr import APP

parser = ArgumentParser(description="Process launch options.")
parser.add_argument("serve",
                    type=str,
                    nargs="?",
                    help="Serve the application on 0.0.0.0.",
                    default="")

args = parser.parse_args()

if __name__ == "__main__":
    if args.serve:
        APP.run(host="0.0.0.0", debug=True)
    else:
        APP.run(debug=True)
