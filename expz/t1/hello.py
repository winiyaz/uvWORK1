# Beauty Panty

# ------------------------------------------------------
from rich import print as rprint  # For rprinting
from rich.pretty import pprint  # For pretty printing
from rich import inspect  # For inspect
from rich.console import Console  # For console.print
from rich.markdown import Markdown  # For markdown
from rich.panel import Panel  # For Panel()
from rich import box  # For Panel Boxes
from rich.prompt import Prompt  # For Prompting

console = Console()  # Standard code to access console
# -------------------------------------------------------


def main():
    print("Hello from t1!")
    # Heading Panel here
    panel = Panel(
        """
Enjoy StinlySmellySWeaty women
""",
        title="Mistress",
        subtitle="ToiletSlave",
        style="Italic",
        border_style="magenta",
    )
    # Print the Panel
    console.print(panel)

    console.print(
        """
                  Centered Text - mistress fart
                  in mouth and nose
                  """,
        style="bold",
        justify="center",
    )


if __name__ == "__main__":
    main()
